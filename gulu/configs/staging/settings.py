from gulu.configs.common.settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://media-beta.gulu.com'

# Predefined domain
MY_SITE_DOMAIN = 'beta.gulu.com'

# Email
#EMAIL_HOST = 'mail.ec2-122-248-196-115.ap-southeast-1.compute.amazonaws.com'
#EMAIL_PORT = 25

# Caching
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'

# S3
AWS_S3_URL = 's3://s3-ap-southeast-1.amazonaws.com/media-beta.gulu.com/'

# Internal IPs for security
INTERNAL_IPS = ()

# logging
import logging.config
LOG_FILENAME = os.path.join(os.path.dirname(__file__), 'logging.conf')
logging.config.fileConfig(LOG_FILENAME)