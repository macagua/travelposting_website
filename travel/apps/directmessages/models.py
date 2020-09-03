from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from apps.accounts.models import CustomerUser
from apps.destinations.formatChecker import ContentTypeRestrictedFileField


#A private directmessage
class Message(models.Model):
    subject = models.CharField(_('Subject'), blank=False, null=False, max_length=1000)
    content = models.TextField(_('Content'))
    attached = ContentTypeRestrictedFileField(
        upload_to='file_image/', 
        content_types=[
            'video/x-msvideo', 
            'video/mp4',
            'video/webm',
            'video/ogg',
            'video/x-msvideo',
            'audio/mpeg',
            'audio/ogg',
            'audio/x-wav',
            'application/x-7z-compressed',
            'application/pdf',
            'application/pdf',
            'application/msword', 
            'application/vnd.ms-powerpoint',
            'application/x-rar-compressed',
            'application/x-tar',
            'application/vnd.ms-excel',
            'application/zip',
            'image/jpeg',
            'image/gif',
            'image/png',
            'image/vnd.adobe.photoshop',
            'image/psd',
        ], 
        max_upload_size=5242880, 
        blank=True, 
        null=True
    )
    sender = models.ForeignKey(
        CustomerUser, related_name='sent_dm', verbose_name=_("Sender"), on_delete=models.CASCADE)
    recipient = models.ForeignKey(
        CustomerUser, related_name='received_dm', verbose_name=_("Recipient"), on_delete=models.CASCADE)
    sent_at = models.DateTimeField(_("sent at"), null=True, blank=True)
    read_at = models.DateTimeField(_("read at"), null=True, blank=True)

    class Meta:
        verbose_name_plural = _('Messages')
        verbose_name = _('Message')

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
