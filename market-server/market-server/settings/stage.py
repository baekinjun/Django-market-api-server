from wooahmarket.settings.common import *
import json
import yaml

DEBUG = True
SETTINGS_LEVEL = 'stage'

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ('http://10.100.101.102:3000', 'http://localhost:3000', 'http://10.100.101.148:3000')