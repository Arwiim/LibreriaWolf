from django.db import models
# managers

from .managers import AutorManager

# Create your models here.
class Autores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField() #Numero Positivo si o si

    objects = AutorManager() #Heredo la clase managers para poder usarla fuera

    def __str__(self):
        return  str(self.pk) + '-' + self.nombre + '-' + self.apellido