from django.urls import path
from mispeliculas import views

urlpatterns = [
    path('',views.inicio),
    path('peli',views.peli,name= "Peliculas"),
    path('serie',views.serie,name= "Series"),
    path('chapter',views.chapter,name= "Capitulos"),


]