from django.contrib import admin
from .models import Animal # importa el modelo Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 
        'especie', 
        'disponible', 
        'adoptado', 
        'fecha_subida', 
        'subido_por'
    )

admin.site.register(Animal, AnimalAdmin)