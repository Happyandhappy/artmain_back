from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([UserGroup,ProgramObject,User,Vendor,FieldConfigure,FieldUIConfigure,FieldValDef,Plan,APIMaster,Config,Hconfig,Partner,Employee,MenuDef,Customer])


