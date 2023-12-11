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
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sensor_detail(request, name, format=None):
    try:
        sensor = Sensor.objects.get(name = name)
    except Sensor.DoesNotExist:
        return Response('Data not found.', status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SensorSerializer(sensor, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer = SensorSerializer(sensor)
        sensor.delete()
        return Response(serializer.data ,status=status.HTTP_204_NO_CONTENT)