# Generated by Django 5.1.4 on 2025-01-24 18:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarbonFootprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('car_miles', models.FloatField(default=0)),
                ('public_transport_miles', models.FloatField(default=0)),
                ('flights_hours', models.FloatField(default=0)),
                ('electricity_kwh', models.FloatField(default=0)),
                ('gas_therms', models.FloatField(default=0)),
                ('waste_pounds', models.FloatField(default=0)),
                ('recycling_pounds', models.FloatField(default=0)),
                ('total_emissions', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
