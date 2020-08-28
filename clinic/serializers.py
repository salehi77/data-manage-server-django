from .models import ClinicModel
from rest_framework import serializers


class ClinicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClinicModel
        fields = '__all__'
