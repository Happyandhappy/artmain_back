from rest_framework import serializers
from .models import *

class UserGroupSerializer(serializers.Serializer):
    class Meta:
        model = UserGroup
        fields = ('userType','desc',)

class PlanSerializer(serializers.Serializer):
    class Meta:
        model = Plan
        fields = ('plancode','plandescription','tier','price','terms','threshold','multiplier','effective_date',)

class ProgramObjectSerializer(serializers.Serializer):
    class Meta:
        model = ProgramObject
        fields = '__all__'

class APIMasterSerializer(serializers.Serializer):
    class Meta:
        model  = APIMaster
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
class FieldConfigureSerializer(serializers.Serializer):
    class Meta:
        model = FieldConfigure
        fields = '__all__'

class FieldUIConfigureSerializer(serializers.Serializer):
    class Meta:
        model = FieldUIConfigure
        fields = ('tanentid', 'direc', 'progname', 'type', 'defname', 'changedname', 'desctription', 'fieldname', 'fieldtype', 'widget', 'visible', 'position', 'action', 'defvalue')

class FieldValDefSerializer(serializers.Serializer):
    class Meta:
        model = FieldValDef
        fields = '__all__'

class ConfigSerializer(serializers.Serializer):
    class Meta:
        model = Config
        fields = '__all__'

class HconfigSerializer(serializers.Serializer):
    class Meta:
        model = Hconfig
        fields = '__all__'

class MenuDefSerializer(serializers.Serializer):
    class Meta:
        model = MenuDef
        fields = ('tenantid','usergroup','progname','type','menuname')

class CustomerSerializer(serializers.Serializer):
    class Meta:
        model = Customer
        fields = (
                  'tenantid','name',
                  'description','address',
                  'country','country_code',
                  'phone','email',
                  'contact','active',
                  'control','plan',
                  'status'
        )

class PartnerSerializer(serializers.Serializer):
    class Meta:
        model = Partner
        fields = (
                'tenantid', 'name',
                'description', 'address',
                'country', 'country_code',
                'phone', 'email',
                'contact', 'active',
                'control', 'plan',
                'status')

class VendorSerializer(serializers.Serializer):
    class Meta:
        model = Vendor
        fields = (
            'tenantid', 'name',
            'description', 'address',
            'country', 'country_code',
            'phone', 'email',
            'contact', 'active',
            'control', 'plan',
            'status'
        )

class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = '__all__'
