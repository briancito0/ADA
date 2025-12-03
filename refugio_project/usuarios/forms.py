from django.contrib.auth.models import User
<<<<<<< HEAD
from django.contrib.auth.forms import UserChangeForm
from django import forms

class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(required=True) #campos editables excepto contraseña

    class Meta:
        
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')#elegimos los campos a mostrar en el formulario de edición
=======
from django.contrib.auth.forms import UserChangeForm 
from django import forms

class UserProfileChangeForm(UserChangeForm):
    email = forms.EmailField(required=True) 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
>>>>>>> 14c232eec7c2ae9ecf53c78531bb9d6ffafa42a8
