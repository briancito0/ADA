from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from .models import Animal
from django.views.generic import TemplateView

# 1. READ: Listar todos los animales (Página principal)
class AnimalListView(ListView):
    model = Animal
    template_name = 'animales/animal_list.html'
    context_object_name = 'animales'
    queryset = Animal.objects.filter(disponible=True) 
    
# 2. READ: Ver detalles de un animal
class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animales/animal_detail.html'
    context_object_name = 'animal'

# 3. CREATE: Agregar un nuevo animal (Solo usuarios logueados)
class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'animales/animal_form.html'
    fields = ['nombre', 'raza','edad', 'sexo', 'especie', 'descripcion', 'foto', 'disponible' ]
    success_url = reverse_lazy('animales:lista')

# 4. UPDATE: Modificar datos de un animal (Solo usuarios logueados)
class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = 'animales/animal_form.html'
    fields = ['nombre', 'raza', 'especie', 'descripcion', 'foto', 'disponible']
    success_url = reverse_lazy('animales:lista')

# 5. DELETE: Eliminar un animal (Solo usuarios logueados)
class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animales/animal_confirm_delete.html'
    context_object_name = 'animal'
    success_url = reverse_lazy('animales:lista')

class HomePageView(TemplateView):
    template_name = 'home.html'