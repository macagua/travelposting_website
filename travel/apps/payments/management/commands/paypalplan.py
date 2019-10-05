import json
import logging
from typing import Any

from django.core.management.base import BaseCommand, CommandParser

from apps.payments.paypal.resources import Plan
from config.settings.base import CURRENCIES, DEFAULT_CURRENCY

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create plans in paypal"

    def add_arguments(self, parser: CommandParser) -> None:
        """
        Create arguments for plans paypal
        :param parser:
        :return: None
        """

        parser.add_argument('file', type=open, help='Archivo con las opciones del plan en formato json')
        parser.add_argument('-a', '--action', type=str, choices=('create', 'replace', 'find', 'activate',
                                                                 'deactivate', 'all'),
                            default='create', help='Action for run')
        # parser.add_argument('product_id', type=str, help='Id del producto')
        # parser.add_argument('name', type=str, help='Name of plan')
        # parser.add_argument('description', type=str, help='Descripcion del plan')
        # parser.add_argument('-s', '--status', help='Estado del plan', type=str, default='ACTIVE',
        #                     choices=('ACTIVE', 'CREATED', 'INACTIVE'))
        # parser.add_argument('-q', '--quantity-supported', action='store_true', help='Quantity supported')
        #
        # parser.add_argument('--b-c', '--billing-cycles', action='append', help='Billing cycles', type=dict)

        # parser.add_argument('--b-c-tt', '--billing-cycles-tenure-type', type=str, default='TRIAL',
        #                     dest='billing_cycles', choices=('TRIAL', 'REGULAR'), help='tenure type', metavar='Tenure')
        # parser.add_argument('--b-c-s', '--billing-cycles-sequence', type=int, default=1, help='Sequence',
        #                     dest='billing_cycles', metavar='Sequence')
        # parser.add_argument('--b-c-tc', '--billing-cycles-total-cycles', type=int, default=0, dest='billing_cycles',
        #                     help='Total cycles', metavar='Total')
        #
        # payment = parser.add_argument_group('Payment preferences', 'Preferencias de pago.')
        # payment.add_argument('--p-abo', '--payment-auto-bill-outstanding', action='store_true',
        #                      help='Auto bill outstanding')
        # payment.add_argument('--p-ffa', '--payment-fee-failure-action', type=str, default='CONTINUE',
        #                      choices=('CONTINUE', 'CANCEL'), help='setup fee failure action')
        # payment.add_argument('--p-ft', '--payment-failure-threshold', type=int, default=0,
        #                      help='payment failure threshold')
        #
        # setup_fee = payment.add_argument_group('setup_fee', 'settings of fee')
        # setup_fee.add_argument('--p-f-cc', '--payment-fee-currency_code', type=str, choices=CURRENCIES,
        #                        default=DEFAULT_CURRENCY, help='Currency code del plan')
        # setup_fee.add_argument('--p-f-v', '--payment-fee-value', type=float, help='Monto', default=0.00)
        #
        # taxes = parser.add_argument_group('Taxes', 'Taxes description')
        # taxes.add_argument('--t-p', '--taxes-percentage', type=float, default=0.00)
        # taxes.add_argument('--t-i', '--taxes-inclusive', action='store_true', help='Taxes inclusive')

    def handle(self, *args: Any, **options: Any) -> None:
        """
        Create plans for paypal
        :param args:
        :param options:
        :return: None
        """
        data = json.loads(options.get('file').read())
        action = options.get('action')

        self.stdout.write(self.style.SUCCESS(f'{action.capitalize()} plan {data["name"]}'))
        plan = Plan(data)

        if hasattr(plan, action):
            func = getattr(plan, action)
            if func():
                self.stdout.write(self.style.SUCCESS(f"Plan {plan.name} {action} successfully with id: {plan.id}"))
            else:
                self.stderr.write(self.style.ERROR(f"Plan not {action} with errors: {plan.error}"))
        else:
            self.stderr.write(self.style.ERROR(f"Action not found"))
