from django.contrib import admin

from ventas.models import Articulos, Clientes, Pedidos

admin.site.register(Clientes)

admin.site.register(Articulos)

admin.site.register(Pedidos)