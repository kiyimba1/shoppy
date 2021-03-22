import braintree

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Edwin K', 'edwineddie54@gmail.com')
)

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shoppy',
        'USER': 'shoppy',
        'PASSWORD': os.environ('DB_PASSWORD')
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'mail')
# Braintree settings
BRAINTREE_MERCHANT_ID = os.environ('BRAINTREE_MARCHANT_ID')  # Merchant ID
BRAINTREE_PUBLIC_KEY = os.environ('BRAINTREE_PUBLIC_KEY')  # Public Key
BRAINTREE_PRIVATE_KEY = os.environ('BRAINTREE_PRIVATE_KEY')  # Private key

BRAINTREE_CONF = braintree.Configuration(
    braintree.Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

REDIS_HOST = os.environ('REDIS_HOST')
REDIS_PORT = os.environ('REDIS_PORT')
REDIS_DB = os.environ('REDIS_DB')
