from django.http import JsonResponse
from .models import Sensor
from .serializers import SensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sensor_list(request, format=None):
    if request.method == 'GET':
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
