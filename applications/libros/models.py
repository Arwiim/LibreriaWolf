from django.db import models
from applications.autores.models import Autores
from .managers import LibrosManager, CategoriaManager

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=30)

    objects = CategoriaManager() #Manager de categoria
    
    def __str__(self):
        return self.nombre

class Libros(models.Model):
    categoria = models.ForeignKey(
        Categorias, #FK de Categorias
        on_delete=models.CASCADE,
        related_name='categoria_libro') #'contraint_fk'

    autor = models.ManyToManyField(Autores) #Many to Many: 1 autor = n Libros ,-----,  1 Libro = n Autores, DJANGO CREA INTERNAMENTE TABLA INTERMEDIA, ES UNA LISTA
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada',null=True, blank=True) #almacenar en 'portada'
    visitas = models.PositiveIntegerField()

    objects = LibrosManager() #Manager de Libro

    def __str__(self):
        return  str(self.pk) + '-' +self.titulo