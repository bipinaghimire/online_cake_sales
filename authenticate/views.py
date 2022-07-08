from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# import authenticate

# Create your views here.
def login_fn(request):
    if request.method =="POST":
        user = authenticate(request,
        username = request.POST["username"],
        password = request.POST["password"])
        # print(user)
        if user is not NONE:
            login(request,user)
            return redirect("/customer")
        else:
            return redirect(request, "authenticate/login")
    else:
        return render(request, "authenticate/login.html")
    

def register_fn(request):
    print(request.method)
    if request.method =="POST":
        user = User.objects.create_user(
            first_name = request.POST["firstname"],
            last_name = request.POST["lastname"],
            email = request.POST["email"],
            username = request.POST["username"],
            password = request.POST["password"]
            )
        return redirect("/authenticate/login")     
        # print(request.POST)
    else:
        return render(request, "authenticate/register.html")

def logout_fn(request):
    return render(request, "authenticate/login")
    
