from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/employee/profile')
        else:
            messages.error(request,"invalid username")

    return render(request,'authentication/login.html')

def auth_logout(request):
    logout(request)
    messages.success(request,"logout successfully")
    return redirect('/authentication')

def auth_registration(request):
    return render(request,'authentication/registration.html')

def forget_password(request):
    return render(request,'authentication/forget.html')

