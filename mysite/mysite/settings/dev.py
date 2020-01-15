from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'q5i*1y15y#u#s@4+zv-p7p=9@zgp2di0+2jbn9=-10=^7q2nh#'
SECRET_KEY = '5d8c7c90fd156917c2370984c89ba78594dcf340'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
