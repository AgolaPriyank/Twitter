from django import forms
from .models import Twitt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TwittForm(forms.ModelForm):
    class Meta:
        model = Twitt
        fields = ['text' , 'photo']
    

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')