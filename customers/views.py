# customers/views.py
from django.shortcuts import render


def customer_home(request):
    return render(request, 'customers/customer_home.html')
