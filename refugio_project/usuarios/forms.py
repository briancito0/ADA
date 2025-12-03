from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm 
from django import forms

class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
