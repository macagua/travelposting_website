from djmoney.contrib.exchange.backends.base import SimpleExchangeBackend

from tour import settings


class OpenRatesBackend(SimpleExchangeBackend):
    name = 'openrates.io'
    url = settings.OPEN_RATES_URL
