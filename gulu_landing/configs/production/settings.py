from gulu_landing.configs.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media.gulu.com/assets/'

ADMIN_MEDIA_PREFIX = 'http://gulu.com/assets/admin_media/'

# Predefined domain
SITE_DOMAIN = 'gulu.com'


# Email
EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'do.not.reply@gulu.com'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# Facebook
FACEBOOK_APP_ID = "156315944428521"
FACEBOOK_APP_SECRET = "51096bb8e2d3821e4ffe0c059b7802de"

# Internal IPs for security
INTERNAL_IPS = ()

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)
