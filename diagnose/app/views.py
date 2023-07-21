from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.brain_tumor import prediction
from django.contrib.auth.forms import UserCreationForm
import os
from django.http import JsonResponse
from app.form import UserRegistrationForm



@login_required(login_url='login')
def home(request):
    if request.method == 'POST' and request.FILES.get('img'):
        image = request.FILES['image']
        image_path = os.path.join('temp', image.name)
        with open(image_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        prediction = prediction(image_path)
        os.remove(image_path)
        return JsonResponse({"prediction":prediction})
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
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            my_user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render (request,'signups.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')