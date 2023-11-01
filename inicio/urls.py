from django.urls import path
from inicio.views import inicio, camaras, crear_camara
urlpatterns = [
    path('',inicio, name='inicio'),
    path('camaras/',camaras, name='camaras'), 
    path('camaras/crear/', crear_camara, name='crear_camaras')
]
