import datetime

from django.db import models
from django.db.models import Q, Count #Sentencias de tipo 'or', y count

class LibrosManager(models.Manager):
    """ managers para el modelo libros """
    
    def listar_libros(self,kword):

        resultado = self.filter(
            titulo__icontains=kword,#icontains seria el '[% kword %]' de SQL
            fecha__range=('2000-01-01','2020-03-01')#Rango para fechas entre Y entre
        ) 

        return resultado

    def listar_libros2(self,kword,fecha1,fecha2): #Chrome ya manda el formato MM-DD-YYYY

        date1 = datetime.datetime.strptime(fecha1,"%Y-%m-%d").date() #conver fecha a especifica, 2 digitos en minuscula, 4 en mayusucla
        date2 = datetime.datetime.strptime(fecha2,"%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,#icontains seria el '[% kword %]' de SQL
            fecha__range=(date1,date2)#Rango para fechas entre Y entre
        ) 

        return resultado
    
    def listar_libros_categorias(self,categoria):

        return self.filter(
            categoria__id=categoria #Me va a traer los libros que pertenecen a la categoria que le voy a pasar por parametro
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autorr):
        libro = self.get(id=libro_id) #recuperar el id del libro
        libro.autor.add(autorr) #Agregar autor desde el paramentro
        """libro.autor.remove(autorr)""" #para eliminar
        return libro

    """def libros_num_prestamos(self):
        resultado = self.aggregate( #Devuelve un diccionario + la operacion se usa mas que todo cuando requeris 1 solo valor
            num_prestamos = Count('libro_prestamo')
        )
        return []"""
    
    def num_libros_prestados(self):
        resultado = self.annotate(
            num_prestados = Count('libro_prestamo')
        )

        for r in resultado:
            print(r, r.num_prestados)
        return resultado
        

class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autor__id=autor  #relacion de categoria > libro > autor
        ).distinct()# el famoso distinct, no va a repetetir las categorias por los libros en la misma categoria
    
    def listar_categorias_libros(self):

        resultado = self.annotate(#deuvuelve una consulta query set + la operacion
            num_libros=Count('categoria_libro') #Hacer el count de sql de la FK de categorias para contar libros por categoria
        )
        #Solo para verificar en la shell
        for r in resultado:
            print('************')
            print(r, r.num_libros)
        #--------------------------------
        return resultado