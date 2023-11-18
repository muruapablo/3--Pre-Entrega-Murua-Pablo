from django.urls import path
from inicio.views import inicio,camaras,crear_camara,eliminar_camara,about_me,tripodes,crear_tripode,microfonos,crear_microfono,actualizar_camara,detalle_camara

urlpatterns = [
    path('',inicio, name='inicio'),
    path('camaras/',camaras, name='camaras'), 
    path('camaras/crear/', crear_camara, name='crear_camaras'),
    path('eliminar_camara/<int:camara_id>/',eliminar_camara, name='eliminar_camara'),
    path('camaras/<int:camara_id>/',detalle_camara, name='detalle_camara'),
    path('actualizar_camara/<int:camara_id>/actualizar/', actualizar_camara, name='actualizar_camara'),
    path('about/', about_me, name='about_me'),
    path('tripodes/',tripodes, name='tripodes'), 
    path('tripodes/crear/', crear_tripode, name='crear_tripode'),
    path('microfonos/',microfonos, name='microfonos'), 
    path('microfonos/crear/', crear_microfono, name='crear_microfono'),
]
