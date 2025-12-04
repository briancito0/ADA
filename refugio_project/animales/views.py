from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from .models import Animal
from django.views.generic import TemplateView

class AnimalListView(ListView):
    model = Animal
    template_name = 'animales/animal_list.html'
    context_object_name = 'animales'
    queryset = Animal.objects.filter(disponible=True).order_by('nombre')
    
class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animales/animal_detail.html'
    context_object_name = 'animal'

class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = 'animales/animal_form.html'
    fields = ['nombre', 'raza', 'especie', 'edad', 'sexo', 'descripcion', 'foto', 'disponible']
    success_url = reverse_lazy('animales:lista')

class AnimalDeleteView(LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'animales/animal_confirm_delete.html'
    context_object_name = 'animal'
    success_url = reverse_lazy('animales:lista')

class HomePageView(TemplateView):
    template_name = 'home.html'

class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'animales/animal_form.html'
    fields = ['nombre', 'raza', 'edad', 'sexo', 'especie', 'descripcion', 'foto', 'disponible']
    success_url = reverse_lazy('animales:lista')

    def form_valid(self, form):
   
        form.instance.subido_por = self.request.user
        return super().form_valid(form)

class AdoptarAnimalDeleteView(LoginRequiredMixin, DeleteView):
    
    model = Animal
    template_name = 'animales/animal_confirm_adopcion.html'
    context_object_name = 'animal'
    success_url = reverse_lazy('animales:lista')