from django import forms
from .models import Animal, SolicitudAdopcion

# 1. Formulario de Publicación de Animales

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        
        fields = ['nombre', 'raza', 'especie', 'edad', 'sexo', 'descripcion', 'foto', 'disponible']#no muetra 'subido_por' y 'adoptado' porque se manejan en la vista
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4}),
        }

# 2. Formulario de Solicitud de Adopción

class SolicitudAdopcionForm(forms.ModelForm):
    
    # El formulario de confirmación es valido sin texto.
    motivos = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Explica tus motivos para la adopción...'}),
        required=False 
    )
    
    class Meta:
        model = SolicitudAdopcion
        fields = ['motivos']