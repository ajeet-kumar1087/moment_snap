# vendors/admin.py
from django.contrib import admin
from .models import VendorProfile, Service

admin.site.register(VendorProfile)
admin.site.register(Service)
