from rest_framework import serializers
from .models import *

class GetPackSerializer(serializers.ModelSerializer):
    class Meta:
        model=RechargePack
        fields ='__all__'