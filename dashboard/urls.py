from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('invoice', views.invoice, name='invoice'),
]