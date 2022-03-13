from ast import Index
from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    #path('endereço', Minhaview.as_view(), 'nome da url')
    path('', PaginaInicial.as_view(), name = 'Página Inicial'),
    
]