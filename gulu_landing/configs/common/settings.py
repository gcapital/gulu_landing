""" Base settings for gulu-landing project

If you need to override any of these settings for local/dev environment,
create a settings_local.py and include any needed settings.
"""

__author__ = "Ben Homnick <bhomnick@gmail.com>"

import django
import logging
import os

# Base paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
SITE_DOMAIN = 'localhost.local:8000'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ben Homnick', 'bhomnick@gmail.com'),
)

INTERNAL_IPS = ('127.0.0.1',)

MANAGERS = ADMINS

DATABASES = {
    'default': {
    	'ENGINE': 'django_mongodb_engine',
    	'NAME': 'gulu_landing',
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Taipei'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = "4d8b1216217db90ad400001c"

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(SITE_ROOT, 'assets')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://localhost:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a-!jr$fbbp1@uhkaclf&+wghgzttqbj1&%+6+o6*z!$2mr53f*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	  'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',
	'django.core.context_processors.auth',
	'django.core.context_processors.i18n',
	'django.core.context_processors.debug',
	'django.core.context_processors.media',
	'django.contrib.messages.context_processors.messages',
	'facebook.context_processors.facebook_common',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

APPEND_SLASH = True

ROOT_URLCONF = 'gulu_landing.configs.common.urls'

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, 'templates')
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',

	'facebook',
	'landing',
)

### Email
DEFAULT_FROM_EMAIL = "Gulu <do.not.reply@gulu.com>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

### Logging
logging.basicConfig(
    level=logging.DEBUG,
)

### Storage
AWS_ACCESS_KEY_ID = "AKIAIIR2TKOBEZ33OGHA"
AWS_SECRET_ACCESS_KEY = "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"
AWS_S3_SECURE_URLS = False

### Facebook
FACEBOOK_APP_ID = "157405627645845"
FACEBOOK_APP_SECRET = "138b27ab32c9c3015560f2efe218becb"

# Allow for local (per-user) override
try:
    from settings_local import *
except ImportError:
    pass
