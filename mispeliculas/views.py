from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *

# Create your views here.

def inicio(request):
    return HttpResponse("Bienvenidos")

def peli(request):
    return HttpResponse("Vista Peliculas")

def serie(request):
    return HttpResponse("Vista Series")

def chapter(request):
    return HttpResponse("Vista Capitulos")


