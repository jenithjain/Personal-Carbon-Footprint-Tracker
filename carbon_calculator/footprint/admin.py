from django.contrib import admin
from .models import CarbonFootprint

@admin.register(CarbonFootprint)
class CarbonFootprintAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total_emissions')
    list_filter = ('user', 'date')
