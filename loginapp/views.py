from django.shortcuts import render

# Create your views here.
def sigin(request):
    return render(request,"auth-signin-basic.html")