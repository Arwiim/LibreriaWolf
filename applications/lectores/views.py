from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
# Create your views here.

from .models import Prestamos
from .forms import PrestamoForm, MultiplePrestamoForm

class RegistrarPrestamo(FormView):
    template_name = 'lectores/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self,form):

        """Prestamos.objects.create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestame=date.today(),
            devuelto=False
        )"""#Una forma de hacerlo

        prestamo = Prestamos(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']
        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistrarPrestamo,self).form_valid(form)

#----------------------------------------#

class AddPrestamo(FormView):
    template_name = 'lectores/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self,form):

        obj, created = Prestamos.objects.get_or_create( #Funcion para ver si el objecto esta ya creado y en caso contrario lo crea con esos valores

            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto= False,
            defaults={
                'fecha_prestamo' : date.today()


            }
        )

        if created:
            return super(AddPrestamo,self).form_valid(form)
        else:
            return HttpResponseRedirect('/')#en caso de que este registrado lo manda a url de error
    
class AddMultiPrestamo(FormView):
    template_name = 'lectores/add_multiple_prestame.html'
    form_class = MultiplePrestamoForm
    success_url = '.'

    def form_valid(self,form):
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])

        prestamos = []

        for l in form.cleaned_data['libros']:
            prestamo = Prestamos(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo=date.today(),
                devuelto= False, 
            )
            prestamos.append(prestamo)

        Prestamos.objects.bulk_create( #va crear registros pero a partir de la lista
            prestamos
        )

        return super(AddMultiPrestamo,self).form_valid(form)