import braintree

from .base import *

# # SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(!))-4e!mhd3wbd(-ch_85q28d-jxf7n!luks@#@$r1fkmq*x1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
# Braintree settings
BRAINTREE_MERCHANT_ID = 'kqct9hnxg4mqtpxw'  # Merchant ID
BRAINTREE_PUBLIC_KEY = 'fbcx7gdh6t9ngsj5'  # Public Key
BRAINTREE_PRIVATE_KEY = 'f62820b763853d5b539a1be375210654'  # Private key

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
