from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,login,authenticate
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def index(request):
    form=profileform

    name="Shankar Varat"
    return render(request,'index.html',{'form':form})


def profile(request):
    form=profileform
    if request.method =="POST":
        f=form(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/index')
        else:
            m="Form is invalid"
            return render(request, 'profile.html', {'f': f,'m':m})
    else:
        m="not ok"

        return render(request,'profile.html',{'form':form,'m':m})

def signup(request):
    form=UserCreationForm

    return render(request,'signup.html',{'form':form})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                auth.login(request, user)
                return redirect('/index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})



