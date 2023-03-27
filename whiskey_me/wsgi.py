"""
WSGI config for whiskey_me project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'whiskey_me.settings')
project_folder = '/home/whiskyme/Django-Whisky2U'
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()
