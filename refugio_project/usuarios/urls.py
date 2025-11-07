# usuarios/urls.py

from django.urls import path
from .views import RegistroUsuario, PerfilUsuarioUpdateView

# Define un namespace para esta aplicación (opcional pero buena práctica)
app_name = 'usuarios' 

urlpatterns = [
    # URL para registrar un nuevo usuario
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    
    # URL para que el usuario logueado modifique su perfil
    path('modificar/', PerfilUsuarioUpdateView.as_view(), name='modificar_perfil'),
]