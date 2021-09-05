import os
from os import environ

class config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname('D:\flask projects\fake_image_detector'))

    SECRET_KEY = 'shivam8825'

    UPLOADS = 'D:\flask projects\fake_image_detector\static\uploads'

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

    class DevelopmentConfig(config):
        DEBUG = True
        SESSION_COOKIE_SECURE = False

    class DebugConfig(config):
        DEBUG = False