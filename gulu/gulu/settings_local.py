# $Id: settings_local.py.example 293 2010-11-30 10:20:04Z ben $
#
# Example settings_local.py file

#DATABASES = {
#	'default': {
#		'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#		'NAME': '',						 # Or path to database file if using sqlite3.
#		'USER': '',						 # Not used with sqlite3.
#		'PASSWORD': '',					 # Not used with sqlite3.
#		'HOST': '',						 # Set to empty string for localhost. Not used with sqlite3.
#		'PORT': '',						 # Set to empty string for default. Not used with sqlite3.
#	}
#}

#MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")

MEDIA_URL = 'http://192.168.11.2:8000/media/'

DEBUG_TOOLBAR_CONFIG = {
	'INTERCEPT_REDIRECTS': False,
#	'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
#	'EXTRA_SIGNALS': ['myproject.signals.MySignal'],
#	'HIDE_DJANGO_SQL': False,
#	'TAG': 'div',
}
