from django.urls import path
from landingapp import views

urlpatterns = [
    path('', views.home),
]