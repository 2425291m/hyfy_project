"""
Django settings for hyfy_project project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

STATIC_DIR = os.path.join(BASE_DIR, 'static')
# page 46
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [STATIC_DIR, ]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#jr+kkgs96o#3ht*^g47+dsrev!byrbs%6lz-q!n-2r05ztn@*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hyfy',
    'social_django',
]

SOCIAL_AUTH_URL_NAMESPACE = 'social'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hyfy_project.urls'




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # page 48
                'django.template.context_processors.media'
            ],
        },
    },
]

# WSGI_APPLICATION = 'hyfy_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 6, }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_URL = '/hyfy/login/'

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

 # page 46
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login/'

# If True, users can register
# REGISTRATION_OPEN = True
# One-week activation window; you may, of course, use a different value.
# ACCOUNT_ACTIVATION_DAYS = 7
# If True, the user will be automatically logged in.
# REGISTRATION_AUTO_LOGIN = True
# The page you want users to arrive at after they successfully log in
# LOGIN_REDIRECT_URL = '/rango/'
# The page users are directed to if they are not logged in,
# and are trying to access pages requiring authentication
# LOGIN_URL = '/accounts/login/'

SOCIAL_AUTH_SPOTIFY_KEY = '294156b84c3a4659838991a3ebec94e2'
SOCIAL_AUTH_SPOTIFY_SECRET = 'a536e1e7b77c49d5abaa6e39764c4cf9'
SOCIAL_AUTH_SPOTIFY_SCOPE = ['user-read-email', 'user-library-read']
LOGIN_REDIRECT_URL = '/releases'

AUTHENTICATION_BACKENDS = (
    ('django.contrib.auth.backends.ModelBackend'),
)
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.spotify.SpotifyOAuth2',
# )