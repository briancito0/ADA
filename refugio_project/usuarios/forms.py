from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.db import transaction
from .models import Perfil #importa el modelo perfil

User = get_user_model()

# A. REGISTRO DE USUARIO (Crear User + Perfil)

class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario personalizado para crear un nuevo Usuario y su Perfil asociado.
    """
    # Campos adicionales del modelo Perfil
    nombre_completo = forms.CharField(max_length=150, label="Nombre Completo")
    numero_telefono = forms.CharField(max_length=20, label="Número de Teléfono")

    class Meta(UserCreationForm.Meta):
        model = User
        #Solo se lista los campos de User (username, email)
        # y los campos personalizados. UserCreationForm automáticamente añade
        # los campos 'password1' y 'password2' requeridos.
        fields = ('username', 'email', 'nombre_completo', 'numero_telefono') 

    @transaction.atomic
    def save(self, commit=True):
        """
        Guarda el objeto User y luego actualiza el objeto Perfil asociado.
        """
        #guarda el objeto User, esto se encarga de las contraseñas internamente
        user = super().save(commit=True)
        
        if commit:
            # Accedemos y actualizamos los campos personalizados.
            try:
                perfil = user.perfil 
            except Perfil.DoesNotExist:
                
                perfil = Perfil(usuario=user)

            perfil.nombre_completo = self.cleaned_data['nombre_completo']
            perfil.numero_telefono = self.cleaned_data['numero_telefono']
            perfil.save()
            
        return user

# B. MODIFICACIÓN DE PERFIL

class UsuarioModificacionForm(UserChangeForm):#modifica campos del usuario
    class Meta:
        model = User
        fields = ('username', 'email')

    # Elimina el campo 'password' de UserChangeForm
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in self.fields:
            del self.fields['password']


class PerfilModificacionForm(forms.ModelForm):#modificar los campos del perfil
    class Meta:
        model = Perfil
        fields = ('nombre_completo', 'numero_telefono')