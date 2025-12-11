from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegistroUsuario, PerfilUsuarioUpdateView

app_name = 'usuarios' 

urlpatterns = [
    # 1REGISTRO PERSONALIZADO
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    
    # 2INICIO DE SESIÓN
    # Utilizamos LoginView de Django, pero especificamos la plantilla
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    
    # 3CIERRE DE SESIÓN
    # Utilizamos LogoutView de Django, redirigiendo al home
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # 4MODIFICACIÓN DE PERFIL PERSONALIZADA
    path('modificar/', PerfilUsuarioUpdateView.as_view(), name='modificar_perfil'),
]