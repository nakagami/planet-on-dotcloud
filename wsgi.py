import os
import sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'planetplanet.settings'
sys.path.insert(0, '/home/dotcloud/current/planetplanet')
import django.core.handlers.wsgi
djangoapplication = django.core.handlers.wsgi.WSGIHandler()
def application(environ, start_response):
    if 'SCRIPT_NAME' in environ:
        del environ['SCRIPT_NAME']
    return djangoapplication(environ, start_response)
