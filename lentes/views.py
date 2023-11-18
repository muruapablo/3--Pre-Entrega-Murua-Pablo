from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.views.generic.detail import DetailView
from lentes.models import Lentes
from django.urls import reverse_lazy

class ListadoLentes(ListView):
    model = Lentes
    context_object_name = 'Listado_de_Lentes'
    template_name = 'lentes/lentes.html'

class CrearLentes(CreateView):
    model = Lentes
    template_name = "lentes/crear_lentes.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('lentes')


class ActualizarLentes(UpdateView):
    model = Lentes
    template_name = "lentes/actualizar_lentes.html"
    fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('lentes')


class DetalleLentes(DetailView):
    model = Lentes
    template_name = "lentes/detalle_lente.html"


class EliminarLentes(DeleteView):
    model = Lentes
    template_name = "lentes/eliminar_lentes.html"
    success_url = reverse_lazy('lentes')     