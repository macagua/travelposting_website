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


#A private directmessage
class Message(models.Model):
    content = models.TextField(_('Content'))
    sender = models.ForeignKey(
        CustomerUser, related_name='sent_dm', verbose_name=_("Sender"), on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        CustomerUser, related_name='received_dm', verbose_name=_("Recipient"), on_delete=models.CASCADE)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)

    @property
    def unread(self):
        """returns whether the message was read or not"""
        if self.read_at is not None:
            return False
        return True

    def __str__(self):
        return self.content

    def save(self, **kwargs):
        if self.sender == self.recipient:
            raise ValidationError(_("You can't send messages to yourself"))

        if not self.id:
            self.sent_at = timezone.now()
        super(Message, self).save(**kwargs)
