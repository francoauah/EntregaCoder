from django.urls import path
from . views import home, hija1, plantilla, left_sidebar

urlpatterns = [
    path('', home, name='inicio' ),
    path('hija1/', hija1, name='hija1' ),
    path('plantilla/', plantilla, name='plantilla' ),
    path('left_sidebar/', left_sidebar, name='left_sidebar')
]
