
# Domain of EDID.tv website. Make sure to use a trailing slash.
EDID_WEBSITE_ROOT_URL = 'http://edid.tv/'

# Path to upload URL.
EDID_WEBSITE_UPLOAD_URL = 'api/upload/'


try:
    from local_settings import *
except ImportError:
    pass
