import os
import sys
from pathlib import Path

# When deployed on Vercel, the repo root is at /var/task
# The backend Django apps are at /var/task/backend
repo_root = Path(__file__).resolve().parent.parent
backend_dir = repo_root / 'backend'

sys.path.insert(0, str(backend_dir))
sys.path.insert(0, str(repo_root))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecosphere.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application()
