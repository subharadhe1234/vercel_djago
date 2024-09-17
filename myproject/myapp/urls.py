# urls.py
from django.urls import path
from . import views  # Import the views module

# Define the URL pattern for the /api/register endpoint
urlpatterns = [
    path('',views.index,name="index"),
    path('api/register', views.register_user, name='register_user'),
]
