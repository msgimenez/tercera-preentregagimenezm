from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *

# Create your views here.

def serie(self):
    serie = Serie(titulo="The Flash",genero="Ciencia Ficcion",temporadas=4)
    serie.save()
    documentoDeTexto=f"--> Serie:{serie.titulo} Genero:{serie.genero} Temporadas:{serie.temporadas}"
    return HttpResponse(documentoDeTexto)

def peli(self):
    peli = Peliculas(titulo="Titanic",genero="Drama",director="James Cameron")
    peli.save()
    documentoDeTexto=f"--> Peliculas:{peli.titulo} Genero:{peli.genero} Director:{peli.director} Descargada: {peli.descargada}"
    return HttpResponse(documentoDeTexto)



