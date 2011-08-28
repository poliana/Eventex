import os
PROJECT_DIR = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'database.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DEFAULT_FROM_EMAIL = 'contato@eventex.com'


TIME_ZONE = 'America/Sao_Paulo'


LANGUAGE_CODE = 'pt-br'

SITE_ID = 1


USE_I18N = True


USE_L10N = True


MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')


MEDIA_URL = '/media/'


ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'


SECRET_KEY = 'rclkre-&5sknt8@f65u!jp&1vwu(-_nobr0gj1oa_@c(q@#)nc'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'core',
    'subscription',
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

