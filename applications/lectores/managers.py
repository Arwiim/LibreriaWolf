import datetime

from django.db import models
from django.db.models import Q, Count,Avg, Sum #Sentencias de tipo 'or', y count, y Promedio
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):
    """Procedimiento para prestamos"""

    def libros_promedio_edades(self):
        resultado = self.filter(
            libro__id='1'
        ).aggregate(
            promedio_edad= Avg('lector__edad'),
            suma_edad= Sum('lector__edad')
        )
        return resultado

    
    def num_libros_prestados(self):
        resultado = self.values( #nos devuelve una lista en diccionarios
            'libro' #el group by por la fk
        ).annotate(
            num_prestados = Count('libro'),
            titulo = Lower('libro__titulo'),#agregar al diccionario el titulo
        )

        for r in resultado:
            print(r, r['num_prestados'])
        return resultado