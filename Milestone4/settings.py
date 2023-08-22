"""
Django settings for Milestone4 project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8000-jonasitoelpr-milestone4-xe9m2o65j4l.ws-eu104.gitpod.io', 'language-stay-2.herokuapp.com']
CSRF_TRUSTED_ORIGINS = ['https://8000-jonasitoelpr-milestone4-xe9m2o65j4l.ws-eu104.gitpod.io']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'django_countries',
    'hostofferings',
    'users',
    'products',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Milestone4.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Milestone4.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse('postgres://xcexqnpjyhqwll:adcd4f53dc9043049f89e5d0e691bb97bf4d9ddb5dbed2e3d27b004b2236d09c@ec2-54-228-97-176.eu-west-1.compute.amazonaws.com:5432/d40jn6psvhhf0h')
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



#This will only run if USE_AWS is included in the environment variables


value = os.environ.get('USE_AWS')
if value:
    # Cache control	
    AWS_S3_OBJECT_PARAMETERS = {	
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',	
        'CacheControl': 'max-age=94608000',	
    }	

    AWS_STORAGE_BUCKET_NAME = 'language-stay'
    AWS_S3_REGION_NAME = 'eu-west-2'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    STATICFILES_LOCATION = 'static'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

    LOGIN_URL = 'login'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUBLIC_KEY = "pk_test_51KOfJ0CS31G6KZO7biEXnTyyKT4G4wDg129iGCnr2LN4FbOXDgDe4i6mDu9LP2GjH7VOYv0o0rurKidobSWOE3k600PhNWTujf"
STRIPE_SECRET_KEY = "sk_test_51KOfJ0CS31G6KZO7To5bVMrFMhQVaJ0yLi3JaDo5gAgg1h8jsyemik1OUKR08793jT3vD5eUlt6vOU6kNViZWIgR00cuzpa7gC"
STRIPE_WEBHOOK_SECRET = "whsec_DAvoFYeUPH78YBhhJeHLDwhwLAtkSdbz"


DATABASE_URL = 'postgres://xcexqnpjyhqwll:adcd4f53dc9043049f89e5d0e691bb97bf4d9ddb5dbed2e3d27b004b2236d09c@ec2-54-228-97-176.eu-west-1.compute.amazonaws.com:5432/d40jn6psvhhf0h'