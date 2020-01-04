from django.contrib.auth import get_user_model
from django.db import models
from apps.destinations.models import Destination
from django.contrib.auth.models import User
from apps.accounts.models import CustomerUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here.
class Recommendation(models.Model):
    destino = models.ForeignKey(
            Destination, related_name='destino', on_delete=None)
    user_recommendation = models.ForeignKey(
        CustomerUser,
        max_length=80,
        related_name='user_recommendation',
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    recommendation = models.TextField(blank=True, null=True, 
                                        help_text=_("Would you recommend this trip again? "))
    recommendation2 = models.TextField(blank=True, null=True,
                                        help_text=_("Do you think we should get better?"))



    class Meta:
        verbose_name = _("Recommendation")
        verbose_name_plural = _('Recommendations')
        # swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.destino


