from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from animales.views import HomePageView
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('animales/', include('animales.urls')),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    

