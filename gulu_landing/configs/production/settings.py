from gulu.configs.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://demo-media.gulu.com/assets/'

ADMIN_MEDIA_PREFIX = 'http://demo-media.gulu.com/assets/admin_media/'

# Predefined domain
SITE_DOMAIN = 'gulu.com'
SITE_ID = '4d63289052399e19b700001c'

# Email
EMAIL_BACKEND = 'django_ses.SESBackend'
EMAIL_HOST = 'localhost'
SERVER_EMAIL = 'do.not.reply@gulu.com'

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

### HAYSTACK
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = "http://127.0.0.1:8000/solr"
# These settings will bump up the CPU reqs of solr
HAYSTACK_BATCH_SIZE = 200
HAYSTACK_SOLR_TIMEOUT = 60

# Storage
#DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
AWS_STORAGE_BUCKET_NAME = "media-beta.gulu.com"
AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
AWS_S3_FILE_OVERWRITE = False

# Facebook
FACEBOOK_APP_ID = "156315944428521"
FACEBOOK_APP_SECRET = "51096bb8e2d3821e4ffe0c059b7802de"

# Internal IPs for security
INTERNAL_IPS = ()

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)
