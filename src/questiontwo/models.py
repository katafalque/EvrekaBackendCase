from gc import collect
from django.db import models
from django.forms import IntegerField

class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Operation(models.Model):
    name = models.CharField(max_length=20)

class BinsByOperations(models.Model):
    class Meta:
        unique_together = ['bin_id', 'operation_id']
    
    bin_id = models.ForeignKey('Bin', on_delete=models.CASCADE)
    operation_id = models.ForeignKey('Operation', on_delete=models.CASCADE)
    collection_frequency = models.IntegerField(default=1)
    last_collection = models.DateTimeField()
