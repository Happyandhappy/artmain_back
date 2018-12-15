from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from tenant_schemas.models import TenantMixin

class TenantMaster(TenantMixin):
    class Meta:
        verbose_name = _("Tenants")
        verbose_name_plural = _("Tenants")

    company_name = models.CharField(max_length=100, null=False, blank=False)
    company_description = models.TextField(default="")
    company_address = models.CharField(max_length=200, null=True, blank=True)
    company_city = models.CharField(max_length=200, null=True, blank=True)
    contry_code = models.CharField(max_length=200, null=True, blank=True)
    company_phone = models.CharField(max_length=200, null=True, blank=True)
    company_email = models.EmailField(blank=True, null=True,)
    company_contact = models.CharField(max_length=200, default="", null=True, blank=True)
    company_active = models.BooleanField(default=False)
    control = models.CharField(max_length=100, default="")
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True

    def __unicode__(self):
        return self.company_name

    def __str__(self):
        return self.company_name

