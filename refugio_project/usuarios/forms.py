# usuarios/forms.py

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm # Para modificar el modelo User
from django import forms

class UserProfileChangeForm(UserChangeForm):
    # Define los campos que deseas permitir editar (excluyendo la contraseña/permisos)
    email = forms.EmailField(required=True) 

    class Meta:
        # Usa el modelo de usuario por defecto
        model = User
        # Especifica los campos a mostrar en el formulario de edición
        fields = ('username', 'first_name', 'last_name', 'email')
        
    # *Nota*: UserChangeForm incluye lógica para limpiar el campo de password, 
    # pero este formulario es para el perfil, no para cambiar la contraseña.
    # La contraseña se cambia a través de las URLs de autenticación de Django.