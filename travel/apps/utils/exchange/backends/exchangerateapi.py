from urllib.parse import urljoin

from djmoney.contrib.exchange.backends.base import SimpleExchangeBackend

from tour import settings


class ExchangeRateApiBackend(SimpleExchangeBackend):
    name = 'exchangerateapi.io'
    url = settings.EXCHANGE_RATE_API_URL

    def __init__(self, url=settings.EXCHANGE_RATE_API_URL, base='latest'):
        self.url = urljoin(url, base)
