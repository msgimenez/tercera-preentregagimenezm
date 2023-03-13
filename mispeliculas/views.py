from django.shortcuts import render
from django.http import HttpResponse
from mispeliculas.models import *
from mispeliculas.forms import pelisformulario

# Create your views here.

def inicio(request):
    return render(request,'mispeliculas/inicio.html')
    #return HttpResponse("Bienvenidos")

def pelis(request):
    return render(request,'mispeliculas/pelis.html')
    #return HttpResponse("Vista Peliculas")

def serie(request):
    return render(request,'mispeliculas/serie.html')
    #return HttpResponse("Vista Serie")

def chapter(request):
    return render(request,'mispeliculas/chapter.html')
    #return HttpResponse("Vista Capitulos")


"""def pelisformulario(request):
    if request.method == 'POST':
         peli = Peliculas(request,'POST'['titulo'],(request,'POST'['genero']),(request,'POST'['director']),(request,'POST'['fecha']))
         peli.save()
         return render(request, 'mispeliculas/inicio.html') 
    
    return render(request,'mispeliculas/pelisformulario.html')"""

"""def seriesformulario(request):
    return render(request,'mispeliculas/seriesformulario.html')

def chapterformulario(request):
    return render(request,'mispeliculas/chapterformulario.html')"""

def pelisFormulario(request):
    if request.method == 'POST':
        miFormulario = pelisformulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            peli = Peliculas(titulo=informacion['titulo'],genero=informacion['genero'], director=informacion['director'])
            peli.save()
            return render(request, "mispeliculas/inicio.html")
    else:
        miFormulario= pelisformulario()
    
    return render(request,"mispeliculas/pelisformulario.html", {"miFormulario":miFormulario})


    
