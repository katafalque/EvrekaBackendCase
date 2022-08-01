from django.contrib import admin
from .models import Bin, Operation, BinsByOperations

admin.site.register(Bin)
admin.site.register(Operation)
admin.site.register(BinsByOperations)