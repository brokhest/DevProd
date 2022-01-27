from .base import *
from .env_status import Env

# Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()
#
# environ.setdefault('My_server_version', 'Production')
Env('Production')
ENV_TYPE = "production"

SECRET_KEY = 'django-insecure-*)%=$#rpfknmyr_82nld!nm7_x6gfa6+ju*ko4_7)3+25=mawy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', ]