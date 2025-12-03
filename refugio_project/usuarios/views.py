from django.shortcuts import render
<<<<<<< HEAD
=======

>>>>>>> 14c232eec7c2ae9ecf53c78531bb9d6ffafa42a8
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import User
from .forms import UserProfileChangeForm 

<<<<<<< HEAD
class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):#requiere que el usuario esté logueado para acceder
    # Requiere que el usuario esté logueado para acceder
=======
class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
>>>>>>> 14c232eec7c2ae9ecf53c78531bb9d6ffafa42a8
    
    model = User
    form_class = UserProfileChangeForm
    template_name = 'usuarios/modificar_perfil.html'

<<<<<<< HEAD
    success_url = reverse_lazy('home')
    
    def get_object(self, queryset=None):
       
        return self.request.user

class RegistroUsuario(SuccessMessageMixin, CreateView):
    
    form_class = UserCreationForm
    
    template_name = 'usuarios/registro.html'

    success_url = reverse_lazy('login') 
    
    success_message = "Usuario registrado"
=======
    success_url = reverse_lazy('home') 
    
    def get_object(self, queryset=None):
        return self.request.user

class RegistroUsuario(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    
    template_name = 'usuarios/registro.html'
    
    success_url = reverse_lazy('login') 
    
    success_message = "¡Tu cuenta ha sido creada exitosamente! Ya puedes iniciar sesión."
>>>>>>> 14c232eec7c2ae9ecf53c78531bb9d6ffafa42a8
