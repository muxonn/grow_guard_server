from rest_framework import serializers
from .models import Sensor, Device, Camera, Temperature, Humidity, Lighting

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name']

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['device', 'value', 'timestamp']

class LightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lighting
        fields = ['device', 'value', 'timestamp']

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ['device', 'value', 'timestamp']


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'value']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'image']