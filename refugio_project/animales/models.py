from django.db import models

class Animal(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    especie = models.CharField(max_length=50, choices=[('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro')])
    edad = models.IntegerField(verbose_name='Edad', null=True, blank=True)
    descripcion = models.TextField()
    SEXO_CHOICES = [
        ('M', 'Macho'),
        ('H', 'Hembra'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name='Sexo')

    
    foto = models.ImageField(upload_to='animales_fotos/') 

    fecha_ingreso = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return f"{self.nombre} ({self.raza})"
    from django.urls import reverse
    def get_absolute_url(self):
        return reverse('animales:detalle', kwargs={'pk': self.pk})