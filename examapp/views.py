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


def uprofile(request):


            u = User.objects.get(username=request.user)
            try:
                profile1 = profile.objects.get(username=u)
            except:
                profile1 = "Not found"
            return render(request, 'eprofile.html', {'profile1': profile1})


def eprofile(request):
            form=profileform
            if request.method =="POST":
                f=form(request.POST)
                if f.is_valid():
                    f.save()
                    return redirect('/index')
                else:
                    m="Form is invalid"
                    return render(request, 'eprofile', {'form': form})
            else:
                return render(request, 'eprofile.html', {'form':form})

                #return render(request,'uprofile',{'form':form})

def signup(request):
    form=UserCreationForm
    if request.method=='POST':
        f=form(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/index')
        else:
            m="Invalid data !!"
            return HttpResponse("Not valid Data")


    return render(request,'signup.html',{'form':form})
def loginu(request):
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
        return render(request, 'login.html')
def logoutu(request):
            logout(request)
            return redirect("/index")

def texam(request):
            u=User.objects.get(username=request.user)
            try:
                profile1=profile.objects.get(username=u)
            except:
                profile1="Not found"
            ques=questions.objects.all()
            tq=len(ques)
            return render(request,'texam.html',{'u':u,'profile1':profile1,'ques':ques,'tq':tq})

def uans(request):
    u = User.objects.get(username=request.user)
    try:
        profile1 = profile.objects.get(username=u)
    except:
        profile1 = "Not found"
    ques = questions.objects.all()
    form=uaform()

    tq = len(ques)
    if request.method=="POST":
        f=uaform(request.POST)

        if f.is_valid:
            f.save()
            return redirect('/texam')
        else:
            m='form is not valid'
            return render(request, 'uans.html', {'m': m, 'profile1': profile1, 'ques': ques, 'tq': tq})

    return render(request, 'uans.html', {'u': u, 'profile1': profile1, 'ques': ques, 'tq': tq})



