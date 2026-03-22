import os
from .base import *
import environ 

env = environ.Env()
# Lecture du fichier .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = False

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])


DATABASES = {
    'default': env.db('DATABASE_URL')
}
# Sécurité supplémentaire pour la prod
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECRET_KEY = env('SECRET_KEY')


# Force le HTTPS pour les cookies de session et CSRF
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Redirection automatique vers HTTPS (si votre serveur le gère)
SECURE_SSL_REDIRECT = False
