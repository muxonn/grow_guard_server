from django.contrib import admin
from .models import Sensor, Device

admin.site.register(Sensor)
admin.site.register(Device)