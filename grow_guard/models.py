from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    device = models.ForeignKey(Device, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50, unique = True)
    value = models.FloatField(max_length = 50)

    def __str__(self):
        return self.name