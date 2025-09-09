"""
Django settings for proyecto1 project.

Adaptado para despliegue en Render con:
- dj-database-url para DB (SQLite por defecto, Postgres si agregás DATABASE_URL)
- WhiteNoise para servir archivos estáticos
- Config de seguridad básica para proxy/HTTPS
"""

from pathlib import Path
import os
import dj_database_url  # Render usa DATABASE_URL para Postgres

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------
# Seguridad
# ---------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "blog1234")  # definirlo en Render
DEBUG = os.getenv("DEBUG", "True") == "True"  # DEBUG=False en producción

ALLOWED_HOSTS = [
    "*",  # se puede restringir a tu-app.onrender.com
]

# Necesario en Django 4+ para evitar 403 en POST
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

# ---------------------------
# Apps
# ---------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps de proyecto
    "blog",
    "Main",
]

# ---------------------------
# Middleware
# ---------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise para servir estáticos
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "proyecto1.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "proyecto1.wsgi.application"

# ---------------------------
# Base de datos
# ---------------------------
# Por defecto usa SQLite.
# Si se configura DATABASE_URL en Render, se conecta automáticamente a Postgres.
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# ---------------------------
# Validación de contraseñas
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------
# Internacionalización
# ---------------------------
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# ---------------------------
# Archivos estáticos
# ---------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"  # collectstatic junta todo acá

# WhiteNoise: mejora de performance para prod
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# (Opcional) Media si después se usan imágenes de usuarios
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------
# HTTPS detrás de proxy (Render)
# ---------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Seguridad extra si DEBUG=False
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # Podés activar HSTS si tu dominio va a estar siempre en HTTPS:
    # SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30  # 30 días
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_PRELOAD = True

# ---------------------------
# Default primary key
# ---------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

