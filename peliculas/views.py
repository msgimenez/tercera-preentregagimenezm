from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse('Bienvenido a mis peliculas')

def segunda_vista(request):
    return HttpResponse('<br> Usted puede elegir su pelicula <br> y tambien la serie que prefiera')

def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoTexto = f'Hoy es: <br> {dia}'
    return HttpResponse(documentoTexto)

def mipeli(self,nombre):
    documentoTexto= f'Mi pelicula elegida es: <br> {nombre}'
    return HttpResponse(documentoTexto)

def probandoTemplate(self):
    nom = "Toy Story"
    miseriefav = "The Flash"
    listaDeGeneros = ['Drama', 'Comedia', 'Infantil', 'Documental', 'Terror']
    diccionario = {"nombre":nom, "serie":miseriefav, "hoy":datetime.datetime.now(),"generos":listaDeGeneros}
    mihtml = open('C:/Users/msgim/OneDrive/Escritorio/peliculas/peliculas/pelicula-git/peliculas/planillas/template1.html')
    plantilla = Template(mihtml.read())
    mihtml.close()
    miContexto = Context(diccionario)
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
