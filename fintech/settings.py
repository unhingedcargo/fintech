from pathlib import Path
# import cloudinary
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, parse_qsl

load_dotenv()

tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)%^8ktft3bqp$dly%4c14fx=eje+%l9)id&3j$!&8%arj-u=28'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["*"]

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.168.0.0:3000",
    "https://fintech-frontend-mpvt.onrender.com",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django_extensions',
    'corsheaders',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fintech.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fintech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# postgresql://unhingedcargo_fintech:2PU0pNRqa1c6MFDHHJUEM88kzHgVvUpA@dpg-d32mnpgdl3ps73886uf0-a/fintech_db_tigq
# postgresql://uhjcqi16yu6nig9w9reg:rSQRon5j91Svo9ACMM6PywefWGKHsy@be96qdzvd9ngp2e72tjc-postgresql.services.clever-cloud.com:50013/be96qdzvd9ngp2e72tjc

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': tmpPostgres.path.replace('/', ''),
        'USER': tmpPostgres.username,
        'PASSWORD': tmpPostgres.password,
        'HOST': tmpPostgres.hostname,
        'PORT': 5432,
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'postgres',
    #     'USER' : 'postgres.vdzmwbjuanrtqrutnlgd',
    #     'HOST' : 'aws-1-ap-south-1.pooler.supabase.com',
    #     'PASSWORD' : 'Printplus@790',
    #     'PORT' : 6543,
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'be96qdzvd9ngp2e72tjc',
    #     'USER' : 'uhjcqi16yu6nig9w9reg',
    #     'HOST' : 'be96qdzvd9ngp2e72tjc-postgresql.services.clever-cloud.com',
    #     'PASSWORD' : 'rSQRon5j91Svo9ACMM6PywefWGKHsy',
    #     'PORT' : 50013,
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'birkmpn6thyy9rkcsn4r',
    #     'USER' : 'uqadswlozvcuquj2ktdu',
    #     'HOST' : 'birkmpn6thyy9rkcsn4r-postgresql.services.clever-cloud.com',
    #     'PASSWORD' : 'w4RgX3VUE5eCzrXrIFLgKCJxb2bcKH',
    #     'PORT' : 50013,
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'bnadkuwamr7blr2jsi4b',
    #     'USER' : 'uyqvvdl5z2icnhht',
    #     'HOST' : 'bnadkuwamr7blr2jsi4b-mysql.services.clever-cloud.com',
    #     'PASSWORD' : 'xGeqOWbPhHFyFrO7PqAK',
    #     'PORT' : 3306,
    # }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'fastapi',
    #     'USER' : 'root',
    #     'HOST' : 'localhost',
    #     'PASSWORD' : 'whitesatin',
    #     'PORT' : 3306,
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# cloudinary.config(
#     cloud_name = "diqwjvuaz",  
#     api_key = "117632985185942",  
#     api_secret = "emDmcAD26cs5CsWZ5WdGYCmTWbE" 
# )



