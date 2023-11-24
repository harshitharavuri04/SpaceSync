from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Workspace

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import your custom form
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def base(request):
    return render(request, 'base.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('base')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('base')  # Replace 'home' with the URL name of your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def about(request):
    return render(request, 'firstapp/about.html')


def ContactUs(request):
    return render(request, 'firstapp/ContactUs.html')


def my_account(request):
    return render(request, 'my_account.html')


def submit_workspace(request):
    return render(request, 'registration.html')


def insertws(request):
    u_l = request.POST['workspace_location'];
    u_capacity = request.POST['capacity'];
    u_wtype = request.POST['workspace_type'];
    u_davl = request.POST['days_available'];
    u_ts = request.POST['time_start'];
    u_endstart = request.POST['end_start'];
    u_price = request.POST['price'];
    u_features = request.POST['features'];
    u_desc = request.POST['description'];
    us = Workspace(location=u_l, capacity=u_capacity, workspace_type=u_wtype, days_available=u_davl, time_start=u_ts,
                   end_start=u_endstart, price_per_hour=u_price, features=u_features, description=u_desc);
    us.save();
    return render(request, 'base.html')
