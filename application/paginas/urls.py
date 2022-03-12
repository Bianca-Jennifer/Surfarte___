from ast import Index
from django.urls import path
from .views import PaginaInicial, Modelo

urlpatterns = [
    #path('endereço', Minhaview.as_view(), 'nome da url')
    path('', Modelo.as_view(), name = 'Modelo'),
    path('Página Inicial/', PaginaInicial.as_view(), name = 'Página Inicial'),
]