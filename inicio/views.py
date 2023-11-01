from django.shortcuts import render
from inicio.models import Camaras

def inicio(request):
    return render(request, 'inicio.html',{})

def Camaras(request):
    Camaras = Camaras(marca='Sony', descripcion='A7II - Camara full frame', anio=2022)
    Camaras.save()

    return render(request, 'inicio/Camaras.html' ,{'Camaras': Camaras}) 


def crear_Camaras(request):
    return 