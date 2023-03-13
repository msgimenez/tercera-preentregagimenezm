from django.urls import path
from mispeliculas import views

urlpatterns = [
    path('inicio',views.inicio, name="Inicio"),
    path('pelis',views.pelis,name= "Peliculas"),
    path('serie',views.serie,name= "Series"),
    path('chapter',views.chapter,name= "Capitulos"),
    path('pelisformulario',views.pelisformulario, name="PelisFormulario"),

   



]