from djmoney.contrib.exchange.backends.base import SimpleExchangeBackend

from tour import settings


class ExchangeRateAPiBackend(SimpleExchangeBackend):
    name = 'exchangerate-api.com'
    url = settings.EXCHANGE_RATE_API_COM_URL
