from django.urls import path
from .views import (
    AnimalListView, 
    AnimalDetailView, 
    AnimalCreateView, 
    AnimalUpdateView, 
    AnimalDeleteView
)

app_name = 'animales'

urlpatterns = [
    path('', AnimalListView.as_view(), name='lista'),
    path('<int:pk>/', AnimalDetailView.as_view(), name='detalle'),
    path('nuevo/', AnimalCreateView.as_view(), name='crear'),
    path('<int:pk>/editar/', AnimalUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', AnimalDeleteView.as_view(), name='eliminar'),
]