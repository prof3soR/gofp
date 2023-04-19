from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import json
# Create your views here.
from django.contrib.auth.models import User
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
                return redirect("login")
    else:
         return render(request,"login.html")
    
def logout_view(request):
     logout(request)
     return redirect("index")

def index(request):
     return render(request,"index.html")

def signup(request):
     if request.method=="POST":
        first_name=request.POST["fullName"]
        username=request.POST["username"]
        email=request.POST["email"]
        phone=request.POST["phoneNumber"]
        password=request.POST["password"]
        user=User(username=username,email=email,password=password,first_name=first_name)
        user.save()
        return redirect("login")

     return render(request,"register.html")

def cal(request):
     return render(request,"cal.html")
def investment_cal(request):
     return render(request,"investment_cal.html")

def top_30_schmeas(request):
     with open("finance/top_30_schemes.json") as f:
          data=json.load(f)
     return render(request,"table_data.html",{"data":data})