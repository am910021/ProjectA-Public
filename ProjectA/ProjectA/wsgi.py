"""
WSGI config for ProjectA project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .settings import DEBUG

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProjectA.settings")

if DEBUG==True:
    application = get_wsgi_application()
else: # Running on Heroku
    from dj_static import Cling
    application = Cling(get_wsgi_application())
