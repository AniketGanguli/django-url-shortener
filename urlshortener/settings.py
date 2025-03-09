import os
from pathlib import Path

# 🔹 BASE DIRECTORY
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔹 SECURITY WARNING: Keep the secret key secret!
SECRET_KEY = "your-secret-key-here"

# 🔹 SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []  # Add your domain/IP in production

# 🔹 INSTALLED APPLICATIONS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shortener",  # ✅ Your app
]

# 🔹 MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    #"django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 🔹 ROOT URL CONFIGURATION
ROOT_URLCONF = "urlshortener.urls"  # ✅ Update with your project name

# 🔹 TEMPLATES CONFIGURATION
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # ✅ Ensures templates are correctly loaded
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 🔹 WSGI CONFIGURATION
WSGI_APPLICATION = "urlshortener.wsgi.application"

# 🔹 DATABASE CONFIGURATION (SQLite for Development)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔹 PASSWORD VALIDATION
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 🔹 INTERNATIONALIZATION
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 🔹 STATIC FILES (CSS, JavaScript, Images)
STATIC_URL = "/static/"

# ✅ Fix for Static Files Issue
STATICFILES_DIRS = [
    BASE_DIR / "static",  # ✅ Change to global static folder
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# 🔹 MEDIA FILES (User Uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# 🔹 LOGIN & LOGOUT REDIRECTS
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# 🔹 DEBUGGING EMAIL BACKEND (Use SMTP in production)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
