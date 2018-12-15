from django.contrib import admin
from .models import *
# Register your models here.
class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('userType','desc',)
    list_filter = ('userType',)
    search_fields = ('userType',)
    ordering = ('userType',)
    filter_horizontal = ()
admin.site.register(UserGroup, UserGroupAdmin)

class ProgramObjectAdmin(admin.ModelAdmin):
    list_display = ('progname','d_displayname','type','status',)
    list_filter = ('progname',)
    search_fields = ('progname',)
    ordering = ('progname',)
    filter_horizontal = ()
admin.site.register(ProgramObject, ProgramObjectAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('usertype','name','desciption','address','country','countrycode','email','contact')
    list_filter = ('usertype',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
admin.site.register(User, UserAdmin)

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','description','address','country','country_code','phone','email','contact','menu','plan',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
admin.site.register(Vendor, VendorAdmin)

class FieldConfigureAdmin(admin.ModelAdmin):
    list_display = ('tblname','group','userid','filedname','projectid','value')
    list_filter = ('userid',)
    search_fields = ('tblname',)
    ordering = ('userid',)
    filter_horizontal = ()
admin.site.register(FieldConfigure, FieldConfigureAdmin)

class FieldUIConfigureAdmin(admin.ModelAdmin):
    list_display = ('direc','progname','type','defname','changedname','desctription','fieldname','fieldtype','widget','visible','position','defvalue')
    list_filter = ('type',)
    search_fields = ('type',)
    ordering = ('type',)
    filter_horizontal = ()
admin.site.register(FieldUIConfigure, FieldUIConfigureAdmin)

class FieldValDefAdmin(admin.ModelAdmin):
    list_display = ('table','fieldname','type','value',)
    list_filter = ('fieldname',)
    search_fields = ('fieldname',)
    ordering = ('fieldname',)
    filter_horizontal = ()
admin.site.register(FieldValDef, FieldValDefAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('plancode','plandescription','tier','price','terms','usage','threshold','multiplier','effective_date','status')
    list_filter = ('plancode',)
    search_fields = ('plancode',)
    ordering = ('plancode',)
    filter_horizontal = ()
admin.site.register(Plan, PlanAdmin)

class APIMasterAdmin(admin.ModelAdmin):
    list_display = ('progname','direc','type','defname','changedname','description','scriptref','apiLink','credentials','secretkey','status')
    list_filter = ('defname',)
    search_fields = ('defname',)
    ordering = ('defname',)
    filter_horizontal = ()
admin.site.register(APIMaster, APIMasterAdmin)

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('type','tolerance','scalingfactor','match','loss',)
    list_filter = ('type',)
    search_fields = ('type',)
    ordering = ('type',)
    filter_horizontal = ()
admin.site.register(Config, ConfigAdmin)

class HconfigAdmin(admin.ModelAdmin):
    list_display = ('net','description',)
    list_filter = ('net',)
    search_fields = ('net',)
    ordering = ('net',)
    filter_horizontal = ()
admin.site.register(Hconfig, HconfigAdmin)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name','description','address','country','country_code','phone','email','contact','active')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
admin.site.register(Partner, PartnerAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','description','address','country','country_code','phone','email','contact','active','manager','team','employeeid','employeetype','status')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
admin.site.register(Employee, PartnerAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','description','address','country','country_code','phone','email','contact','active','control','plan','status')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()
admin.site.register(Customer, CustomerAdmin)

class MenuDefAdmin(admin.ModelAdmin):
    list_display = ('usergroup','progname','type','menuname','menu_sub1','menu_sub2','menu_sub3','crud','view',)
    list_filter = ('menuname',)
    search_fields = ('menuname',)
    ordering = ('menuname',)
    filter_horizontal = ()
admin.site.register(MenuDef, MenuDefAdmin)


