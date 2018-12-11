from rest_framework import serializers
from .models import *
class F000015Serializer(serializers.Serializer):

    class Meta:
        model = F000015
        fields = ('plancode','planscription','tier','price','effective_date','status')

class F00001Serializer(serializers.Serializer):
    class Meta:
        model = F00001
        fields = ()
