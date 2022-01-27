from .base import *
import os
from .env_status import Env
# Initialise environment variables
# env = environ.Env()
# environ.Env.read_env()

Env('development')

ENV_TYPE = "Development"
SECRET_KEY = 'django-insecure-*)%=$#rpfknmyr_82nld!nm7_x6gfa6+ju*ko4_7)3+25=mawy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', ]