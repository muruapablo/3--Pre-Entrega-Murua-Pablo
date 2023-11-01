from django.urls import path
from inicio.views import inicio,camaras
urlpatterns = [
    path('',inicio),
    path('camaras/',camaras), 
]
