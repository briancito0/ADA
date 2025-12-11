from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# 1. MODELO ANIMAL
class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.IntegerField()
    
    SEXO_CHOICES = [ #opciones de genero
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='animales_fotos/', blank=True, null=True)
    
    disponible = models.BooleanField(default=True)# si el estado es disponible
    
    subido_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='animales_publicados')
    fecha_subida = models.DateTimeField(auto_now_add=True)
    
    # Campos para el estado de adopción
    adoptado = models.BooleanField(default=False)# Campo para el estado de adopción
    fecha_adopcion = models.DateTimeField(null=True, blank=True)# Campo para el estado de adopción

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('animales:detalle_animal', kwargs={'pk': self.pk})


# 2. MODELO SOLICITUD DE ADOPCIÓN

class SolicitudAdopcion(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='solicitudes')
    adoptante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitudes_enviadas')
    
    motivos = models.TextField(help_text="Explica por qué deseas adoptar a este animal.")
    
    # Estado de la solicitud
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('A', 'Aprobada'),
        ('R', 'Rechazada'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('animal', 'adoptante', 'estado') 
        verbose_name = "Solicitud de Adopción"
        verbose_name_plural = "Solicitudes de Adopción"

    def __str__(self):
        return f"Solicitud de {self.adoptante.username} para {self.animal.nombre}"