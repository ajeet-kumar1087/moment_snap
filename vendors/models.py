# vendors/models.py
from django.contrib.auth.models import User
from django.db import models


class VendorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Service(models.Model):
    SERVICE_TYPES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('prewedding', 'Pre-wedding'),
        ('other', 'Other')
    ]
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_service_type_display()} - {self.rate}"
