from django.contrib import admin

from .models import Libros,Categorias   
# Register your models here.

admin.site.register(Libros)
admin.site.register(Categorias)