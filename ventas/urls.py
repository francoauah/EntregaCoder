

from django.urls import path

from django.urls import path
from .views import articulo

urlpatterns = [
    path('muebleria/', articulo, name='muebleria' )
]
