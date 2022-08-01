from django.shortcuts import render
from .models import Bin, BinsByOperations, Operation

def qtwo_view(request):
    bin_operations = BinsByOperations.objects.values('collection_frequency', 'bin_id', 'operation_id')
    data = [pair for pair in bin_operations]
    response = {
        'collection_frequencies' : data
    }

    return render(request, 'q2.html', response)
