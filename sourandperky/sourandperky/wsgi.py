"""
WSGI config for sourandperky project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sourandperky.settings')

WhiteNoise.autorefresh = settings.WHITENOISE_AUTOREFRESH

application = WhiteNoise(
    application=get_wsgi_application(),
    root=settings.MEDIA_ROOT,
    prefix=settings.MEDIA_URL
)
