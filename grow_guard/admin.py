from django.contrib import admin
from .models import Device, Camera, Temperature, Humidity, Lighting

admin.site.register(Device)
admin.site.register(Camera)

admin.site.register(Temperature)
admin.site.register(Humidity)
admin.site.register(Lighting)