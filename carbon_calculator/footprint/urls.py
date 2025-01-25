from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'footprint'  # This defines the namespace

urlpatterns = [
    path('', views.landing_page, name='landing'),  # Make landing page the root URL
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calculate/', views.input_data, name='input'),
    path('rewards/', views.rewards_page, name='rewards'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('events/', views.events, name='events'),
    path('signup/', views.signup_view, name='signup'),
] 