from rest_framework import serializers
from .models import Sensor, Device

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name', 'value']

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['name']