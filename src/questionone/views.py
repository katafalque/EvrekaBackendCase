from django.shortcuts import render
from .models import NavigationRecord, Vehicle
from datetime import datetime, timedelta
import json


def qone_view(request):
    time = datetime.now() - timedelta(hours=48)
    navigation_records = NavigationRecord.objects.filter(datetime__gte=time)
    last_points = []
    for record in navigation_records:
        data = {
            'latitute' : record.latitude,
            'longitude': record.longitude,
            'vehicle_plate' : record.vehicle.plate,
            'datetime' : record.datetime
        }
        last_points.append(data)
    
    response = {
        'last_points' : json.dumps(last_points, default=str)
    }
    return render(request, 'q1.html', response)