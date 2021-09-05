import os
from os import environ

class config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname('D:\flask projects\fake_image_detector'))

    SECRET_KEY = 'shivam8825'