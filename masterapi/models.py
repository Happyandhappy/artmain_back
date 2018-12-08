from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Timestamp model
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        abstract = True


# F000015 Plan
class F000015(TimeStampModel):
    plancode = models.CharField(max_length=100)
    plandescription = models.TextField()
    tier = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    terms = models.CharField(max_length=50, blank=True)
    usage = models.BooleanField(default=False)
    threshold = models.IntegerField(max_length=20,blank=True, null=True)
    multiplier = models.FloatField(blank=True, null=True,)
    effective_date = models.DateField(auto_now=False)
    status = models.BooleanField(default=False)

# F00001 Tenant
class F00001(TimeStampModel):
    tenantid = models.CharField(max_length=100, primary_key=True)
    name     = models.CharField(max_length=200)
    description     = models.TextField()
    address  = models.CharField(max_length=200)
    country  = models.CharField(max_length=100)
    tryCode  = models.CharField(max_length=50)
    phone    = models.CharField(max_length=50)
    email    = models.CharField(max_length=50)
    contact  = models.CharField(max_length=50)
    active   = models.BooleanField(default=False)
    control  = models.CharField(max_length=50)
    menu     = models.CharField(max_length=50, blank=True)
    DB       = models.CharField(max_length=50, blank=True)
    server   = models.CharField(max_length=50, blank=True)
    version  = models.CharField(max_length=50, blank=True)
    plan     = models.ForeignKey(F000015, on_delete=models.CASCADE)
    status   = models.BooleanField(default=False)

    def __str__(self):
        return self.tenantid

# Program Object Definition
class F00008(models.Model):
    progname = models.CharField(primary_key=True, max_length=150)
    d_displayname = models.CharField(max_length=150)
    type = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.progname


# F000011 APIMaster
class F000011(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete = models.CASCADE)
    progname = models.ForeignKey(F00008, on_delete = models.CASCADE)
    direc = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    defname = models.CharField(max_length=50)
    changedname = models.CharField(max_length=150, blank=True)
    description = models.TextField()
    scriptref = models.CharField(max_length=150)
    apiLink = models.CharField(max_length=200)
    credentials = models.CharField(max_length=200)
    secretkey = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    json = models.TextField()

#F00009	UserGroup
class F00009(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.usertype

#F000091 User
class F000091(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    usertype = models.ForeignKey(F00009, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    desciption = models.TextField()
    address = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    countrycode = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=50, blank=True)
    active = models.BooleanField(default=False)


#F00001T Field Configurations
class F00001T(TimeStampModel):
    tanentid = models.ForeignKey(F00001, on_delete = models.CASCADE)
    tblname = models.CharField(max_length=100)
    group = models.ForeignKey(F00009, on_delete=models.CASCADE)
    userid = models.ForeignKey(F000091, blank=True, null=True)
    filedname = models.CharField(max_length=200)
    projectid = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200)


#F000012 Field UI Configurations
class F000012(TimeStampModel):
    tanentid = models.ForeignKey(F00001, on_delete= models.CASCADE)
    direc = models.CharField(max_length=50)
    progname = models.ForeignKey(F00008, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    defname = models.CharField(max_length=50)
    changedname = models.CharField(max_length=50)
    desctription = models.TextField()
    fieldname = models.CharField(max_length=200)
    fieldtype = models.CharField(max_length=50)
    widget = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    calculation = models.CharField(max_length=100, blank=True, null=True)
    action = models.CharField(max_length=50)
    defvalue = models.CharField(max_length=100, default='')


#F0000Z	Field Values Definations
class F0000Z(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    table    = models.CharField(max_length=100)
    fieldname  = models.CharField(max_length=100)
    type     = models.CharField(max_length=100, default='json')
    value    = models.TextField()

#F00005	Config
class F00005(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE,)
    type = models.CharField(max_length=50)
    tolerance = models.FloatField(null=True)
    scalingfactor = models.FloatField(null=True)
    match = models.FloatField(null=True)
    loss = models.FloatField(null=True)

#F000051 Hconfig
class F000051(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    net = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


#F000081 Menu Definition
class F000081(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    usergroup = models.ForeignKey(F00009, on_delete=models.CASCADE)
    progname = models.ForeignKey(F00008, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    menuname = models.CharField(max_length=100, blank=True)
    menu_sub1 = models.CharField(max_length=100, blank=True)
    menu_sub2 = models.CharField(max_length=100, blank=True)
    menu_sub3 = models.CharField(max_length=100, blank=True)
    crud = models.CharField(max_length=50, blank=True, null=True)
    view = models.NullBooleanField(default=None)

#F00003	Customer
class F00003(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    control = models.CharField(max_length=100)
    menu = models.CharField(max_length=100, blank=True)
    db = models.CharField(max_length=100, blank=True)
    server = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    plan = models.ForeignKey(F000015, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

#F000031 Partner
class F000031(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
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
    plan = models.ForeignKey(F000015, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


#F000032 Vendor
class F000032(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
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
    plan = models.ForeignKey(F000015, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


#F000034 Employee
class F000034(TimeStampModel):
    tenantid = models.ForeignKey(F00001, on_delete=models.CASCADE)
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



