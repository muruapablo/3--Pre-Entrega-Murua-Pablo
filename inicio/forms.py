from django import forms
from inicio.models import Camaras
from ckeditor.fields import RichTextFormField
class CrearCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    foto = forms.ImageField(required=False)
   
class BusquedaCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)

class ActualizarCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    foto = forms.ImageField(required=False)
class Meta:
    model = Camaras
    fields = ['marca', 'modelo', 'descripcion', 'anio', 'foto']    
   
class CrearTripodeFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    
class BusquedaTripodeFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)
class CrearMicrofonoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)

class BusquedaMicrofonoFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)