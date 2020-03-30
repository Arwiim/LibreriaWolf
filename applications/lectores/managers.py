import datetime

from django.db import models
from django.db.models import Q, Count,Avg, Sum #Sentencias de tipo 'or', y count, y Promedio

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