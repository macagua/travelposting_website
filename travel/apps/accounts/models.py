from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core import validators
from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from apps.landing_page.models import Plan
from django.conf import settings

DEGRE_CHOICES = (
    ('sra', _('Sra.')),
    ('sr', _('Sr.')),
    ('divers', _('Divers')),
    ('dr', _('Dr.')),
    ('prof', _('Prof.')),
    ('lic', _('Lic.')),
    ('agrupacion', _('Agrupación')),
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
        _("Nombre de la empresa"),
        max_length=150,
        blank=True,
        null=True,
    )

    business_address = models.CharField(
        _("Dirección comercial"),
        max_length=150,
        blank=True,
        null=True,
    )

    postal_code = models.CharField(
        _("Código postal"),
        max_length=50,
        blank=True,
        null=True,
    )

    state = models.CharField(
        _("Ciudad / Estado / Parroquia"),
        max_length=50,
        blank=True,
        null=True,
    )

    country = models.CharField(
        _("País"),
        max_length=50,
        blank=True,
        null=True,
    )

    language = models.CharField(
        _("Idiomas en los que le interesa enviar o recibir información"),
        max_length=2,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
    )

    comment = models.TextField(
        _("¿Tienen algo que decirnos?"),
        blank=True,
        null=True,
    )

    degree = models.CharField(
        _("Título (Persona de contacto)"),
        max_length=20,
        choices=DEGRE_CHOICES,
        blank=True,
        null=True,
    )

    business_position = models.CharField(
        _("Cargo en la empresa"),
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(
        _("Déjenos un número de teléfono donde le podamos contactar"),
        max_length=20,
        blank=True,
        null=True,
    )

    mobile = models.CharField(
        _("Número móvil o WhatsApp"),
        max_length=20,
        blank=True,
        null=True,
    )

    web_site = models.URLField(
        _("Déjenos su dirección Web"),
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta(AbstractUser.Meta):
        verbose_name = _("Usuario")
        verbose_name_plural = _('Usuarios')
        # swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse_lazy('accounts:user-details', kwargs={'pk': self.pk})
