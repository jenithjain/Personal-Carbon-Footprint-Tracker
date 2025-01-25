from django.db import models
from django.contrib.auth.models import User

class HomeData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    electricity_bill = models.DecimalField(max_digits=10, decimal_places=2)
    kwh_usage = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username}'s Home Data - {self.timestamp.strftime('%Y-%m-%d')}"

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    co2_absorption = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.location} - {self.count} plants"

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    emissions = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username}'s {self.type}"

class CarbonFootprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    
    # Transportation
    car_miles = models.FloatField(default=0)
    public_transport_miles = models.FloatField(default=0)
    flights_hours = models.FloatField(default=0)
    
    # Home Energy
    electricity_kwh = models.FloatField(default=0)
    gas_therms = models.FloatField(default=0)
    
    # Waste
    waste_pounds = models.FloatField(default=0)
    recycling_pounds = models.FloatField(default=0)
    
    # Results
    total_emissions = models.FloatField(default=0)
    
    def calculate_emissions(self):
        car_emissions = self.car_miles * 0.404
        transport_emissions = self.public_transport_miles * 0.14
        flight_emissions = self.flights_hours * 90
        electricity_emissions = self.electricity_kwh * 0.92
        gas_emissions = self.gas_therms * 11.7
        waste_emissions = self.waste_pounds * 0.9
        
        self.total_emissions = (car_emissions + transport_emissions + flight_emissions +
                              electricity_emissions + gas_emissions + waste_emissions)
        return self.total_emissions
