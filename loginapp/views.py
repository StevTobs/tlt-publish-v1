from django.shortcuts import render, redirect
from loginapp.models import User
from django.contrib import messages 
# Create your views here.
def sigin(request):
    return render(request,"auth-signin-basic.html")

def signup_form(request):
    return render(request,"signup_form.html")

def form(request):
    print("in form(request)")
    if request.method == "POST" :
        #รับข้อมูล
        _username   = request.POST['username']
        _password   = request.POST['password']
        _first_name = request.POST['first_name']
        _last_name  = request.POST['last_name']
        _tel        = request.POST['tel']
        _province   = request.POST['province']
        _business   = request.POST['job']
        _email   = request.POST['email'] 
        print("-----------------------------")
        print(_username )
        #บันทึกข้อมูล
        user = User.objects.create(
            username   = _username,
            password   = _password,
            first_name = _first_name,
            last_name  = _last_name,
            tel        = _tel,
            province   = _province, 
            business   = _business,
            email   = _email
        )
        # user.save()
        # messages.success(request, 'บันทึกข้อมูลสําเร็จ')
        

        # Check names and prepare context for rendering
        names_to_check = ['akanit', 'other_name']
        users = User.objects.all()
        context = {
            'users': users,
            'names_to_check': names_to_check,
        }
        return render(request, "view_users.html", context)
        
    else :
        return redirect("/")
        #เปลี่ยนเส้นทาง
   

def view_users(request):
    users = User.objects.all()
    return render(request, "view_users.html" , {"users":users})


