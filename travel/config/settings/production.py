from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# PAYPAL
# ------------------------------------------------------------------------------
PAYPAL_MODE = env("PAYPAL_MODE")
PAYPAL_CLIENT_ID = env("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = env("PAYPAL_CLIENT_SECRET")

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host
EMAIL_HOST = env('EMAIL_HOST')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host-user
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-DEFAULT_FROM_EMAIL
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='Travel Solution <travelsolution@travelposting.com>')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env.bool('EMAIL_SUBJECT_PREFIX', default='TravelPosting:')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-SERVER_EMAIL
SERVER_EMAIL = env('SERVER_EMAIL')
# https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-EMAIL_PORT
EMAIL_PORT = env('EMAIL_PORT', default='465')
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-use-tls
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
# https://docs.djangoproject.com/en/2.2/ref/settings/#email-use-ssl
EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL', default=False)
ACCOUNT_ACTIVATION_DAYS = env.bool('ACCOUNT_ACTIVATION_DAYS', default=7)

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "verbose" }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.db.backends": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
