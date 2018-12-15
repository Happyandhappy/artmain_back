from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer, DocumentSerializer
from .models import *
from tenants.views import get_tenant

class F0000Z1Serializer(DocumentSerializer):
    class Meta:
        model = F0000Z1
        fields = '__all__'


class F00050Serializer(DocumentSerializer):
    class Meta:
        model = F00050
        fields = '__all__'


class F00051Serializer(DocumentSerializer):
    class Meta:
        model = F00051
        fields = '__all__'


class F000502Serializer(DocumentSerializer):
    class Meta:
        model = F000502
        fields = '__all__'



class F00060Serializer(DocumentSerializer):
    class Meta:
        model = F00060
        fields = '__all__'


class F00061Serializer(DocumentSerializer):
    class Meta:
        model = F00061
        fields = '__all__'


class F00062Serializer(DocumentSerializer):
    class Meta:
        model = F00062

        fields = '__all__'

class F00063Serializer(DocumentSerializer):
    class Meta:
        model = F00063
        fields = '__all__'

class F00064Serializer(DocumentSerializer):
    class Meta:
        model = F00064
        fields = '__all__'

class F00065Serializer(DocumentSerializer):
    class Meta:
        model = F00065
        fields = '__all__'
