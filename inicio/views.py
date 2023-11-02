from django.shortcuts import render, redirect
from inicio.models import Camaras
from inicio.forms import CrearCamaraFormulario, BusquedaCamaraFormulario

def inicio(request):
   
    return render(request, 'inicio/inicio.html', {})

def camaras(request):
    
    Listado_de_Camaras = Camaras.objects.all()
    
    formulario = BusquedaCamaraFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar= formulario.cleaned_data.get('marca')
        Listado_de_Camaras = Camaras.objects.filter(marca__icontains=marca_a_buscar)
    
  

    return render(request, 'inicio/camaras.html',{'Listado_de_Camaras': Listado_de_Camaras}) 


def crear_camara(request):
    
    # if request.method == 'POST': 
    #     marca = request.POST.get('marca')
    #     modelo = request.POST.get('modelo') 
    #     descripcion = request.POST.get('descripcion')
    #     anio = request.POST.get('anio')     
    
    #     camara = Camaras(marca=marca, modelo=modelo, descripcion=descripcion, anio=anio)
    #     camara.save()
    if request.method == 'POST':
        formulario = CrearCamaraFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo') 
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')     
    
            camara = Camaras(marca=marca, modelo=modelo, descripcion=descripcion, anio=anio)
            camara.save()
            
            return redirect('camaras')
        else:
            return render(request, 'inicio/crear_camaras.html', {'formulario':formulario})          
        
        
    
    formulario = CrearCamaraFormulario()
    return render(request, 'inicio/crear_camaras.html', {'formulario':formulario}) 