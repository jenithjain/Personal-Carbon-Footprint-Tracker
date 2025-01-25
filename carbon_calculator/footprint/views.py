from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarbonFootprint, HomeData, Plant, Vehicle
from .forms import CarbonFootprintForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse

# Create your views here.

@login_required
def input_data(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'footprint/input.html')

@login_required
def dashboard(request):
    user_footprints = CarbonFootprint.objects.filter(user=request.user).order_by('-date')
    latest_footprint = user_footprints.first()
    
    context = {
        'latest_footprint': latest_footprint,
        'footprint_history': user_footprints,
    }
    return render(request, 'footprint/dashboard.html', context)

@login_required
def rewards_page(request):
    return render(request, 'footprint/rewards.html')

def landing_page(request):
    if request.user.is_authenticated:
        return redirect('footprint:dashboard')
    return render(request, 'footprint/landing.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'footprint/signup.html', {'form': form})

def profile(request):
    return render(request, 'footprint/profile.html')

def events(request):
    return render(request, 'footprint/events.html')

def login_view(request):
    # your login view logic
    return render(request, 'footprint/login.html')

def signup_view(request):
    # your signup view logic
    return render(request, 'footprint/signup.html')

# Remove the my_home view if it exists
# def my_home(request):
#     return render(request, 'footprint/my_home.html')

@login_required
def decarbonize(request):
    if request.method == 'POST':
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        transport_modes = request.POST.getlist('transport')
        
        # Here you would typically:
        # 1. Call a maps API to get route information
        # 2. Calculate carbon emissions for each transport mode
        # 3. Return the results
        
        # For now, just render the template
        return render(request, 'footprint/decarbonize.html')
        
    return render(request, 'footprint/decarbonize.html')
