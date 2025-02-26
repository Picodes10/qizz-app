# WSGI configuration for Quizz App

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'quizz_app' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizz_app.settings')

# Get the WSGI application for the project.
application = get_wsgi_application()
