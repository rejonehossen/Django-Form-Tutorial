from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from myApp.models import *
from myProject.forms import *
from django.contrib.auth.decorators import login_required
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
            return redirect("index")
    else:
        form=myauthenticationform(request,data=request.POST)
    myDict={
        'form':form
    }
    return render(request,'signin.html',myDict)



def signout(request):
    logout(request)
    return redirect("singin")


@login_required
def addcategorypage(request):
    if request.method == 'POST':
        form=addcategotyform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("categorylist")
    else:
        form=addcategotyform()
    return render(request,'addcategorypage.html',{'form':form})

@login_required
def categorylist(request):
    return render(request,'categorylist.html')

@login_required
def addtask(request):
    if request.method == 'POST':
        current_user=request.user
        form= addtaskform(request.POST, request.FILES)
        if form.is_valid():
            task=form.save(commit=False)
            task.created_by=current_user
            task.save()
            return redirect("tasklist")
    else:
        form=addtaskform()
    return render(request,'addtask.html',{'form':form})



@login_required
def tasklist(request):
    task= TaskModel.objects.all()
    return render(request,'tasklist.html',{'task':task})


@login_required
def edittask(request,myid):
    task=get_object_or_404(TaskModel,id=myid)
    if request.method == 'POST':
        current_user=request.user
        form= addtaskform(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task=form.save(commit=False)
            task.created_by=current_user
            task.save()
            return redirect("tasklist")
    else:
        form=addtaskform(instance=task)
    return render(request,'edittask.html',{'form':form})


@login_required
def index(request):
    return render(request,'index.html')