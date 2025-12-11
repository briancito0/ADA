from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Este modelo extiende el modelo User predefinido de Django
# para añadir información específica del refugio.
class Perfil(models.Model):
    # link uno a uno al modelo User de Django
    # Si se borra el User, se borra el Perfil
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    #campos adicionales solicitados:
    nombre_completo = models.CharField(
        max_length=150, 
        blank=True, 
        null=True, 
        verbose_name="Nombre Completo"
    )
    numero_telefono = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        verbose_name="Teléfono de Contacto"
    )
    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def __str__(self):
        
        return f'Perfil de {self.usuario.username}'#muestra el nombre de usuario asociado

@receiver(post_save, sender=User)
def crear_o_actualizar_perfil_usuario(sender, instance, created, **kwargs):
    #sirve para crear o actualizar un perfil cuando se crea o se guarda
    if created:
        # Si el usuario es nuevo, crea un objeto Perfil
        Perfil.objects.create(usuario=instance)
    
    # Intenta guardar el perfil para manejar actualizaciones futuras, 
    # usando un bloque try/except por si el perfil fue borrado manualmente.
    try:
        instance.perfil.save()
    except Perfil.DoesNotExist:
        # Si el perfil no existe por alguna razón, lo crea.
        Perfil.objects.create(usuario=instance)