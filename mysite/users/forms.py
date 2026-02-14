# this will contain all the form required by user app

from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
# to show inheritance to registerform from usercreationform

class RegisterForm(UserCreationForm):
     email = forms.EmailField()
     #abhi tk feilds add ni hue hai form mai uske liye we have to use meta class 
     class Meta:
         # user ke model mai changes kr rhe hai
         model = User
         #jo jo feild mujhe form pe dekhegi 
         fields = ['username' , 'email','password1' , 'password2']