from django.contrib import admin
from .models import TenantMaster
# Register your models here.


class TenantAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_description','company_address','company_city', 'contry_code','company_phone','company_email','company_contact')
    list_filter = ('company_name',)
    search_fields = ('company_name',)
    ordering = ('company_name',)
    filter_horizontal = ()
admin.site.register(TenantMaster, TenantAdmin)
