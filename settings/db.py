from os import getenv


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': getenv('POSTGRES_NAME', ''),
        'USER': getenv('POSTGRES_USER', ''),
        'PASSWORD': getenv('POSTGRES_PASSWORD', ''),
        'HOST': getenv('POSTGRES_HOST', ''),
        'PORT': getenv('POSTGRES_PORT', ''),
    },
}
