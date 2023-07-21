from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from MLsavedmodel.brain_tumor import brain_tumor_predictions
from MLsavedmodel.chest_xray import chest_xray_predictions
from django.contrib.auth.forms import UserCreationForm
import os
from django.http import JsonResponse
from app.form import ImageUploadForm
from app.models import UserProfileImage




@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            image = form.cleaned_data['image']
            # Save the image to the database
            user_image = UserProfileImage(user=user, image=image)
            user_image.save()
            image_paths = user_image.url
            # prediction = prediction(image)

            return HttpResponse({"image_paths":image_paths})  # Replace 'home' with the URL name of your home page view
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})


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
    return render(request,'signups.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')