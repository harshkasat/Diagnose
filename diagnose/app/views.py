from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'login.html')


def signups(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        my_user=User.objects.create_user(username=username,password=password)
        my_user.save()
        return redirect('login')
    return render (request,'signups.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')