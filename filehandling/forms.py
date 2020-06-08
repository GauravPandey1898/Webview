from django.contrib.auth.forms import UserCreationForm
from .models import ImageForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email','password1' ,'password2'  ]

class ImageForms(forms.Form):
    name=forms.CharField(max_length=100,label='')
    image=forms.ImageField(label='')

    name.widget.attrs.update({'class':'form-control','placeholder':"Person's Name"})
    image.widget.attrs.update({'class':'file-upload'})

    """class Meta:
        model=ImageForm
        fields=['user_name','image_file']"""
