"""
WSGI config for dinh_did_it project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

https://www.youtube.com/watch?v=u0oEIqQV_-E
https://www.youtube.com/watch?v=_TBw7ALJp0Y
https://www.youtube.com/watch?v=PCjeBQ2636Y
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dinh_did_it.settings')

application = get_wsgi_application()
