import email
from django.db import models

# Create your models here.

class Clientes(models.Model):
    Nombre=models.CharField(max_length=30)
    Direccion=models.CharField(max_length=30)
    Email=models.EmailField()
    Telefono=models.CharField(max_length=20)


class Articulos(models.Model):
    Nombre=models.CharField(max_length=50)
    Seccion=models.CharField(max_length=50)
    PrecioArticulo=models.IntegerField()


class Pedidos(models.Model):
    NumeroDePedido=models.IntegerField()
    Fecha=models.DateField()
    Entregado=models.BooleanField()