from django.shortcuts import render,redirect
from .models import Customer
# Create your views here.

def home(request):
    if request.method == "POST":
        data = request.POST.copy()
        name = data.get('name')
        email = data.get('email')
        number = data.get('number')
        message = data.get('comments')

        # name = request.POST["name"]
        # email = request.POST["email"]
        # number = request.POST["number"]
        # message = request.POST["comments"]

        # customer = Customer.objects.create(
        #     name = name,
        #     email = email,
        #     number = number,
        #     message = message
        # )
        cus = Customer()
        cus.name = name
        cus.email = email
        cus.number = number
        cus.message = message

        cus.save()
        return redirect("/")
    
    else:
        return render(request,"home.html")
    

