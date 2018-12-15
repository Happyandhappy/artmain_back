from .models import TenantMaster
# Create your views here.

def get_tenant(request):
    hostname = request.META['HTTP_HOST'].split(':')[0]
    return TenantMaster.objects.get(domain_url=hostname).company_name