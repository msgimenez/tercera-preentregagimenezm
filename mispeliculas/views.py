from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *

# Create your views here.

def inicio(request):
    return render(request,'mispeliculas/inicio.html')
    #return HttpResponse("Bienvenidos")

def peli(request):
    #return render(request,'mispeliculas/pelis.html')
    return HttpResponse("Vista Peliculas")

def serie(request):
    return render(request,'mispeliculas/serie.html')
    #return HttpResponse("Vista Series")

def chapter(request):
    return render(request,'mispeliculas/chapter.html')
    #return HttpResponse("Vista Capitulos")


