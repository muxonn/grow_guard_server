from django.db import models
from django.utils import timezone

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Temperature(models.Model):
    device = models.ForeignKey(Device, related_name = 'temperatures', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    # def save(self, *args, **kwargs):
    #     self.timestamp = timezone.now()
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return '(' + str(self.device.name) + ') ' + str(self.value)

class Humidity(models.Model):
    device = models.ForeignKey(Device, related_name = 'humidities', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.value

class Lighting(models.Model):
    device = models.ForeignKey(Device, related_name = 'lighting', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.value

class Sensor(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    value = models.FloatField(max_length = 50)

    class Meta:
        unique_together = ('name', 'device')

    def __str__(self):
        return self.name + ' ' + self.device.name
    
class Camera(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.name