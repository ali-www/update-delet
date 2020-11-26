from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Po

class Poform(ModelForm):
    class Meta:
        model = Po
        fields =  ['name','photo']




class FormSignup(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())  

    class Meta:
        model = User
        fields = ['username','email','password1','password2']      


   

       
