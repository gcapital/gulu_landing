from gulu.configs.common.settings import *

# Debugging
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'https://s3-ap-southeast-1.amazonaws.com/media-api2.gulu.com/static/'

# Predefined domain
MY_SITE_DOMAIN = 'api.gulu.com'

# Email
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'do.not.reply@api.gulu.com'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# S3
AWS_S3_URL = 's3://s3-ap-southeast-1.amazonaws.com/media-api2.gulu.com/'

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)
