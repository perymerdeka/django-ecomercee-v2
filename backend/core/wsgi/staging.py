from .base import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.staging')

application = get_wsgi_application()