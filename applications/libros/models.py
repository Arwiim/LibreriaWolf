from django.db import models
from django.db.models.signals import post_save#lo que pasa despues del guardado

from PIL import Image

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
    stock = models.PositiveIntegerField(default=0)

    objects = LibrosManager() #Manager de Libro

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['id']

    def __str__(self):
        return  str(self.pk) + '-' +self.titulo
    
#Funcion para optimizar la imagen con la calidad y dismunuirla

def optimize_image(sender, instance, **kwargs): #Enviar, trabajr con la instancia, sobrescribir
    print("========")
    print(instance)
    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)
post_save.connect(optimize_image,sender=Libros)