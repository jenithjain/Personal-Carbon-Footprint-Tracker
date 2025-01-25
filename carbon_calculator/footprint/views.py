from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CarbonFootprint, HomeData, Plant, Vehicle
from .forms import CarbonFootprintForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

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
    api_key = '9dead4ec7bc94844b5e09bcbf8d20b86'
    logger.info(f"Decarbonize page accessed by user: {request.user}")
    
    # Log query parameters if any
    if request.GET:
        logger.info(f"Query parameters: {request.GET}")
    
    context = {
        'api_key': api_key
    }
    logger.info("Rendering decarbonize page with API key")
    return render(request, 'footprint/decarbonize.html', context)

@csrf_exempt
def calculate_route(request):
    if request.method == 'POST':
        try:
            logger.info("Route calculation request received")
            data = json.loads(request.body)
            source = data.get('source')
            destination = data.get('destination')
            
            logger.info(f"Calculating route from {source} to {destination}")
            
            # Log the complete request data
            logger.debug(f"Complete request data: {data}")
            
            return JsonResponse({
                'success': True,
                'message': 'Route calculation endpoint reached',
                'source': source,
                'destination': destination
            })
        except Exception as e:
            logger.error(f"Error calculating route: {str(e)}", exc_info=True)
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    logger.warning("Invalid request method for route calculation")
    return JsonResponse({
        'success': False,
        'error': 'Invalid request method'
    })
