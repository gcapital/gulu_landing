# -*- coding: utf-8 -*-

import logging
import os

import django

# Base paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

# Debugging
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gulu', 'gulu@geniecapital.com.tw'),
)

MANAGERS = ADMINS

# Email
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = 'gulu@geniecapital.com.tw'
EMAIL_HOST_PASSWORD = '123456'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
SERVER_EMAIL = 'do.not.reply@gulu.com'

# Database
# Note: DATABASE_USER and DATABASE_PASSWORD are defined in the staging and
# production settings.py files. For local use, either define them in
# local_settings.py or ignore to use your local user.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'gulu', # Or path to database file if using sqlite3.#
		'USER': 'gulu', # Not used with sqlite3.
        'PASSWORD': 'PrtPA4KV4E', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time
TIME_ZONE = 'Asia/Taipei'

# Local language
LANGUAGE_CODE = 'en-us'

# Available languages
LANGUAGES = (
    ('en', u"English"),
    ('ja', u"日本語"),
	('zh-tw', u"中文"),
)

# Site framework
SITE_ID = 1

# Internationalization
USE_I18N = True

# Localization
USE_L10N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://localhost.local:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'g!@h6(n*45*u2(!2jhbrhc0o@%c249cf$ohz0gkhwr-o_eo&&)'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#    'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = ( 
	'django.core.context_processors.request',
	'django.core.context_processors.i18n',
	'django.core.context_processors.debug',
	'django.core.context_processors.media',
	#'django.contrib.messages.context_processors.messages',
 )

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    #'django.middleware.cache.UpdateCacheMiddleware',
    'localeurl.middleware.LocaleURLMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

APPEND_SLASH = True

ROOT_URLCONF = 'gulu.configs.common.urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
    #'django.contrib.contenttypes',
    #'django.contrib.sites',
    'globals',
)

# Predefined domain
MY_SITE_DOMAIN = 'localhost.local:8000'

# Email
# run "python -m smtpd -n -c DebuggingServer localhost:1025" to see outgoing
# messages dumped to the terminal
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025
#DEFAULT_FROM_EMAIL = 'do.not.reply@ec2-175-41-161-6.ap-southeast-1.compute.amazonaws.com'

# Caching
CACHE_MIDDLEWARE_KEY_PREFIX='gulu'
CACHE_MIDDLEWARE_SECONDS=90 * 60 # 90 minutes
CACHE_BACKEND="dummy:///"

# Logging
logging.basicConfig(
    level=logging.DEBUG,
)

MAILSNAKE_API_KEY = '2770d86d0d2ef3b5daf38b2749cd4304-us2'


# Allow for local (per-user) override
try:
    from settings_local import *
except ImportError:
    pass