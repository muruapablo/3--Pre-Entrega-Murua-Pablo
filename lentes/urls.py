from django.urls import path
from lentes.views import ListadoLentes,CrearLentes,DetalleLentes,ActualizarLentes,EliminarLentes

urlpatterns = [
    path('lentes/', ListadoLentes.as_view(), name='lentes'),
    path('lentes/crear/', CrearLentes.as_view(), name='crear_lentes'),
    path('lentes/<int:pk>/', DetalleLentes.as_view(), name='detalle_lentes'),
    path('lentes/<int:pk>/actualizar/', ActualizarLentes.as_view(), name='actualizar_lentes'),
    path('lentes/<int:pk>/eliminar/', EliminarLentes.as_view(), name='eliminar_lentes'),
      
]