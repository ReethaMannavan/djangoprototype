# trading_app/context_processors.py
from .models import SiteConfig

def site_config(request):
    return {'site_config': SiteConfig.objects.first()}
