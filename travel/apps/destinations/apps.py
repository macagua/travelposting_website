from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DestinationsConfig(AppConfig):
    name = 'apps.destinations'
    verbose_name = _('Destination Applications')
