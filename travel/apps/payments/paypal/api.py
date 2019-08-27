from django.core.exceptions import ImproperlyConfigured
from paypalrestsdk import Api
from apps.payments.paypal import settings

class ApiPayPal:
    def __init__(self, mode: str = settings.MODE, client_id: str = settings.CLIENT_ID,
                 client_secret: str = settings.CLIENT_SECRET) -> None:
        if client_id is None:
            raise ImproperlyConfigured("settings.PAYPAL_CLIENT_ID should be set to use PayPal")

        if client_secret is None:
            raise ImproperlyConfigured("settings.PAYPAL_CLIENT_SECRET should be set to use PayPal")

        self.mode = mode
        self.client_id = client_id
        self.client_secret = client_secret

    def get_credentials(self):
        return self.__dict__


default_api = Api(ApiPayPal(mode=settings.MODE).get_credentials())
