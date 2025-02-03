from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.index, name="index"),
    path('all_emp',views.all_emp,name="all emp")  # Pass the view function directly
]