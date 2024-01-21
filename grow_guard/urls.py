"""
URL configuration for grow_guard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from grow_guard import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', views.device_list),
    path('devices/<int:device_id>/sensors/<str:sensor>/', views.specific_sensor_list),
    path('devices/<int:device_id>/camera/', views.camera_data),
    path('devices/<int:device_id>/camera/generate_video', views.generate_video),
    path('devices/<int:device_id>/led_value/', views.led_value)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



urlpatterns = format_suffix_patterns(urlpatterns)
