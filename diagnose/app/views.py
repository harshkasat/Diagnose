from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from MLsavedmodel.brain_tumor import brain_tumor_predictions
from MLsavedmodel.chest_xray import chest_xray_predictions
from MLsavedmodel.melanoma_cancer import melanoma_cancer_predictions

from django.contrib.auth.forms import UserCreationForm
import os
from django.http import JsonResponse
from app.form import ImageUploadForm, MedicalConditionForm
from app.models import UserProfileImage




@login_required(login_url='login')
def home(request):
    form = ImageUploadForm()
    medical_form = MedicalConditionForm()
    if request.method == 'POST' :
        # if 'form' in request.POST and 'medical_form' in request.POST :
            # print("inside form and medical_form")
            form = ImageUploadForm(request.POST, request.FILES)
            medical_form = MedicalConditionForm(request.POST)

            if form.is_valid() and medical_form.is_valid():
                user = request.user
                image = form.cleaned_data['image']
                medical_condition = medical_form.cleaned_data['medical_condition']
                # Save the image to the database
                user_image = UserProfileImage(user=user, image=image)
                user_image.save()
                # print(user_image.save())
                image_paths = user_image.image.url
                print(image_paths)
                if medical_condition == 'brain_tumor':
                    prediction = brain_tumor_predictions(image_paths)
                elif medical_condition == 'chest_xray':
                    prediction = chest_xray_predictions(image_paths)
                else :
                    prediction = melanoma_cancer_predictions(image_paths)

                return JsonResponse({"prediction":prediction,
                                    "image_path":image_paths})
        
    return render(request, 'home.html', {"form": form,
                                         "medical_form":medical_form})


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