from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommunityConfig(AppConfig):
    name = 'apps.community'
    verbose_name = _('Community')
