from django.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        unique_together = ('name', 'device')

    def __str__(self):
        return self.name + ' ' + self.device.name
    
class Camera(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image.name