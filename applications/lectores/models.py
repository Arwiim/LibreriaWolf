from django.db import models
from django.db.models.signals import post_delete

from applications.libros.models import Categorias, Libros
from applications.autores.models import Persona
# Create your models here.
#from managers
from .managers import PrestamoManager
from .singals import update_libro_stock


class Lectores(Persona):

    class Meta:
        verbose_name = 'Lector'
        verbose_name_plural = 'Lectores'

    def __str__(self):
        return self.nombre

class Prestamos(models.Model):
    lector = models.ForeignKey(Lectores, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    def save(self, *args, **kwargs): #reescribio la funcion save
        print("-----")

        self.libro.stock = self.libro.stock - 1
        self.libro.save()

        super(Prestamos, self).save(*args,**kwargs)

    def __str__(self):
        return self.libro.titulo


#Singal importado!
post_delete.connect(update_libro_stock, sender=Prestamos)