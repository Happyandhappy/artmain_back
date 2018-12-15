from rest_framework import serializers
from .models import *

class UserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('userType','desc',)

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('plancode','plandescription','tier','price','terms','threshold','multiplier','effective_date',)

class ProgramObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramObject
        fields = '__all__'

class APIMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = APIMaster
        # tenantid = serializers.RelatedField(source='tenants.TenantMaster', write_only=True)
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class FieldConfigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldConfigure
        fields = '__all__'

class FieldUIConfigureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldUIConfigure
        fields = ('tanentid', 'direc', 'progname', 'type', 'defname', 'changedname', 'desctription', 'fieldname', 'fieldtype', 'widget', 'visible', 'position', 'action', 'defvalue')

class FieldValDefSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldValDef
        fields = '__all__'

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

class HconfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hconfig
        fields = '__all__'

class MenuDefSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDef
        fields = ('tenantid','usergroup','progname','type','menuname')

class CustomerSerializer(serializers.ModelSerializer):
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

class PartnerSerializer(serializers.ModelSerializer):
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

class VendorSerializer(serializers.ModelSerializer):
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

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
