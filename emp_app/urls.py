from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.index, name="index"),  # Pass the view function directly
]