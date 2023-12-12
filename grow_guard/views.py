from django.http import JsonResponse
from .models import Sensor, Device
from .serializers import SensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def device_sensors(request, device_id, format = None):
    try:
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sensors = Sensor.objects.filter(device = device)
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = SensorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(device = device)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def device_sensor_detail(request, device_id, name, format = None):
    try:
        device = Device.objects.get(id = device_id)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        sensor = Sensor.objects.get(device = device, name = name)
    except Sensor.DoesNotExist:
         return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = SensorSerializer(sensor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        serializer = SensorSerializer(sensor)
        sensor.delete()
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)