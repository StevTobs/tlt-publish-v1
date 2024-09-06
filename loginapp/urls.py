from django.urls import path
from loginapp import views
# from landingapp import views

urlpatterns = [
    # path('home', views.sigin),
    # path('', views.home),
    # path('', landingapp.views.home),
   
    path('login', views.sigin),
    path('signup', views.signup_form),
    path('form', views.form),
    path('view_users', views.view_users),
]
