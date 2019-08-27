import logging

from paypalrestsdk import Api

logger = logging.getLogger(__name__)


class ProductPayPal:
    def __init__(self, name, description, type, category, image_url, home_url, id=None):
        self.name = name
        self.description = description
        self.type = type
        self.category = category
        self.image_url = image_url
        self.home_url = home_url
        self.id = id

    def list(self, credentials, **params) -> dict:
        api = Api(credentials)
        logger.debug(f"Listando los productos")
        return api.get('v1/catalogs/products')

    def create(self, credentials: dict) -> dict:
        api = Api(credentials)
        logger.debug(f"Creando el producto {self.name}")
        return api.post('v1/catalogs/products', self.__dict__)

    def detail(self, credentials) -> dict:
        api = Api(credentials)
        logger.debug(f"Mostrando los detalles del producto: {self.name}")
        return api.get(f'v1/catalogs/products/{self.name}')

    def update(self, credentials, data: dict) -> dict:
        api = Api(credentials)
        logger.debug(f"Actualizando el producto {self.name}")
        return api.patch(f'v1/catalogs/products/{self.id}',
                         {'op': 'replace', 'path': f'/description', 'value': data['description']})
