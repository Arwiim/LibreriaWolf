from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prestamo/add/', views.RegistrarPrestamo.as_view(), name="prestamo-add"),
    path('prestamo2/add/', views.AddPrestamo.as_view(), name="prestamo2-add"),
    path('prestamo2/multiple/', views.AddMultiPrestamo.as_view(), name="add-multipleprestamo"),

]
