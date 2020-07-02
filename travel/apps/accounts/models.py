from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core import validators
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from apps.landing_page.models import Plan
from apps.utils.views import get_referal_code

from random import randint
import uuid


DEGRE_CHOICES = (
    ('sra', _('Mrs.')),
    ('sr', _('Mr.')),
    ('divers', _('Divers')),
    ('dr', _('Dr.')),
    ('prof', _('Prof.')),
    ('lic', _('Lic.')),
    ('agrupacion', _('Grouping')),
    ('prof-dr', _('Prof. Dr.'))
)

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomerUser(AbstractUser):
    """Define a model to deal with our customers."""

    username = None

    email = models.EmailField(
        _('email address'),
        unique=True,
    )

    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        verbose_name=_('Plan'),
        blank=True,
        null=True,
    )

    subscription_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        editable=False,
        validators=[validators.MinLengthValidator(3)],
    )

    coupon = models.CharField(
        _('Coupon'),
        max_length=50,
        blank=True,
        null=True,
    )

    business_name = models.CharField(
        _("Company name"),
        max_length=150,
        blank=True,
        null=True,
    )

    business_address = models.CharField(
        _("Commercial address"),
        max_length=150,
        blank=True,
        null=True,
    )

    postal_code = models.CharField(
        _("Postal code"),
        max_length=50,
        blank=True,
        null=True,
    )

    state = models.CharField(
        _("City / State / Parish"),
        max_length=50,
        blank=True,
        null=True,
    )

    country = models.CharField(
        _("Country"),
        max_length=50,
        blank=True,
        null=True,
    )

    language = models.CharField(
        _("Languages in which you are interested in sending or receiving information"),
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    comment = models.TextField(
        _("Do you have something to tell us?"),
        blank=True,
        null=True,
    )

    degree = models.CharField(
        _("Title (Contact person)"),
        max_length=20,
        choices=DEGRE_CHOICES,
        blank=True,
        null=True,
    )

    business_position = models.CharField(
        _("Position in the company"),
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        _("Leave us a phone number where we can contact you"),
        max_length=20,
        blank=True,
        null=True,
    )

    mobile = models.CharField(
        _("Mobile number or WhatsApp"),
        max_length=20,
        blank=True,
        null=True,
    )

    web_site = models.URLField(
        _("Leave us your web address"),
        blank=True,
        null=True,
    )

    ref_code = models.CharField(
        _("Code Referral"),
        max_length=20,
        default=get_referal_code,
    )

    facebook = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    instagram = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    twitter = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    linkedin = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    about_me = models.TextField(
        _('About me'),
        null=True,
        blank=True,
        max_length=2000,
    )

    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
    )

    pinterest = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_community = models.BooleanField(default=True)

    last_ip = models.GenericIPAddressField(protocol='IPv4', verbose_name="Last Login IP", null=True, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    slug = models.SlugField(unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    def add_slug(self):
        name = self.get_full_name() if not self.business_name else self.business_name
        name = name if name.strip() != '' else uuid.uuid4()
        slug = slugify(name)
        if CustomerUser.objects.filter(slug=slug).exists():
            slug = slugify(name+"-"+str(randint(300,999)))
        self.slug = slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.add_slug()
        super().save(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        verbose_name = _("User")
        verbose_name_plural = _('Users')
        # swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('accounts:user-details', kwargs={'pk': self.pk})


class LastVisitIP(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    last_ip_login = models.GenericIPAddressField(protocol='IPv4', verbose_name="Last Login", null=True, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)

    @classmethod
    def add(self, user):
        last, new = self.objects.get_or_create(
                user=user,
                last_ip_login=user.last_ip,
                defaults={
                    'location': user.location 
                    })

    def str(self):
        return str(self.user) +" "+ str(self.last_ip_login)

### Model to interact between one user and another
'''
The preceding code shows the Contact model we will use for user relationships. It contains the following fields:

-> user_from: ForeignKey for the user that creates the relationship
-> user_to: ForeignKey for the user being followed
-> created: A DateTimeField field with auto_now_add=True to store the time when the relationship was created

'''
class Contact(models.Model):
    user_from = models.ForeignKey('accounts.CustomerUser',
                                  related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey('accounts.CustomerUser',
                                related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return _('%(user_from)s follows %(user_to)s') % {
            'user_from': self.user_from,
            'user_to': self.user_to
        }


# Add following field to User dynamically
CustomerUser.add_to_class('following',
                  models.ManyToManyField('self',
                                         through=Contact,
                                         related_name='followers',
                                         symmetrical=False))


from apps.destinations.models import Destination

class Comment(models.Model):
    post = models.ForeignKey(
        Destination, related_name='comments', on_delete=None)
    user_comment = models.ForeignKey(
        CustomerUser,
        max_length=80,
        related_name='user_comment_to',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    user_answer = models.ForeignKey(
        CustomerUser,
        max_length=80,
        related_name='user_answer_to',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=200, null=False, blank=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = models.IntegerField(
        _('Parent'),
        null=True,
        blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return _('Comment by %(body)s') % {'body': self.body}
