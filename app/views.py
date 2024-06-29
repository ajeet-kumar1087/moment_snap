from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomerRegistrationForm, CustomerLoginForm, VendorLoginForm, VendorRegistrationForm


def home(request):
    return render(request, 'home.html')


def customer_home(request):
    return render(request, 'customers/customer_home.html')


def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('customer_home')  # Replace 'home' with your actual URL name
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = CustomerLoginForm()

    return render(request, 'customers/customer_login.html', {'form': form})


def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, f'Your Account has been created {email}! Proceed to log in')
            return redirect('customer_login')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'customers/customer_register.html', {'form': form})


def vendor_home(request):
    return render(request, 'vendors/vendor_home.html')


def vendor_login(request):
    if request.method == 'POST':
        form = VendorLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('vendor_home')  # Replace 'home' with your actual URL name
            else:
                form.add_error(None, 'Invalid username or password')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = VendorLoginForm()

    return render(request, 'vendors/vendor_login.html', {'form': form})


def vendor_register(request):
    if request.method == 'POST':
        form = VendorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, f'Your Account has been created {email}! Proceed to log in')
            return redirect('vendor_login')  # Redirect to the login page
    else:
        form = VendorRegistrationForm()
    return render(request, 'vendors/vendor_register.html', {'form': form})
