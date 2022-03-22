from django.urls import path
from .views import crearArticulo, crearClientes, crearPedido, buscarArticulo
urlpatterns = [
    # path('muebleria/', articulo, name='muebleria' ),
    path('articulo/crear/', crearArticulo, name = 'crearArticulo'),
    path('articulo/buscar/', buscarArticulo, name = 'buscarArticulo'),
    # path('busqueda_articulos/', buscarArticulos), 
    # path('buscar/', buscar, name = 'buscarArticulo'),
    path('pedido/crear/', crearPedido, name = 'crearPedido'),
    path('cliente/crear/', crearClientes, name = 'crearClientes')
]
