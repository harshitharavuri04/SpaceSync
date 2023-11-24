from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Workspace, Booking
from .forms import BookingForm
# Create your views here.
from django.shortcuts import render
from .models import Workspace
from django.db.models import Q
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
    u_l = request.POST['city'];
    u_add = request.POST['address']
    u_wtype = request.POST['workspaceType'];
    u_f = request.POST['furniture'];
    u_park = request.POST['parking'];
    u_price = request.POST['costPerDay'];
    u_cancellation = request.POST['cancellationPolicy'];
    u_image = request.FILES['imageUpload'];
    us = Workspace(city=u_l, address=u_add, workspace_type=u_wtype, furniture=u_f,
                   parking=u_park,
                   cancellation_policy=u_cancellation, cost_per_day=u_price, image_upload=u_image);
    us.save();
    return render(request, 'base.html')


def search_workspaces(request):
    if request.method == 'GET':
        # Get the filter parameters from the request
        city = request.GET.get('city')
        workspace_type = request.GET.get('workspaceType')

        # Build a query based on the provided filters
        query = Q()
        if city:
            query &= Q(city=city)
        if workspace_type:
            query &= Q(workspace_type=workspace_type)

        # Execute the query and get the results
        workspaces = Workspace.objects.filter(query)
        print(workspaces)
        # Render the results in the template
        return render(request, 'search_results.html', {'workspaces': workspaces})

    return render(request, 'search_results.html')


def book_workspace(request, workspace_id):
    workspace = get_object_or_404(Workspace, pk=workspace_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.workspace = workspace
            booking.save()
            return redirect('booking_success')  # Create a success page for bookings
    else:
        form = BookingForm()

    return render(request, 'book_workspace.html', {'form': form, 'workspace': workspace})
