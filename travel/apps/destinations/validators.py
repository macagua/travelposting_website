from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def valid_video_extension(value):
    """
    Function that valid extension
    when upload video file in form
    """
    if (not value.name.endswith('.mp4') and
        not value.name.endswith('.ogg') and
        not value.name.endswith('.webm')):

        text = _("Files allowed")
        files = ".mp4, .ogg, .webm"
        raise ValidationError(text + ': ' + files)
