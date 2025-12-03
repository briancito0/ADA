from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import User
from .forms import UserProfileChangeForm 

class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
    
    model = User
    form_class = UserProfileChangeForm
    template_name = 'usuarios/modificar_perfil.html'

    success_url = reverse_lazy('home') 
    
    def get_object(self, queryset=None):
        return self.request.user

class RegistroUsuario(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    
    template_name = 'usuarios/registro.html'
    
    success_url = reverse_lazy('login') 
    
    success_message = "¡Tu cuenta ha sido creada exitosamente! Ya puedes iniciar sesión."
