from django.urls import path
from . import views

app_name = 'animales'

urlpatterns = [
    # 1. Lista de Animales
    path('', views.ListaAnimales.as_view(), name='lista_animales'),

    # 2. Publicar Animal
    path('crear/', views.PublicarAnimal.as_view(), name='publicar_animal'), 

    # 3. Detalle de Animal
    path('<int:pk>/', views.DetalleAnimal.as_view(), name='detalle_animal'), 
    
    # 3.5. Modificar Animal
    path('modificar/<int:pk>/', views.ModificarAnimalView.as_view(), name='modificar_animal'),
    
    # 3.6. Eliminar Animal
    path('eliminar/<int:pk>/', views.EliminarAnimalView.as_view(), name='eliminar_animal'),

    # 4. Vistas de Adopción
    path('<int:pk>/adoptar/', views.adoptar_animal_confirmacion, name='adoptar_confirmacion'),
    path('<int:pk>/solicitar/', views.enviar_solicitud_adopcion, name='enviar_solicitud'),
    # 5. Gestión de Publicaciones
    # Panel de publicaciones
    path('mis-publicaciones/', views.gestionar_publicaciones, name='mis_publicaciones'),
    # Vista para listar las solicitudes recibidas
    path('mis-publicaciones/solicitudes/', views.gestionar_solicitudes, name='gestionar_solicitudes'),
    # Vista para aceptar una solicitud específica
    path('solicitud/<int:pk>/aceptar/', views.aceptar_solicitud, name='aceptar_solicitud'),
    # Vista para listar las solicitudes hechas
    path('mis-solicitudes/', views.ver_mis_solicitudes, name='mis_solicitudes'),
]