from django.db import models
from django.core import validators
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.managers import TreeManager
from mptt.models import MPTTModel
from mptt.querysets import TreeQuerySet
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from djmoney.models.fields import MoneyField
from djmoney.money import Money


class PriceType(models.Model):
    """
        This models is for the price type.
    """
    type = models.CharField(
        _('Type'),
        blank=False,
        null=False,
        max_length=20,
    )

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = _('Price type')
        verbose_name_plural = _('Price types')


class Price(models.Model):
    type = models.ForeignKey(
        PriceType,
        on_delete=None,
        verbose_name=_('Price Type'),
    )

    value  = MoneyField(
        _('Value'),
        max_digits=19,
        decimal_places=2,
        default_currency='EUR',
        default=Money(0, 'EUR'),
    )

    def __str__(self):
        return f"{self.type} - {self.value}"

    class Meta:
        verbose_name = _("Price")
        verbose_name_plural = _("Prices")


class Plan(models.Model):
    paypal_id = models.CharField(
        _("Paypal ID"),
        max_length=50,
        blank=True,
        null=True,
        validators=[validators.MinLengthValidator(3)],
    )

    name = models.CharField(
        _('name'),
        max_length=50,
    )

    price = models.ManyToManyField(
        'Price',
        blank=True,
        verbose_name='Prices',
    )

    features = models.ManyToManyField(
        'Feature',
        related_name='features',
        through='PlanFeature',
        through_fields=('plan', 'feature'),
        verbose_name=_('features'),
    )

    active = models.BooleanField(
        _('active'),
        default=True,
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name_plural = _('plans')
        verbose_name = _('plan')

    def active_features(self, active=True):
        return self.planfeature_set.active(active).select_related('feature')


class PlanFeatureQuerySet(models.QuerySet):
    def active(self, active=True):
        return self.filter(active=active)


class PlanFeatureManager(models.Manager):
    def get_queryset(self):
        return PlanFeatureQuerySet(self.model, using=self._db)


class PlanFeature(models.Model):
    plan = models.ForeignKey(
        'Plan',
        on_delete=models.CASCADE,
        verbose_name=_('plan'),
    )

    feature = models.ForeignKey(
        'Feature',
        on_delete=models.CASCADE,
        verbose_name=_('feature'),
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    active = models.BooleanField(
        _('active'),
        default=False,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = PlanFeatureManager.from_queryset(PlanFeatureQuerySet)()

    def __str__(self):
        return f"{self.plan.name}-{self.feature.name}"

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name_plural = _('plan-features')
        verbose_name = _('plan-feature')


class FeatureTreeQuerySet(TreeQuerySet):
    def active(self, active=True):
        return self.filter(active=active)

    def validate_plan(self, plan):
        return self.filter(
            Q(validated_plan__isnull=True) |
            Q(validated_plan=plan)
        )


class FeatureTreeManager(TreeManager):
    def get_queryset(self, *args, **kwargs):
        return FeatureTreeQuerySet(self.tree_model, using=self._db)


class Feature(MPTTModel):
    name = models.CharField(
        _('name'),
        max_length=250,
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_('parent'),
    )

    validated_plan = models.ForeignKey(
        'Plan',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('validated to plan'),
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=0,
    )

    active = models.BooleanField(
        _('active'),
        default=False,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = FeatureTreeManager.from_queryset(FeatureTreeQuerySet)()

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        ordering = ('order',)
        verbose_name = _('feature')
        verbose_name_plural = _('features')

    def get_children_active(self):
        return self.get_children().active()


class BaseAbstractExtra(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    icon = models.CharField(
        _('icon'),
        max_length=20,
        default='fa-',
        help_text=_(
            "Icons use of Font Awesome 4.7.0, info: https://fontawesome.com/v4.7.0/icons/"
        ),
    )

    active = models.BooleanField(
        _('active'),
        default=False,
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('order', 'created_at')
        abstract = True


class Service(BaseAbstractExtra):
    description = models.TextField(
        _('description'),
        max_length=150,
    )

    class Meta(BaseAbstractExtra.Meta):
        verbose_name_plural = _('services')
        verbose_name = _('service')


class Statistic(BaseAbstractExtra):
    value = models.CharField(
        _('value'),
        max_length=50,
    )

    counter = models.BooleanField(
        _('counter'),
        default=True,
    )

    class Meta(BaseAbstractExtra.Meta):
        verbose_name_plural = _('statistics')
        verbose_name = _('statistic')


class Testimony(models.Model):
    author = models.CharField(
        _('author'),
        max_length=100,
    )

    comment = models.TextField(
        _('comment'),
    )

    place = models.CharField(
        _('place'),
        max_length=50,
    )

    photo = models.ImageField(
        _('photo'),
        upload_to='landing/testimonies/',
        blank=True,
        null=True,
    )

    active = models.BooleanField(
        _('active'),
        default=False,
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return f"{self.author}"

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name_plural = _("Testimonies")
        verbose_name = _("Testimony")


class Slider(models.Model):
    title = models.CharField(
        _('title'),
        max_length=150,
        blank=True,
        null=True,
    )

    description = models.TextField(
        _('description'),
    )

    image = models.ImageField(
        _('image'),
        upload_to='landing/slider',
    )

    active = models.BooleanField(
        _('active'),
        default=True,
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    type = models.CharField(
        _('type'),
        max_length=5,
        choices=(
            ('h', _('Header')),
            ('c', _('Company')),
        ),
        default='h',
    )

    site = models.URLField(
        _('site'),
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    updated_at = models.DateTimeField(_('Updated at'), auto_now=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ('order', 'created_at')
        verbose_name_plural = _("sliders")
        verbose_name = _("slider")


class Magazine(models.Model):
    """
    Model useful for create new magazines objects to our database.

    Args:
        name: The name to be displayed in the webpage.
        editor: slug to be displayed on website.
        files: Img preview to show.
        status: status (publish/unpublish) of each magazine.
        order: position in list view.
        kliche: click to make it outstanding.
    """
    name = models.CharField(
        _('Name'),
        max_length=50,
    )

    editor = models.CharField(
        _('Editor'),
        max_length=50,
    )

    files = FilerImageField(
        verbose_name=_("Files"),
        null=True,
        blank=True,
        on_delete=False,
        related_name='file_magazine',
    )

    magazine = FilerFileField(
        null=True,
        blank=True,
        related_name="magazine_file",
        on_delete=False,
    )

    status = models.BooleanField(
        _('is active?'),
        default=True,
    )

    order = models.PositiveSmallIntegerField(
        _('order'),
        default=1,
    )

    kliche = models.BooleanField(
        _('outstanding'),
        default=False,
    )

    class Meta:
        ordering = ('name','order',)
        verbose_name = _('Megazine')
        verbose_name_plural = _('Megazines')

    def __str__(self):
        return f"{self.name}"



class DeleteReg(models.Model):
    first_name = models.CharField(_('First Name'), 
                    max_length=50, 
                    null=False, 
                    blank=False,
    )
    last_name = models.CharField(_('Last Name'),
                    max_length= 50,
                    null = False,
                    blank = False,
    )
    email = models.EmailField(_('Email'),
                max_length = 100,
                blank=False,
                null = False
    )
    agree = models.BooleanField(
        _('Agree?'),
        default=True,
    )
    status = models.BooleanField(
        _('Status?'),
        default=True,
    )

    def __str__(self):
        return f"{self.firts_name}-{self.last_name}"

    class Meta:
        verbose_name_plural = _("Delete Registers")
        verbose_name = _('Delete Register')


class PrivacySetting(models.Model):
    ip = models.GenericIPAddressField(_('Address IP'), blank=True, null=True)
    cookie = models.BooleanField(_('cookies'), default=True)
    ganality = models.BooleanField(_('Google Analitys'), default=True)
    facebook = models.BooleanField(_('Facebook Pixel'), default=True)
    twitter = models.BooleanField(_('Twitter'), default=True)
    pinteres = models.BooleanField(_('Pinterest'), default=True)

    def __str__(self):
        return f"{self.ip}"

    class Meta:
        verbose_name_plural = _('Privacity Settings')
        verbose_name = _('Privacity Setting')


class ContactUs(models.Model):
    email = models.EmailField(
        _('Email'),
        blank=False,
        null = False
    )
    message = models.CharField(
        _('Message'),
        max_length = 300,
        blank = False,
        null = False
    )
    ip_client = models.GenericIPAddressField(
        _('Address IP'),
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name_plural = _('Contact Us')
        verbose_name = _('Contacts')
