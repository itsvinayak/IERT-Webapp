"""
Django settings for iert project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '775_^4c@7hj=4l!ru(g$j1!u9n^!3evi=_n0-&s9(pibcdg@f='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # local apps
    'iert_news.apps.IertNewsConfig',
    'extra_links.apps.ExtraLinksConfig',
    'user.apps.UserConfig',
    'aside.apps.AsideConfig',
    'home.apps.HomeConfig',
    #################
    # third party app
    # 'jet.dashboard',
    # 'jet',
    'crispy_forms',
    'social_django',
    'pwa',

    ###to be add####
    #'pagedown', not Build yet
    #'markdown_extras',

    ######tool bar####

    'debug_toolbar',

    ################
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

AUTHENTICATION_BACKENDS = [

    ##############google and github##########
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    #########################################
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    ###first one is for  "DEBUGGER TOOLBAR" #####
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'iert.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

WSGI_APPLICATION = 'iert.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
################set database to sql######################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'iert',
        'USER': 'root',
        'HOST': 'localhost',
        'PASSWORD': 'vinayak',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode':'traditional',
        },
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
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
FILE_UPLOAD_PERMISSIONS = 0o644

ADMIN_MEDIA_PREFIX = '/static/admin/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'


LOGIN_REDIRECT_URL = "index"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
####################collage email id ##############
EMAIL_HOST_USER = "itssvinayak@gmail.com"
EMAIL_HOST_PASSWORD = ""
##################################################


#########################pwa settings###############
#PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'home/static/', 'serviceworker.js')
# own serviceworker


PWA_APP_NAME = 'IERT'
PWA_APP_DESCRIPTION = "Institute of Engineering & Technology website made by vinayak"
PWA_APP_THEME_COLOR = 'black'
PWA_APP_BACKGROUND_COLOR = 'white'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_ICONS = [
    {
        'src': '/static/home/img/iert_icon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': '/static/home/img/iert_icon.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'home/static/', 'serviceworker.js')

PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

###############################################################################################


############################# DEBUGGER TOOLBAR (only for testbranch)###################################

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS':False,
    "SHOW_TOOLBAR_CALLBACK" : show_toolbar,
     # Toolbar options
    'RESULTS_CACHE_SIZE': 3,
    'SHOW_COLLAPSED': True,
    # Panel options
    'SQL_WARNING_THRESHOLD': 100,   # milliseconds

}
