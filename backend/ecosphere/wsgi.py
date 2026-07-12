"""WSGI config for ecosphere project."""
import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Add the backend directory to sys.path so Vercel can find the Django apps
sys.path.append(str(Path(__file__).resolve().parent.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecosphere.settings')
application = get_wsgi_application()
app = application
