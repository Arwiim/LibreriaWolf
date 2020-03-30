from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list_libros/', views.ListaLibros.as_view(), name="lista-libros"),
    path('list_libros2/', views.ListaLibros2.as_view(), name="lista-libros2"),
    path('libro_detalle/<pk>/', views.LibroDetailView.as_view(), name="libro-detalle"),
]


