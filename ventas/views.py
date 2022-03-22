# from django.http import HttpResponse
from django.shortcuts import render
from .models import Articulos, Pedidos, Clientes
from .forms import ArticuloFormulario, PedidosFormulario, ClientesFormulario, ArticuloBusqueda

#Enter your views here.

# def articulo(request):
#     art=Articulos(Nombre='mesa', Seccion='muebles', PrecioArticulo=20000)
#     art.save()
#     return HttpResponse(f"Se agrego un nuevo elemento al catalogo: {art.Nombre}, con un precio de {art.PrecioArticulo}")

def crearArticulo(request):

    if request.method =='POST':
        form = ArticuloFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            articulo=Articulos(Nombre=data['Nombre'], Seccion=data['Seccion'], PrecioArticulo=data['PrecioArticulo'])
            articulo.save()
            return render(request,'base/index.html', {})
            
    form = ArticuloFormulario()
    return render(request,'ventas/crearArticulo.html',{"form":form})



def buscarArticulo(request):
    

    nombreAbuscar = request.GET.get('Nombre',None)

    if nombreAbuscar is not None:
        articulos = Articulos.objects.filter(Nombre__icontains=nombreAbuscar)
    else:
        articulos = Articulos.objects.all()
    articulos = None
    form = ArticuloBusqueda()
    return render(request,'ventas/busquedaArticulo.html',{"form":form, 'articulos':articulos })



















def crearPedido(request):

    if request.method =='POST':
        form = PedidosFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            articulo=Pedidos(NumeroDePedido=data['NumeroDePedido'], Fecha=data['Fecha'], Entregado=data['Entregado'])
            articulo.save()
            return render(request,'base/index.html', {})
            
    form = PedidosFormulario()
    return render(request,'ventas/crearPedido.html',{"form":form})


def crearClientes(request):

    if request.method =='POST':
        form = ClientesFormulario(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            articulo=Clientes(Nombre=data['Nombre'], Direccion=data['Direccion'], Email=data['Email'], Telefono=data['Telefono'])
            articulo.save()
            return render(request,'base/index.html', {})
            
    form = ClientesFormulario()
    return render(request,'ventas/crearClientes.html',{"form":form})






    # # print(request.method)
    # if request.method == 'POST':
    #     art = Articulos(request.POST['nombre'], request.POST['seccion'])
    #     art.save()
    #     return render(request,'ventas/formulario_busqueda.html',{'art':art})
 
    # return render(request,'ventas/formulario_busqueda.html',{})