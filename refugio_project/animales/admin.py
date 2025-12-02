from django.contrib import admin
from .models import Animal 

@admin.register(Animal) 
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'especie', 'disponible', 'fecha_ingreso')
    list_filter = ('disponible', 'especie')
    search_fields = ('nombre', 'raza')
