from django.db import models
from users.models import CustomUser


# Create your models here.
class Ride(models.Model):
    start_location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)

    passenger_count = models.PositiveIntegerField()

    can_shared = models.BooleanField(default = True)
    is_confirmed = models.BooleanField(default = False)
    is_completed = models.BooleanField(default = False)

    arrival_time = models.DateTimeField('Arrival Time')
    special_request = models.CharField(max_length=200, null=True, blank=True)
    driver = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='assign_driver', blank=True, null=True)
    sharer = models.ManyToManyField(CustomUser, related_name='assign_sharer', blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='assign_owner', blank=True, null=True)

    driver_real_name = models.CharField(max_length=120, blank=True)
    vehicle_type = models.CharField(max_length=120, blank=True)
    license_plate_number = models.CharField(max_length=120, blank=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    
class searchFromSharer(models.Model):
    destination = models.CharField(max_length=200)

    earliest_arrival_time = models.DateTimeField('Earliest Arrival Time')
    latest_arrival_time = models.DateTimeField('Latest Arrival Time')

    passenger_count = models.PositiveIntegerField()
    
