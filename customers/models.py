# customers/models.py
from django.contrib.auth.models import User
from django.db import models

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add more customer-related fields here...

    def __str__(self):
        return self.user.username
