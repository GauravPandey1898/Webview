from django.shortcuts import render , redirect
from django import forms
import cv2
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from sample import settings
from .forms import UserForm,ImageForms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ImageForm
from MachineLearning.detectface import detect_face
from numpy import asarray


def homeView(request):
    return render(request,'filehandling/home.html')


def registerView(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filehandling:login')
    else:
        form = UserForm()
    params = {
        'forms' : form
    }
    return render(request, 'login_page/register.html', params)



def loginView(request):
    if request.method == 'POST':
        user1 = request.POST.get('login')
        passwd = request.POST.get('password')
        user = authenticate(request , username = user1 , password = passwd )
        if user is not None:
            login(request , user)
            return redirect('filehandling:home_auth')
        else:
            messages.error(request, 'Oops, Wrong username or password, please try a diffrerent one')
    return render(request , 'login_page/login.html')

def logoutView(request):
    logout(request)
    return render(request,'filehandling/home.html')


@login_required(login_url='filehandling:login')
def home_authView(request):
    return render(request,'filehandling/home_auth.html')

@login_required(login_url='filehandling:login')
def image_uploadView(request):
    form=ImageForms()
    if request.method=='POST':

        form=ImageForms(request.POST,request.FILES)
        current_user = request.user
        if form.is_valid():
            username=form.cleaned_data['name']
            userpicture=form.cleaned_data['image']



            #if(detect_face(userpicture)):
                #print(true)
            m=ImageForm(id=None,user_id=current_user,user_name=username,image_file=userpicture)
            m.save()

            """m=ImageForm(pk=current_user.id)
            m.user_name=form.cleaned_data['name']
            m.image_file=form.cleaned_data['image']
            m.save()"""
            messages.success(request,'Image was successfully uploaded')

            redirect('filehandling:home_auth')
        else:
             messages.error(request,'All fields are required')
    else:
        form = ImageForms()
    params = {
            'forms' : form
                }

    return render(request,'fileupload/fileupload.html',params)


def imageView(request):
    current_user = request.user
    img=[e.image_file for e in ImageForm.objects.filter(user_id=current_user)]
    path=settings.MEDIA_URL
    return render(request,'viewimage/viewimage.html',{"img":img, 'media_url':path})

def classificationView(request):
    return render(request,'classification/classification.html')
