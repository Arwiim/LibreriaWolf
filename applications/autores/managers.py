from django.db import models

from django.db.models import Q #Sentencias de tipo 'or'

class AutorManager(models.Manager):
    """ managers para el modelo autor """

    def listar_autores(self):

        return self.all()
    
    def buscar_autor(self,kword):

        resultado = self.filter(nombre__icontains=kword) #icontains seria el 'like' de SQL

        return resultado

    def buscar_autor2(self, kword):

        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword) #Funcion para buscar el  autor por nombre o por apellido
        )
        #where nombre like 'kword' or apellido like 'kword' el | hace referencia al 'or' de SQL
        return resultado
    
    def buscar_autor3(self, kword):

        resultado = self.filter(
            nombre__icontains=kword 
        ).exclude( #exlude en sql seria 'NOT ='
            Q(edad=20) | Q(edad=18)
        ) 

        #Se puede remplazar el exclude por el filter, y seria un filtro sobre otro filtro
        
        return resultado
    
    def buscar_autor4(self,kword):

        resultado = self.filter( #el and de sql seria ' , '
            edad__gt=39, #gt = greather
            edad__lt=50 #lt = lower
        ).order_by('apellido','nombre','edad')#ordery by sql

        return resultado
