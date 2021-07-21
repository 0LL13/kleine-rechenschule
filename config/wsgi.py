"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # noqa

# this throws error ModuleNotFound:
# from django.core.wsgi import get_wsgi_application  # noqa
# application = get_wsgi_application()

import django.core.handlers.wsgi  # noqa
application = django.core.handlers.wsgi.WSGIHandler()


from whitenoise import WhiteNoise  # noqa
application = WhiteNoise(application)
# application.add_files('STATICFILES_DIRS', prefix='more-files/')
