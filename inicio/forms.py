from django import forms
 
class CrearCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class BusquedaCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30, required=False)

class ActualizarCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
   
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