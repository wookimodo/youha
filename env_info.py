from pathlib import Path

SECRET_KEY = 'django-insecure-veq0tnmipj#ws462u9q82ljk9(7ma^mias4$oe=_6k@!og-e3q'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

BASE_DIR = Path(__file__).resolve().parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}