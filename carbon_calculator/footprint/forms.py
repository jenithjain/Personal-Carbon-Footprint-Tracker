from django import forms
from .models import CarbonFootprint

class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprint
        exclude = ['user', 'date', 'total_emissions']
        widgets = {
            'car_miles': forms.NumberInput(attrs={'class': 'form-control'}),
            'public_transport_miles': forms.NumberInput(attrs={'class': 'form-control'}),
            'flights_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'electricity_kwh': forms.NumberInput(attrs={'class': 'form-control'}),
            'gas_therms': forms.NumberInput(attrs={'class': 'form-control'}),
            'waste_pounds': forms.NumberInput(attrs={'class': 'form-control'}),
            'recycling_pounds': forms.NumberInput(attrs={'class': 'form-control'}),
        } 