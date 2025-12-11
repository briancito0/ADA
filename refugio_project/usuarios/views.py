from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction 
from .forms import (RegistroUsuarioForm, UsuarioModificacionForm, PerfilModificacionForm)
from .models import Perfil
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

# 1VISTA DE REGISTRO
class RegistroUsuario(CreateView):#maneja el registro de nuevos usuarios

    form_class = RegistroUsuarioForm
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('usuarios:login') 

    def form_invalid(self, form):#imprime los errores en la terminal
        print("🚨 ERRORES EN LA VALIDACIÓN DEL FORMULARIO:")
        print(form.errors) 
        messages.error(self.request, "Hubo un error en los datos de registro. Por favor, revisa los campos.")
        return super().form_invalid(form) 
    
    def form_valid(self, form):
   
        response = super().form_valid(form)
        messages.success(self.request, "Te registraste, podes iniciar sesión.")
        return response

# 2VISTA DE MODIFICACIÓN DE PERFIL

class PerfilUsuarioUpdateView(LoginRequiredMixin, UpdateView):
   #para editar datos de perfil

    model = User 
    form_class = UsuarioModificacionForm
    template_name = 'usuarios/modificar_perfil.html'
    success_url = reverse_lazy('usuarios:modificar_perfil') 
    
    def get_object(self, queryset=None):#obtenemos el objeto user cuando se loguea

        return self.request.user

    def get_context_data(self, **kwargs):#añadimos el formulario del perfil al contexto

        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['perfil_form'] = PerfilModificacionForm(
                self.request.POST, 
                instance=self.request.user.perfil
            )
        else:
            context['perfil_form'] = PerfilModificacionForm(
                instance=self.request.user.perfil
            )
        return context

    def post(self, request, *args, **kwargs):#validacion de formulario de usuario y de perfil

        self.object = self.get_object()
        
        # Inicializa ambos formularios con los datos POST
        user_form = self.form_class(request.POST, instance=self.object) 
        perfil_form = PerfilModificacionForm(request.POST, instance=request.user.perfil)
        
        if user_form.is_valid() and perfil_form.is_valid():
            return self.forms_valid(user_form, perfil_form)
        else:
            return self.forms_invalid(user_form, perfil_form)

    @transaction.atomic 
    def forms_valid(self, user_form, perfil_form):
        #guarda los datos de ambos formularios con un mesaje de actualización exitoso
        user_form.save()
        perfil_form.save()
        messages.success(self.request, "Tu perfil ha sido actualizado exitosamente.")
        return redirect(self.get_success_url())

    def forms_invalid(self, user_form, perfil_form):#maneja el formulario ivalido con un mensaje de error

        context = self.get_context_data(form=user_form, perfil_form=perfil_form)
        messages.error(self.request, "Hubo un error al actualizar el perfil. Revisa los campos.")
        return self.render_to_response(context)