# vendors/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ServiceForm


def vendor_home(request):
    return render(request, 'vendors/vendor_home.html')


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.vendor = request.user.vendorprofile
            service.save()
            return redirect('vendor_home')
    else:
        form = ServiceForm()
    return render(request, 'vendors/add_service.html', {'form': form})
