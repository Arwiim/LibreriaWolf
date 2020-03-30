from django.db import models
from applications.libros.models import Categorias, Libros
# Create your models here.
#from managers
from .managers import PrestamoManager


class Lectores(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=20)
    edad = models.PositiveIntegerField(default=0) #en caso de que no  nos pida, lo dejamos por valor en 0

    def __str__(self):
        return self.nombre

class Prestamos(models.Model):
    lector = models.ForeignKey(Lectores, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestame = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def __str__(self):
        return self.libro.titulo