"""
WSGI config for monivet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os,sys

sys.path.append('/home/pi/monitev/')

#referencia (en python) desde el path anterior al fichero settings.py
#Importante hacerlo asi, si hay varias instancias coriendo (en lugar de setdefault)
os.environ['DJANGO_SETTINGS_MODULE'] = "monitev.settings"
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proyectodjango.settings")

#prevenimos UnicodeEncodeError
os.environ.setdefault("LANG", "es_CO.UTF-8")
os.environ.setdefault("LC_ALL", "es_CO.UTF-8")

#activamos nuestro virtualenv
#activate_this = '/home/pi/monitev/env/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

#obtenemos la aplicacion
#from django.core.wsgi import get_wsgi_application
#path a donde esta el manage.py de nuestro proyecto Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "monivet.settings")
#application = get_wsgi_application()
