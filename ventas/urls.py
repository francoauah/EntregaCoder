from django.urls import path
from .views import articulo, formulario_busqueda

urlpatterns = [
    path('muebleria/', articulo, name='muebleria' ),
    path('busqueda/', formulario_busqueda, name = 'formulario_busqueda')
]
