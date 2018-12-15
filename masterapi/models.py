from django.db import models
from tenants.models import TenantMaster
from django.utils.translation import gettext as _
# Create your models here.

# Timestamp model
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class UserGroup(TimeStampModel):
    class Meta:
        verbose_name = _("User Group")
        verbose_name_plural = _("User Group")

    userType = models.CharField(max_length=100, null=False)
    desc = models.TextField()
    def __str__(self):
        return self.userType

# F000015 Plan
class Plan(TimeStampModel):
    class Meta:
        verbose_name = _("Plan")
        verbose_name_plural = _("Plan")
    plancode = models.CharField(max_length=100)
    plandescription = models.TextField()
    tier = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    terms = models.CharField(max_length=50, blank=True)
    usage = models.BooleanField(default=False)
    threshold = models.IntegerField(blank=True, null=True)
    multiplier = models.FloatField(blank=True, null=True,)
    effective_date = models.DateField(auto_now=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.plancode

# Program Object Definition
class ProgramObject(models.Model):
    class Meta:
        verbose_name = _("Program Object Definition")
        verbose_name_plural = _("Program Object Definition")

    progname = models.CharField(max_length=150)
    d_displayname = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.progname


# F000011 APIMaster
class APIMaster(TimeStampModel):
    class Meta:
        verbose_name = _("API Master")
        verbose_name_plural =_("API Master")

    # tenantid = models.ForeignKey(TenantMaster, on_delete = models.CASCADE)
    progname = models.ForeignKey(ProgramObject, on_delete = models.CASCADE)
    direc = models.CharField(max_length=50, )
    type = models.CharField(max_length=50, )
    defname = models.CharField(max_length=50,)
    changedname = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    scriptref = models.CharField(max_length=150, null=True)
    apiLink = models.CharField(max_length=200, null=True)
    credentials = models.CharField(max_length=200,)
    secretkey = models.CharField(max_length=200,)
    status = models.BooleanField(default=False)
    json = models.TextField(default="{}")

#F000091 User
class User(TimeStampModel):
    class Meta:
        verbose_name = _("User in Tenant")
        verbose_name_plural = _("User in Tenant")

    # tenantid = models.ForeignKey(TenantMaster,related_name="user_tenant_id", on_delete=models.CASCADE)
    usertype = models.ForeignKey(ProgramObject, on_delete=models.CASCADE)
    userid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    desciption = models.TextField()
    address = models.CharField(max_length=200,)
    country = models.CharField(max_length=50,)
    countrycode = models.CharField(max_length=50,)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=False)

#F00001T Field Configurations
class FieldConfigure(TimeStampModel):
    class Meta:
        verbose_name = _("Field Configurations")
        verbose_name_plural = _("Field Configurations")

    # tanentid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    tblname = models.CharField(max_length=100)
    group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, models.SET_NULL, null=True,blank=True,)
    filedname = models.CharField(max_length=200)
    projectid = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200)


#F000012 Field UI Configurations
class FieldUIConfigure(TimeStampModel):
    class Meta:
        verbose_name = _("Field UI Configurations")
        verbose_name_plural = _("Field UI Configurations")

    # tanentid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    direc = models.CharField(max_length=50, )
    progname = models.ForeignKey(ProgramObject, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, )
    defname = models.CharField(max_length=50,)
    changedname = models.CharField(max_length=50,)
    desctription = models.TextField()
    fieldname = models.CharField(max_length=200,)
    fieldtype = models.CharField(max_length=50,)
    widget = models.CharField(max_length=100,)
    visible = models.BooleanField(default=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    calculation = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=50,)
    defvalue = models.CharField(max_length=100,)


#F0000Z	Field Values Definations
class FieldValDef(TimeStampModel):
    class Meta:
        verbose_name = _("Field Values Definations")
        verbose_name_plural = _("Field Values Definations")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    table    = models.CharField(max_length=100)
    fieldname  = models.CharField(max_length=100)
    type     = models.CharField(max_length=100, default='json')
    value    = models.TextField(default="{}")

#F00005	Config
class Config(TimeStampModel):
    class Meta:
        verbose_name = _("Config")
        verbose_name_plural = _("Config")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE,)
    type = models.CharField(max_length=50)
    tolerance = models.FloatField(null=True)
    scalingfactor = models.FloatField(null=True)
    match = models.FloatField(null=True)
    loss = models.FloatField(null=True)

#F000051 Hconfig
class Hconfig(TimeStampModel):
    class Meta:
        verbose_name = _("HConfig")
        verbose_name_plural = _("HConfig")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    net = models.CharField(max_length=100, )
    description = models.CharField(max_length=100,)


#F000081 Menu Definition
class MenuDef(TimeStampModel):
    class Meta:
        verbose_name = _("Menu Definition")
        verbose_name_plural = _("Menu Definition")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    usergroup = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    progname = models.ForeignKey(ProgramObject, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, )
    menuname = models.CharField(max_length=100, blank=True)
    menu_sub1 = models.CharField(max_length=100, blank=True)
    menu_sub2 = models.CharField(max_length=100, blank=True)
    menu_sub3 = models.CharField(max_length=100, blank=True)
    crud = models.CharField(max_length=50, blank=True, null=True)
    view = models.NullBooleanField(default=None)

#F00003	Customer
class Customer(TimeStampModel):
    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customer")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100, )
    country = models.CharField(max_length=100, )
    country_code = models.CharField(max_length=50,)
    phone = models.CharField(max_length=50,)
    email = models.CharField(max_length=100,)
    contact = models.CharField(max_length=250,)
    active = models.BooleanField(default=True)
    control = models.CharField(max_length=100,)
    menu = models.CharField(max_length=100, blank=True)
    db = models.CharField(max_length=100, blank=True)
    server = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

#F000031 Partner
class Partner(TimeStampModel):
    class Meta:
        verbose_name = _("Partner")
        verbose_name_plural = _("Partner")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100,)
    country = models.CharField(max_length=100,)
    country_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    control = models.CharField(max_length=100, null=True, blank=True)
    menu = models.CharField(max_length=100, blank=True)
    db = models.CharField(max_length=100, blank=True)
    server = models.CharField(max_length=250, blank=True)
    version = models.CharField(max_length=100, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


#F000032 Vendor
class Vendor(TimeStampModel):
    class Meta:
        verbose_name = _("Vendor")
        verbose_name_plural = _("Vendor")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=250, blank=True)
    active = models.BooleanField(default=False)
    control = models.CharField(max_length=100, null=True, blank=True)
    menu = models.CharField(max_length=100, blank=True)
    db = models.CharField(max_length=100, blank=True)
    server = models.CharField(max_length=250, blank=True)
    version = models.CharField(max_length=100, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


#F000034 Employee
class Employee(TimeStampModel):
    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employee")

    # tenantid = models.ForeignKey(TenantMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    bu = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=100)
    employeetype = models.CharField(max_length=100)
    status = models.BooleanField(default=False)



