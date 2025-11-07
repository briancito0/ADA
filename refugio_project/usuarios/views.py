from django.shortcuts import render

# usuarios/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
# usuarios/views.py (añadir a la clase anterior)

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin # Para proteger la vista
from django.contrib.auth.models import User
from .forms import UserProfileChangeForm 

class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    # Requiere que el usuario esté logueado para acceder
    
    model = User
    form_class = UserProfileChangeForm
    template_name = 'usuarios/modificar_perfil.html'
    
    # Redirige al perfil o a donde desees tras guardar
    success_url = reverse_lazy('home') # Asume que tienes una URL llamada 'home'
    
    def get_object(self, queryset=None):
        # Asegura que solo el usuario logueado pueda editar su propio perfil
        return self.request.user

class RegistroUsuario(SuccessMessageMixin, CreateView):
    # 1. Indicamos el formulario a usar (el estándar de Django)
    form_class = UserCreationForm
    
    # 2. Indicamos la plantilla a renderizar
    template_name = 'usuarios/registro.html'
    
    # 3. URL a la que redirigir tras un registro exitoso
    success_url = reverse_lazy('login') 
    
    # 4. Mensaje que se muestra tras el registro
    success_message = "¡Tu cuenta ha sido creada exitosamente! Ya puedes iniciar sesión."
