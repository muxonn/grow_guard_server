from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    value = models.FloatField(max_length = 50)

    def __str__(self):
        return self.name