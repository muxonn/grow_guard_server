from rest_framework import serializers
from .models import Device, Camera, Temperature, Humidity, Lighting, Led

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name']

class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = ['value', 'timestamp']

class LightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lighting
        fields = ['value', 'timestamp']

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Humidity
        fields = ['value', 'timestamp']

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Camera
        fields = ['id', 'image', 'timestamp']

class LedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Led
        fields = ['value']