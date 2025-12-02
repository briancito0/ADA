from django.urls import path
from .views import RegistroUsuario, PerfilUsuarioUpdateView

app_name = 'usuarios' 

urlpatterns = [
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    
    path('modificar/', PerfilUsuarioUpdateView.as_view(), name='modificar_perfil'),
]