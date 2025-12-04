from django.urls import path
from . import views


app_name = 'animales'

urlpatterns = [
    path('', views.AnimalListView.as_view(), name='lista'),
    path('<int:pk>/', views.AnimalDetailView.as_view(), name='detalle'),
    path('registrar/', views.AnimalCreateView.as_view(), name='registrar'),
    path('<int:pk>/editar/', views.AnimalUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.AnimalDeleteView.as_view(), name='eliminar'),
    path('<int:pk>/adoptar/', views.AdoptarAnimalDeleteView.as_view(), name='adoptar'),
]