"""
WSGI config for djangotest2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys

path = os.path.abspath(os.path.join(__file__, '..', '..'))

if path not in sys.path:
    sys.path.append(path)
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangotest2.settings')

application = get_wsgi_application()
