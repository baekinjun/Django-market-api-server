from wooahmarket.settings.common import *
import json
import yaml

DEBUG = True
SETTINGS_LEVEL = 'develop'

ALLOWED_HOSTS = ['*']
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = ('http://10.100.101.102:3000', 'http://localhost:3000', 'http://10.100.101.148:3000')

with open(PROJECT_DIR + '/environments/environments.yml', 'r') as f:
    yml_settings = yaml.load(f)
    environments = yml_settings['dev']
    print(f'{yml_settings["version"]} Settings Loaded')

common_settings = environments['common']
database_settings = environments['database']
aws_settings = environments['aws']
static_settings = environments['static']
if database_settings['engine'] == 'mysql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': database_settings['name'],
            'USER': database_settings['user'],
            'PASSWORD': database_settings['password'],
            'HOST': database_settings['host'],
            'PORT': database_settings['port'],
            'OPTIONS': {
                'charset': database_settings['charset'],
                'use_unicode': database_settings['use_unicode']
            }
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': database_settings['name'],
        }
    }

API_URL = common_settings['api_url']

AWS_REGION = aws_settings['aws_region']
AWS_QUERYSTRING_AUTH = aws_settings['aws_querystring_auth']
AWS_ACCESS_KEY_ID = aws_settings['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = aws_settings['aws_secret_access_key']

STATICFILES_STORAGE = aws_settings['staticfiles_storage']
DEFAULT_FILE_STORAGE = aws_settings['default_file_storage']
AWS_S3_HOST = aws_settings['aws_s3_host']

AWS_STORAGE_BUCKET_NAME = aws_settings['aws_storage_bucket_name']
AWS_S3_CUSTOM_DOMAIN = aws_settings['aws_s3_custom_domain']
AWS_S3_SECURE_URLS = aws_settings['aws_s3_secure_urls']

S3_URL = aws_settings['s3_url']

STATIC_URL = S3_URL
MEDIA_BASE_URL = static_settings['media_base_url']
MEDIA_ORIGIN_URL = static_settings['media_origin_url']
CRONTAB_DJANGO_SETTINGS_MODULE = common_settings[
    'crontab_django_settings_module']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'request': {
            'format': '[%(levelname)s] %(asctime)s %(pathname)s:%(lineno)s %(funcName)s() - %(message)s'
        },
        'location': {
            'format': '[%(levelname)s] %(asctime)s - %(message)s\n\t이용일시/ 대상/ 취득경로/ 제공 서비스/ 제공 받는자\n개인위치정보의 제3자 제공은 없는 서비스'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'request'
        },
        'log': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': f'{PROJECT_DIR}/log/wooah_debug_debug.log',
            'formatter': 'request'
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{PROJECT_DIR}/log/wooah_info_info.log',
            'formatter': 'request'
        },
        'location': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{PROJECT_DIR}/log/wooah_location_info.log',
            'formatter': 'location'
        },
        'logstash': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{PROJECT_DIR}/log/mamam_logstash_info.log',
        }
    },
    'loggers': {
        'api': {
            'handlers': ['log', 'info'],
            'level': 'DEBUG'
        },
        'web': {
            'handlers': ['log'],
            'level': 'DEBUG'
        },
        'location': {
            'handlers': ['location'],
            'level': 'DEBUG',
            'propagate': False
        },
        'log_manager': {
            'handlers': ['logstash'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}

