from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # URL PRINCIPAL /
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # URLs de las aplicaciones
    path('animales/', include('animales.urls')),
    path('usuarios/', include('usuarios.urls')), 
    
    # URLs de Django Auth
    path('', include('django.contrib.auth.urls')),
]

# Configuración de archivos de media y estáticos para desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)