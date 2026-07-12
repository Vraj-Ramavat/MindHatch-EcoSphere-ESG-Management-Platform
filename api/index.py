import os
import sys
from pathlib import Path

# Add the backend directory to sys.path so Django can find its modules
sys.path.append(str(Path(__file__).resolve().parent.parent / 'backend'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecosphere.settings')
app = get_wsgi_application()
