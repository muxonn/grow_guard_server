from django.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Temperature(models.Model):
    device = models.ForeignKey(Device, related_name = 'temperatures', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.value) + ' - ' + str(self.timestamp.date()) +  ' '  + str(self.timestamp.time())

class Humidity(models.Model):
    device = models.ForeignKey(Device, related_name = 'humidities', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.value) + ' - ' + str(self.timestamp.date()) +  ' '  + str(self.timestamp.time())

class Lighting(models.Model):
    device = models.ForeignKey(Device, related_name = 'lightings', on_delete = models.CASCADE)
    value = models.FloatField(max_length = 50)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.value) + ' - ' + str(self.timestamp.date()) +  ' '  + str(self.timestamp.time())

class Camera(models.Model):
    device = models.ForeignKey(Device,  related_name = 'cameras', null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    timestamp = models.DateTimeField(auto_now_add = True, null = True)
    def __str__(self):
        return self.image.name

class Led(models.Model):
    device = models.OneToOneField(Device, on_delete = models.CASCADE)
    value = models.IntegerField()
    def __str__(self):
        return f"{self.device.id} - Led"