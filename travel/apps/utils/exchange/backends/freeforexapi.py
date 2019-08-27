from djmoney.contrib.exchange.backends.base import SimpleExchangeBackend

from tour import settings


class FreeForexApiBackend(SimpleExchangeBackend):
    name = 'freeforexapi.com'
    url = settings.FREE_FOREX_API_URL
