from django.db import models
from ckeditor.fields import RichTextField

class Camaras(models.Model):
    marca = models.CharField (max_length=30)
    modelo = models.CharField (max_length=30)
    descripcion = RichTextField()
    anio = models.IntegerField()
    def __str__(self):
        return f' {self.id} - {self.marca} - {self.modelo} - {self.descripcion} - {self.anio}' 
    
class Tripode(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f' {self.marca} - {self.modelo} - {self.descripcion}'

class Microfono(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return f' {self.marca} - {self.modelo} - {self.descripcion}'    