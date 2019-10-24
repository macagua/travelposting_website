from config.settings import local as settings

CLIENT_ID = getattr(settings, 'PAYPAL_CLIENT_ID', None)
CLIENT_SECRET = getattr(settings, 'PAYPAL_CLIENT_SECRET', None)
MODE = getattr(settings, 'PAYPAL_MODE', 'live')
PRODUCT_ID = getattr(settings, 'PAYPAL_PRODUCT_ID', None)
