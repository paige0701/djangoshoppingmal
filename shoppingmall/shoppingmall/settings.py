"""
Django settings for shoppingmall project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_*$@o(sl!ksmdwpki_3$4p2fnhvzn=11$@lu+8+@sdc+k^yq5j'

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
    'shopping_app',

    # Django sites framework is required
    'django.contrib.sites',
    #     'allauth',
    #     'allauth.account',
    #     'allauth.socialaccount',

    # 'social.apps.django_app.default',
    'social_django',

    # 댓글 기능 추가
    # 'disqus',
    'billing',



]

# DISQUS_API_KEY = 'DndT7Q6MXyf3Mtf8Hv1CcnMCrHSZhNpGYwdKEIZutpFvgimqwSGxWLTnq4kAoZ0V'
# DISQUS_WEBSITE_SHORTNAME = 'http-127-0-0-1-8000-4'

# Ensure the SITE_ID is defined
SITE_ID = 2

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'shoppingmall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',


                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

                # 'social.apps.django_app.context_processors.backends',
                # 'social.apps.django_app.context_processors.login_redirect',


            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'OPTIONS': {
            'environment': 'shopping_app.jinja2.environment',
        }
    },
]

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


WSGI_APPLICATION = 'shoppingmall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'shopping_app.User'

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static','media')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOGIN_URL = 'login'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = '/'



# 이메일 confirmation 이용할 때 사용
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # Django SMTP (EMAIL)
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'paigechoi0701@gmail.com'
EMAIL_HOST_PASSWORD = 'redhater07'
EMAIL_PORT = 587


# EMAIL_HOST = 'smtp.worksmobile.com'
# # EMAIL_PORT = 25  # Default설정
# EMAIL_HOST_USER = 'kamper@kamper.co.kr'
# EMAIL_HOST_PASSWORD = 'us621011'
# EMAIL_PORT = 465
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_SSL = True


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin and to ensure compatibility with other packages
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods
    # 'allauth.account.auth_backends.AuthenticationBackend',
    # 'social.backends.facebook.FacebookOAuth2',
    # 'social.*',
    # 'social_core.backends.github.GithubOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.open_id.OpenIdAuth',


    # 'social.backends.facebook.FacebookOAuth2',


)


# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
# SOCIAL_AUTH_URL_NAMESPACE = 'social'


# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1441816456116895'
SOCIAL_AUTH_FACEBOOK_SECRET = '6da79d177ac445d25cb36a749390a4d5'

# SOCIAL_AUTH_PIPELINE = ( 'social.pipeline.social_auth.social_details',
#                          'social.pipeline.social_auth.social_uid',
#                          'social.pipeline.social_auth.auth_allowed',
#                          'social.pipeline.social_auth.social_user',
#                          'social.pipeline.user.get_username',
#                          'social.pipeline.user.create_user',
#                          'social.pipeline.social_auth.associate_user',
#                          'social.pipeline.social_auth.load_extra_data',
#                          'social.pipeline.user.user_details')

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCAIL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name'
}

SESSION_EXPIRE_AT_BROWSER_CLOSE=False
SESSION_COOKIE_AGE = 60*60



# 결제
IAMPORT_KEY=8554980182107506
IAMPORT_SECRET='tA3Vs4fkFPMEESPt4VvRtyt6JAQtzWc3xgY0kek037EHZtb4pGWSfqZY0PsAMEDkVCkgQFgUMUCMoNRO'