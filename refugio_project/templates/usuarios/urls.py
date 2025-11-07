from django.urls import path
from . import views # Asegúrate de que importas tus vistas
# from .views import TuVistaDeRegistro, TuVistaDePerfil # (Alternativa)

app_name = 'usuarios' # 📌 Define el namespace 'usuarios'

urlpatterns = [
    # Ruta para REGISTRAR un nuevo usuario
    # El 'name' debe ser 'registro' para que {% url 'usuarios:registro' %} funcione
    path('registro/', views.TuVistaDeRegistro.as_view(), name='registro'), 
    
    # Ruta para MODIFICAR el perfil
    # El 'name' debe ser 'modificar_perfil' para que {% url 'usuarios:modificar_perfil' %} funcione
    path('perfil/modificar/', views.TuVistaDeModificarPerfil.as_view(), name='modificar_perfil'),
    
    # Nota: Reemplaza 'TuVistaDeRegistro' y 'TuVistaDeModificarPerfil' con los nombres reales de tus vistas en usuarios/views.py
]