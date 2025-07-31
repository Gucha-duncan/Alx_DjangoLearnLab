from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class OrderForm(ModelForm):
    
    class Meta:
        model = Orders
        fields = ('__all__')
        
class CreateUserForm(UserCreationForm):  # ✅ Fixed typo
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



