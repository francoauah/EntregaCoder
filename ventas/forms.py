from django import forms

class ArticuloFormulario(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Seccion=forms.CharField(max_length=50)
    PrecioArticulo=forms.IntegerField()

class ArticuloBusqueda(forms.Form):
    Nombre = forms.CharField(max_length=50)




















class PedidosFormulario(forms.Form):
    NumeroDePedido=forms.IntegerField()
    Fecha=forms.DateField()
    Entregado=forms.BooleanField(required=False)

class ClientesFormulario(forms.Form):
    Nombre=forms.CharField(max_length=30)
    Direccion=forms.CharField(max_length=30)
    Email=forms.EmailField()
    Telefono=forms.CharField(max_length=20)


