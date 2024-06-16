from django.shortcuts import render, redirect, HttpResponse
from myApp.models import *
from myProject.forms import *
from django.contrib import messages
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form=myUsercreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Sign Up successfull')
            return redirect("singin")
    else:
        form=myUsercreationForm(request.POST,request.FILES)
    myDict={
        'form':form                             
    }
    return render(request,'signup.html',myDict)


def singin(request):
    if request.method == 'POST':
        form=myauthenticationform(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return HttpResponse("Sign UP Successfull")
    else:
        form=myauthenticationform(request,data=request.POST)
    myDict={
        'form':form
    }
    return render(request,'signin.html',myDict)



def signout(request):
    logout(request)
    return redirect("singin")