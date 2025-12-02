from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.TuVistaDeRegistro.as_view(), name='registro'), 
    path('perfil/modificar/', views.TuVistaDeModificarPerfil.as_view(), name='modificar_perfil'),
    
]