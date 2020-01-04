from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import CustomerUser


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
