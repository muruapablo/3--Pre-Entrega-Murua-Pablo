from django import forms
 
class CrearCamaraFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    modelo = forms.CharField (max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()