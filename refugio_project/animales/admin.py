# animales/admin.py
from django.contrib import admin
from .models import Animal # ⬅️ Importa el modelo

@admin.register(Animal) # ⬅️ Registra el modelo Animal
class AnimalAdmin(admin.ModelAdmin):
    # Esto es opcional, pero ayuda a la visualización
    list_display = ('nombre', 'raza', 'especie', 'disponible', 'fecha_ingreso')
    list_filter = ('disponible', 'especie')
    search_fields = ('nombre', 'raza')
