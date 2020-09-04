from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AdvertisementsConfig(AppConfig):
    name = 'apps.advertisements'
    verbose_name = _('Advertisements')
