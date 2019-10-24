import logging
from typing import Any

from django.core.management.base import BaseCommand, CommandParser

from apps.payments.paypal.api import ApiPayPal
from apps.payments.paypal.product import ProductPayPal
from apps.payments.paypal import settings

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create product in PayPal"

    def add_arguments(self, parser: CommandParser) -> None:
        """
        Crear los arguments que acepta el command.
        :param parser:
        :return: None
        """
        parser.add_argument('--mode', type=str)

    def handle(self, *args: Any, **options: Any) -> None:
        """
        Create el product de travelandsolutions
        :param args:
        :param options:
        :return: None
        """
        self.stdout.write(self.style.SUCCESS(f"Empezando a crear el product Travel Solutions."))
        pp = ProductPayPal('Travelposting', 'TRAVElPOSTING es el Software de xposting-service, con él podrá conectarse a más de MILES de empresas registradas a nivel mundial, ayudandolo a ofrecer sus destinos turísticos a otras empresas.',
                           'DIGITAL', 'SOFTWARE',
                           'https://travelandsolutions.com/uploads/django-summernote/2019-07-31/c6fc3f44-5b42-49df-bbec-2724ddb633a0.jpg',
                           'https://travelposting.com')
        self.stdout.write(self.style.SUCCESS(f"Creado el objeto product {pp.name}"))
        ap = ApiPayPal(mode=settings.MODE)
        resp = pp.create(ap.get_credentials())
        self.stdout.write(self.style.SUCCESS(f"Respuesta valida."))
        for k, v in resp.items():
            self.stdout.write(self.style.SUCCESS(f"{k}: {v}"))
