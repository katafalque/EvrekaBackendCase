from django.db import models

# Create your views here.
class NavigationRecord(models.Model):
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Vehicle(models.Model):
    plate = models.CharField(max_length=9)

    def __str__(self):
        return self.plate

