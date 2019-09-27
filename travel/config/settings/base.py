import os  # isort:skip
import environ
from django.utils.translation import gettext_lazy as _

gettext = lambda s: s

DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
ROOT_DIR = (
        environ.Path(__file__) - 3
)

APPS_DIR = ROOT_DIR.path("apps/")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR.path(".env")))


# Quick-start development settings - unsuitable for production

# Application definition

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

MIGRATION_MODULES = {

}

FIXTURE_DIRS = (
   os.path.join(ROOT_DIR, 'fixtures'),
)

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('de', gettext('de')),
    ('es', gettext('es'))
)

URL_NAME_LANGS = LANGUAGES

#MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'de', 'es')

TIME_ZONE = 'America/Caracas'

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [
    os.path.join(APPS_DIR, 'locale/'),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

MEDIA_URL = '/main/media/'
MEDIA_ROOT = os.path.join(os.getcwd(),'main/media/')
STATIC_ROOT = os.path.join(os.getcwd(), 'main/static/')
STATIC_URL = '/main/static/'

STATICFILES_DIRS = (
    os.path.join(os.getcwd(), 'main/private/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.dirname(__file__), 'main/templates').replace('\\', '/'),
            os.path.join(os.getcwd(), 'main/templates/'),
            os.path.join(os.getcwd(), 'main/templates/'),
            os.path.join(os.getcwd(), 'main/templates/admin'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'apps.landing_page.context_processor.get_ip',
                'cms.context_processors.cms_settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
]

DJANGO_APPS = [
    'djangocms_admin_style',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.humanize'
]

THIRD_PARTY = [
    'favicon',
    #below app is here accordinf to the docs for cms
    'apps.accounts.apps.AccountsConfig',
    'cms',
    'aldryn_apphooks_config',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_translation_tools',
    'parler',
    'sortedm2m',
    'taggit',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'mptt',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'django_summernote',
    'impersonate',
    'rest_framework',
    'nested_admin',
    'rosetta',
    'bootstrap_datepicker_plus',

]

LOCAL_APPS = [
    'apps.landing_page',
    'apps.utils.apps.UtilsConfig',
    'apps.payments.apps.PaymentsConfig',
    'apps.destinations',
    'apps.api',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY + LOCAL_APPS

# Email config
# https://docs.djangoproject.com/en/2.1/topics/email/#module-django.core.mail
# python -m smtpd -n -c DebuggingServer localhost:1025
ADMINS = [
    ('Dehivis Pérez', 'dehivis.oliver@gmail.com'),
]

MANAGERS = [
    ('Dehivis Pérez', 'dehivis.oliver@gmail.com'),
]

# Authentication options
AUTH_USER_MODEL = 'accounts.CustomerUser'
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'destinations:list'
LOGOUT_URL = 'accounts:logout'
LOGOUT_REDIRECT_URL = 'destination:list'

THUMBNAIL_HIGH_RESOLUTION = True


# Django Summernote config
SUMMERNOTE_CONFIG = {
    'iframe': True,
    'lazy': True,
    'js': (
        'destinations/js/summernote-map-plugin.js',
    )
}


#CMS_LANGUAGES = {
    ## Customize this
 #   1: [
 #       {
 #           'code': 'es',
 #           'name': gettext('es'),
#          'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    2: [
#        {
#            'code': 'en',
#            'name': gettext('en'),
#            'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    3: [
#        {
#            'code': 'de',
#            'name': gettext('de'),
#            'redirect_on_fallback': True,
#            'public': True,
#            'hide_untranslated': False,
#        },
#    ],
#    'default': {
#        'redirect_on_fallback': True,
#        'public': True,
#        'hide_untranslated': False,
#    },
#}

CMS_TEMPLATES = (
    ## Customize this
    ('index.html', 'Landing'),
    ('about.html', 'About us'),
    ('template_base_for_text.html', 'Template base'),
    ('tours.html', 'Tour'),
    ('magazine.html', 'Magazine'),
    ('community.html', 'Community'),
    ('datenschutz.html', 'Datenshutz'),
    ('coming-soon.html', 'Coming Soon'),
    ('hotels.html', 'Hotels template'),
    ('pricing.html', 'Pricing'),
    ('make_page.html', 'Make page'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

# Allow all host domains in DEBUG MODE

KEEP_COMMENTS_ON_MINIFYING = False

CKEDITOR_UPLOAD_PATH = "uploads_ckeditor/"
CKEDITOR_IMAGE_BACKED = 'pillow'

CKEDITOR_SETTINGS = {
    'disableNativeSpellChecker': False,
    'language' : 'es',
    'toolbar': 'Custom',
    'toolbar_Custom': [['Undo', 'Redo'], ["Bold", "Italic", "Underline", "Strike", "SpellChecker", "Subscript", "Superscript"],
                   ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'Blockquote'],
                   ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe'],
                   ["TabErrorle", "Link", "Unlink", "Anchor", "SectionLink"],
                   ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],['TextColor', 'BGColor' ],
                   ['Styles', 'Format', 'Font', 'FontSize' ], ['Maximize', 'ShowBlocks', 'Templates', '-', 'Source']],
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# ROSETTA
# https://django-rosetta.readthedocs.io/
# ------------------------------------------------------------------------------
ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = True
# ROSETTA_SHOW_AT_ADMIN_PANEL = True
ROSETTA_REQUIRES_AUTH = False
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_UWSGI_AUTO_RELOAD = True


#PRICES SETTINGS:
SHORT_DATE_FORMAT = "d/m/y"
DEFAULT_CURRENCY = 'USD'
CURRENCIES = ('USD', 'EUR')
CURRENCY_DECIMAL_PLACES = 4
CURRENCY_CHOICES = [
    ('USD', 'USD $'),
    ('EUR', 'EUR €'),
]
