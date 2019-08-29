from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PaymentsConfig(AppConfig):
    name = 'apps.payments'
    verbose_name = _("Payments")

    def ready(self) -> None:
        """Registar los manejadores de signals"""
