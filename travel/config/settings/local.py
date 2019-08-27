from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="h*p!f-*zz=jcf8k)bzne&twvelpn)1suh!&$p5at@vnjp1vva8",
)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="*")

# PAYPAL
# ------------------------------------------------------------------------------
PAYPAL_MODE = env("PAYPAL_MODE", default="sandbox")
PAYPAL_CLIENT_ID = env(
    "PAYPAL_CLIENT_ID",
    default="AVkQSkUEOYynxFx0jLYuLSE6gDk3vhtiE400AFUO4fymFw8p6cuf_40hB7gD7k3n5rwTMOzXy9mlcAS7"
)
PAYPAL_CLIENT_SECRET = env(
    "PAYPAL_CLIENT_SECRET",
    default="EP9Lvor-cD0GNqLeincWEbiVyFO8wOX9xzuJXvvyIXtzLNaq4nsnrVP_8vN7QS4ImjWa0W1U6uuXrmEc"
)

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST', default='mail.agenturserver.de')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='travelsolution@travelposting.com')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='T$Ss_2019!**T')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-DEFAULT_FROM_EMAIL
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='Travel Solution <travelsolution@travelposting.com>')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env.bool('EMAIL_SUBJECT_PREFIX', default='TravelPosting:')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SERVER_EMAIL
SERVER_EMAIL = env('SERVER_EMAIL', default='travelsolution@travelposting.com')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-EMAIL_PORT
EMAIL_PORT = env('EMAIL_PORT', default='465')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-use-tls
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=False)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-use-ssl
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=True)
ACCOUNT_ACTIVATION_DAYS = env.bool('ACCOUNT_ACTIVATION_DAYS', default=7)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
