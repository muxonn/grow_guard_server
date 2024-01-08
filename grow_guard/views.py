from .models import Device, Camera
from .serializers import DeviceSerializer, CameraSerializer, TemperatureSerializer, HumiditySerializer, LightingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def specific_sensor_list(request, device_id, sensor):
    
    try:
        device = Device.objects.get(id = device_id)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
    print(sensor)
    if request.method == 'GET':
        count = request.query_params.get('count', None)
        
        try:
            count = int(count)
        except Exception:
            count = None

        if sensor == 'temperature':
            temperatures = device.temperatures.all().order_by('-timestamp')
            serializer = TemperatureSerializer(temperatures, many = True)
        elif sensor == 'humidity':
            humidities = device.humidities.all().order_by('-timestamp')
            serializer = HumiditySerializer(humidities, many = True)
        elif sensor == 'lighting':
            lightings = device.lightings.all().order_by('-timestamp')
            serializer = LightingSerializer(lightings, many = True)
        else:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if count is not None:
             data = serializer.data[:count]
        else:
            data = serializer.data

        return Response(data, status = status.HTTP_200_OK)
    
    if request.method == 'POST':

        if sensor == 'temperature':
            serializer = TemperatureSerializer(data = request.data)
        elif sensor == 'humidity':
            serializer = HumiditySerializer(data = request.data)
        elif sensor == 'lighting':
            serializer = LightingSerializer(data = request.data)
        else:
            return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save(device = device)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def device_list(request, format = None):
    if request.method == 'GET':
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = DeviceSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST', 'GET'])
def camera_data(request, device_id):
    try:
        device = Device.objects.get(id=device_id)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = CameraSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(device = device)
            return Response(serializer.data, status = status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == "GET":
        count = request.query_params.get('count', None)
    
        try:
            count = int(count)
        except Exception:
            count = None

        images = device.cameras.all().order_by('-timestamp')
        serializer = CameraSerializer(images, many=True)

        if count is not None:
            data = serializer.data[:count]
        else:
            data = serializer.data

        return Response(data, status = status.HTTP_200_OK)

@api_view(['GET'])
def generate_video(request, device_id):
    try:
        device = Device.objects.get(id = device_id)
    except Device.DoesNotExist:
        return Response({'error': 'Device not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        cameras = device.cameras.all()
        images = [str(camera.image) for camera in cameras]
        print(images)
        
        return Response(status = status.HTTP_200_OK)