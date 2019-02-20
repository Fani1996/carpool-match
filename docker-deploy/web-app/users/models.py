from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    real_name = models.CharField(max_length=120)
    driver = models.BooleanField(blank=True)
    vehicle_type = models.CharField(max_length=120, blank=True)
    license_plate_number = models.CharField(max_length=120, blank=True)
    capacity = models.PositiveIntegerField(blank=True, null=True)
    optional_info = models.TextField(blank=True)
    email = models.EmailField(max_length=254, blank=False)
    
    def __str__(self):
        return self.username
