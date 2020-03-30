from django.shortcuts import render

from django.views.generic import ListView
#Modelos local
from .models import Autores
# Create your views here.

class ListAutores(ListView):
    context_object_name = "lista_autores"
    template_name = "autores/lista_autores.html"

    def get_queryset(self):
        
        """return Autores.objects.all()""" #el manager seria ALL que retorna todas las funciones de manager.
        palabra_clave = self.request.GET.get("kword",'')#no puede tener un valor None el get, por eso va el ''

        """return Autores.objects.listar_autores()""" #Llamo a la funcion listar del manager. esto lista todos los autores

        return Autores.objects.buscar_autor4(palabra_clave) #paso como parametro la variable palabra_clave que recoje el dato del html