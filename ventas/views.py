from django.http import HttpResponse
from django.shortcuts import render
from ventas.models import Articulos

# Create your views here.

def articulo(request):
    art=Articulos(Nombre='mesa', Seccion='muebles', PrecioArticulo=20000)
    art.save()
    return HttpResponse(f"Se agrego un nuevo elemento al catalogo: {art.Nombre}, con un precio de {art.PrecioArticulo}")