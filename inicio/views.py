from django.shortcuts import render, redirect
from inicio.models import Camaras,Tripode, Microfono
from inicio.forms import CrearCamaraFormulario, BusquedaCamaraFormulario,CrearTripodeFormulario, BusquedaTripodeFormulario, CrearMicrofonoFormulario, BusquedaMicrofonoFormulario 

def inicio(request):
   
    return render(request, 'inicio/inicio.html', {})

def camaras(request):
    
    # Listado_de_Camaras = Camaras.objects.all()
    
    formulario = BusquedaCamaraFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar= formulario.cleaned_data.get('marca')
        Listado_de_Camaras = Camaras.objects.filter(marca__icontains=marca_a_buscar)
    
  
    formulario = BusquedaCamaraFormulario()
    return render(request, 'inicio/camaras.html', {'formulario': formulario, 'Listado_de_Camaras': Listado_de_Camaras})


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
    
            camara = Camaras(marca=marca.lower(), modelo=modelo, descripcion=descripcion, anio=anio)
            camara.save()
            
            return redirect('camaras')
        else:
            return render(request, 'inicio/crear_camaras.html', {'formulario':formulario})          
        
        
    
    formulario = CrearCamaraFormulario()
    return render(request, 'inicio/crear_camaras.html', {'formulario':formulario})
    
    formulario = CrearCamaraFormulario()
    return render(request, 'inicio/crear_camaras.html', {'formulario': formulario})

def eliminar_camara(request, camara_id):
    camara_a_eliminar = Camaras.objects.get(id=camara_id)
    camara_a_eliminar.delete()
    return redirect('camaras')


def about_me(request):
    return render(request, 'inicio/about_me.html')


def tripodes(request):
    Listado_de_Tripodes = Tripode.objects.all()
    
    formulario = BusquedaTripodeFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        Listado_de_Tripodes = Tripode.objects.filter(marca__icontains=marca_a_buscar)
    
    return render(request, 'inicio/tripodes.html', {'Listado_de_Tripodes': Listado_de_Tripodes}) 

def crear_tripode(request):
    if request.method == 'POST':
        formulario = CrearTripodeFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo') 
            descripcion = info_limpia.get('descripcion')    
    
            tripode = Tripode(marca=marca, modelo=modelo, descripcion=descripcion)
            tripode.save()
            
            return redirect('tripodes')
    
    else:
        formulario = CrearTripodeFormulario()
        
    return render(request, 'inicio/crear_tripodes.html', {'formulario': formulario})

def microfonos(request):
    Listado_de_Microfonos = Microfono.objects.all()
    
    formulario = BusquedaMicrofonoFormulario(request.GET)
    if formulario.is_valid():
        marca_a_buscar = formulario.cleaned_data.get('marca')
        Listado_de_Microfonos = Microfono.objects.filter(marca__icontains=marca_a_buscar)
    
    return render(request, 'inicio/microfonos.html', {'Listado_de_Microfonos': Listado_de_Microfonos}) 

def crear_microfono(request):
    if request.method == 'POST':
        formulario = CrearMicrofonoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo') 
            descripcion = info_limpia.get('descripcion')
                 
            microfono = Microfono(marca=marca, modelo=modelo, descripcion=descripcion)
            microfono.save()
            
            return redirect('microfonos')
    
    else:
        formulario = CrearMicrofonoFormulario()
        
    return render(request, 'inicio/crear_microfono.html', {'formulario': formulario})


