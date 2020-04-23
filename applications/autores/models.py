from django.db import models
# managers

from .managers import AutorManager

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0) #Numero Positivo si o si

    def __str__(self):
        return  str(self.pk) + '-' + self.nombre + '-' + self.apellidos
    
    class Meta:
        abstract = True #para que no se cree en la db


# Create your models here.
class Autores(Persona):
    suedonimo = models.CharField('Seudonomio', max_length=50,blank=True)
    #Heredo la clase managers para poder usarla fuera
    objects = AutorManager()