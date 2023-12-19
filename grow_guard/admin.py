from django.contrib import admin
from .models import Sensor, Device, Camera, Temperature

admin.site.register(Sensor)
admin.site.register(Device)
admin.site.register(Camera)
admin.site.register(Temperature)