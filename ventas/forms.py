from django import forms

class ArticuloFormulario(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Seccion=forms.CharField(max_length=50)
    PrecioArticulo=forms.IntegerField()