from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Customer URLs
    path('customers/', views.customer_home, name='customer_home'),
    path('customers/login/', views.customer_login, name='customer_login'),
    path('customers/register/', views.customer_register, name='customer_register'),

    # Vendor URLs
    path('vendors/', views.vendor_home, name='vendor_home'),
    path('vendors/login/', views.vendor_login, name='vendor_login'),
    path('vendors/register/', views.vendor_register, name='vendor_register'),
]

