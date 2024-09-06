from django.urls import path, include
from django.contrib import admin
from tltapp import views

urlpatterns = [
    path('app', views.forminput),
     path("admin/", admin.site.urls),
    

]