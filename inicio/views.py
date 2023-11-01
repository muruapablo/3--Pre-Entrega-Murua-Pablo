from django.shortcuts import render
from inicio.models import Camaras

def inicio(request):
   
    return render(request, 'inicio/inicio.html', {})

def camaras(request):
    camara = Camaras(marca='Sony', modelo = 'A7 III', descripcion = 'Camara full frame', anio =2022)
    camara.save()

    return render(request, 'inicio/camaras.html', {'camara': camara}) 


# def crear_Camaras(request):
#     return 