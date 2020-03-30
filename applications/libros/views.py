from django.shortcuts import render

from django.views.generic import ListView, DetailView
#Modelos local
from .models import Libros
# Create your views here.

class ListaLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libros/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        #fecha1
        f1 = self.request.GET.get("fecha1",'')
        #fecha2
        f2 = self.request.GET.get("fecha2",'')

        if f1 and f2:
            return Libros.objects.listar_libros2(palabra_clave,f1,f2)
        else:
            return Libros.objects.listar_libros(palabra_clave)


class ListaLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libros/lista2.html'

    def get_queryset(self):
        return Libros.objects.listar_libros_categorias(4)


class LibroDetailView(DetailView): #ver template, el detailView no recibe metodo POST
    model = Libros
    template_name = "libros/detalle.html" #Se puede acceder al object con el nombre de la tabla 'libros' solo en detailView
