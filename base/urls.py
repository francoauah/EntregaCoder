from django.urls import path
from . views import home

urlpatterns = [
    path('', home, name='inicio' ),
    # path('hija1/', hija1, name='hija1' ),
    # path('plantilla/', plantilla, name='plantilla' ),
]
