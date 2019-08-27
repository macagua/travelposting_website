from djmoney.contrib.exchange.backends.base import SimpleExchangeBackend

from tour import settings


class RatesApiBackend(SimpleExchangeBackend):
    name = 'ratesapi.io'
    url = settings.RATES_API_URL
