from django.urls import path
from inicio.views import inicio,camaras
urlpatterns = [
    path('',inicio, name='inicio'),
    path('camaras/',camaras, name='camaras'), 
]
