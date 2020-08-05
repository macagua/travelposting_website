from django.db import models
from apps.destinations.models import Destination
from apps.accounts.models import CustomerUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Recommendation(models.Model):
    destino = models.ForeignKey(
        Destination,
        verbose_name=_('Destination'),
        related_name='destino',
        on_delete=None,
    )

    user_recommendation = models.ForeignKey(
        CustomerUser,
        verbose_name=_('User Recommendation'),
        max_length=80,
        related_name='user_recommendation',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    recommendation = models.TextField(
        _('Recommendation'),
        blank=True,
        null=True,
        help_text=_("Would you recommend this trip again?"),
    )

    recommendation2 = models.TextField(
        _('Recommendation Others'),
        blank=True, null=True,
        help_text=_("Do you think we should get better?"),
    )

    class Meta:
        verbose_name = _("Recommendation")
        verbose_name_plural = _('Recommendations')

    def __str__(self):
        return self.recommendation


class Referral(models.Model):
    user = models.OneToOneField(
        CustomerUser,
        verbose_name=_('User'),
        related_name='user',
        on_delete=models.CASCADE,
    )

    referredBy = models.ForeignKey(
        CustomerUser,
        verbose_name=_('Referred By'),
        related_name='referredBy',
        on_delete=models.CASCADE,
    )

    code = models.CharField(
        _('Code'),
        max_length=40,
    )

    created_at = models.DateTimeField(_('Created at'), default=timezone.now)

    class Meta:
        verbose_name = _('Referral')
        verbose_name_plural = _('Referrals')

    def __str__(self):
        if self.user:
            return f"{self.user} ({self.code})"
        else:
            return self.code
