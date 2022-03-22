from django.urls import path
from .views import crearArticulo, crearClientes, crearPedido, buscarArticulo
urlpatterns = [
    
    path('articulo/crear/', crearArticulo, name = 'crearArticulo'),
    path('articulo/buscar/', buscarArticulo, name = 'buscarArticulo'),
    path('pedido/crear/', crearPedido, name = 'crearPedido'),
    path('cliente/crear/', crearClientes, name = 'crearClientes')
]
