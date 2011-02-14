""" Base settings for Gulu Django project 

If you need to override any of these settings for local/dev environment,
create a settings_local.py and include any needed settings.
"""

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: settings.py 627 2011-02-01 01:11:17Z sean $"

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

OAUTH_AUTH_VIEW = "piston.authentication.oauth_auth_view"
OAUTH_CALLBACK_VIEW = "api.views.request_token_ready"


ADMINS = ( 
	( 'Ben Homnick', 'bhomnick@gmail.com' ),
 )

INTERNAL_IPS = ( '127.0.0.1', )

MANAGERS = ADMINS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'gulu.sqlite', 						 # Or path to database file if using sqlite3.
		'USER': '', 						 # Not used with sqlite3.
		'PASSWORD': '', 					 # Not used with sqlite3.
		'HOST': '', 						 # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '', 						 # Set to empty string for default. Not used with sqlite3.
	}
}

ROOTDIR = os.path.abspath(os.path.dirname(__file__)) 
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ROOTDIR + '/templates',
)

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

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join( os.path.dirname( __file__ ), "media" )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://localhost.local:8000/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 't=^um30u0%k6&unmb4+ojex=$w8ca5_x&$((&6vllbdz!6xq5p'

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
 )

MIDDLEWARE_CLASSES = ( 
	'django.middleware.common.CommonMiddleware',
	'debug_toolbar.middleware.DebugToolbarMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'globals.middleware.SlugURLMiddleware',
	'globals.middleware.Django403Middleware',
 )

APPEND_SLASH = True

ROOT_URLCONF = 'gulu.urls'

TEMPLATE_DIRS = ( 
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join( os.path.dirname( __file__ ), "templates" ),
 )

INSTALLED_APPS = ( 
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	#'django.contrib.admindocs',
	'django.contrib.comments',
	'debug_toolbar',
	'south',
	'bbcode',
	'guardian',
	'haystack',
	'whoosh',

	# Gulu modules
	'actstream',
	'blog',
	'deal',
	'dish',
	'gcomments',
	'globals',
	'invite',
	'like',
	'locations',
	'mission',
	'photos',
	'ranking',
	'recommend',
	'restaurant',
	'review',
	'search',
	#'todo',
	'user_profiles',
	'wall',
	'chef',
	'event',
	'sync',
	'piston',
	'api',
)

COMMENTS_APP = 'gcomments'

AUTHENTICATION_BACKENDS = ( 
	'user_profiles.auth_backends.UserProfileBackend',
	'guardian.backends.ObjectPermissionBackend',
	#'django.contrib.auth.backends.ModelBackend',
)
ANONYMOUS_USER_ID = -1
CUSTOM_USER_MODEL = 'user_profiles.UserProfile'
LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/logged_in"

# HAYSTACK
HAYSTACK_SITECONF = 'search_sites'
#HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = "http://127.0.0.1:8983/solr"

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = './external_apps/whoosh/index'
HAYSTACK_INCLUDE_SPELLING = True

# Import local settings
try:
	from settings_local import *
except ImportError:
	try:
		from settings_dev import *
		try:
			from mod_python import apache
			apache.log_error( "settings_local.py not set; trying settings_dev.py ", apache.APLOG_NOTICE )
		except ImportError:
			import sys
			sys.stderr.write( "settings_local.py not set; trying settings_dev.py \n" )
	except ImportError:
		try:
			from mod_python import apache
			apache.log_error( "settings_dev.py not set; using default settings", apache.APLOG_NOTICE )
		except ImportError:
			import sys
			sys.stderr.write( "settings_dev.py not set; using default settings\n" )
