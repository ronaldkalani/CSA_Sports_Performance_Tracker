from pathlib import Path
import os
import dj_database_url

# ==========================
# 👐 BASE DIRECTORY
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# 🛡️ SECURITY SETTINGS
# ==========================
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-12ust*hb&k2$e9e(@xr@^bz(7p99(yv%b27qv#$gtkss#=agzu')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# ==========================
# 🔧 APPLICATION DEFINITION
# ==========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'core_api',  # Custom API app
]

# ==========================
# 🛠️ MIDDLEWARE
# ==========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Efficient static file serving
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==========================
# 🌐 CORS SETTINGS
# ==========================
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://192.168.122.17:3000",
]
CORS_ALLOW_CREDENTIALS = True

# ==========================
# ⚠️ CSRF SETTINGS
# ==========================
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://192.168.122.17:3000",
]

# ==========================
# 🔗 URL CONFIGURATION
# ==========================
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "frontend", "build"),
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

WSGI_APPLICATION = 'backend.wsgi.application'
ASGI_APPLICATION = 'backend.asgi.application'

# ==========================
# 📂 DATABASE CONFIGURATION
# ==========================
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'ROne3132@')
DB_NAME = os.getenv('DB_NAME', 'CSA_Sports_Performance_Tracker')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
        conn_max_age=600,
        ssl_require=False
    )
}

# ==========================
# 🛠️ PASSWORD VALIDATION
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==========================
# 🔄 INTERNATIONALIZATION
# ==========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ==========================
# 📁 STATIC FILES CONFIGURATION
# ==========================
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Directory for production static files

# Corrected STATICFILES_DIRS path
STATICFILES_DIRS = [
    BASE_DIR / "frontend" / "build" / "static",
]

# Whitenoise storage for efficient static file handling
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==========================
# 🛠️ DEFAULT PRIMARY KEY FIELD TYPE
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================
# 🔗 RENDER HOSTNAME SETTINGS
# ==========================
RENDER_EXTERNAL_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# ==========================
# 🔍 LOGGING CONFIGURATION
# ==========================
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}