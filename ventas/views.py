from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulos
from .forms import ArticuloFormulario

#Enter your views here.

def articulo(request):
    art=Articulos(Nombre='mesa', Seccion='muebles', PrecioArticulo=20000)
    art.save()
    return HttpResponse(f"Se agrego un nuevo elemento al catalogo: {art.Nombre}, con un precio de {art.PrecioArticulo}")

def formulario_busqueda(request):

    if request.method =='POST':
        form = ArticuloFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            articulo=Articulos(Nombre=data['Nombre'], Seccion=data['Seccion'], PrecioArticulo=data['PrecioArticulo'])
            articulo.save()
            return render(request,'base/index.html', {})
            
    form = ArticuloFormulario()
    return render(request,'ventas/formulario_busqueda.html',{"form":form})

    # # print(request.method)
    # if request.method == 'POST':
    #     art = Articulos(request.POST['nombre'], request.POST['seccion'])
    #     art.save()
    #     return render(request,'ventas/formulario_busqueda.html',{'art':art})
 
    # return render(request,'ventas/formulario_busqueda.html',{})