# vendors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_home, name='vendor_home'),
    path('add-service/', views.add_service, name='add_service'),
    # Add more vendor-related URLs here...
]
