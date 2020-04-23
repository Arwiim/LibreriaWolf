from django.db import models

# Create your models here.

class Persona(models.Model):

    full_name = models.CharField('Nombres', max_length=50)
    pais = models.CharField('Pais', max_length=50)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Legajo', max_length=10)

    class Meta:
        """Meta definition for ModelPersona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'personas' #Nombre para que se creee con ese nombre  en la DB
        unique_together = ['pais','apelativo'] #para que sea unico
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18),name='edad_mayor_18') #verficiacion para que la edad no sea mayor a 18
        ]
        #abstract = True #Si es un modelo pero no lo crea en la DB

    def __str__(self):
        """Unicode representation of ModelPersona."""
        return self.full_name

class Empleados(Persona): #Heredo de Persona
    empleo = models.CharField('Empleo', max_length=50)

class Cliente(Persona): #Heredo de Persona
    email = models.CharField('Email', max_length=50)