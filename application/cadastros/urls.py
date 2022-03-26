from ast import Index
from django.urls import path

#Importar views
from .views import  ProfessorCreate, PlanoCreate, AvaliacaoCreate
from .views import  ProfessorUpdate, PlanoUpdate, AvaliacaoUpdate
from .views import  ProfessorDelete, PlanoDelete, AvaliacaoDelete
from .views import  ProfessorList,   PlanoList,   AvaliacaoList, MinhaAvaliacaoList


urlpatterns = [
    path('cadastrar/professor/', ProfessorCreate.as_view(), name="cadastrar-professor"),
    path('cadastrar/plano/', PlanoCreate.as_view(), name="cadastrar-plano"),   
    path('cadastrar/avaliacao/', AvaliacaoCreate.as_view(), name="cadastrar-avaliacao"),   

    path('editar/professor/<int:pk>', ProfessorUpdate.as_view(), name='editar-professor'),
    path('editar/plano/<int:pk>', PlanoUpdate.as_view(), name='editar-plano'),
    path('editar/avaliacao/<int:pk>', AvaliacaoUpdate.as_view(), name='editar-avaliacao'),

    path('excluir/professor/<int:pk>', ProfessorDelete.as_view(), name='excluir-professor'),
    path('excluir/plano/<int:pk>', PlanoDelete.as_view(), name='excluir-plano'),
    path('excluir/avaliacao/<int:pk>', AvaliacaoDelete.as_view(), name='excluir-avaliacao'),

    path('exibir/professor/', ProfessorList.as_view(), name='exibir-professor'),
    path('exibir/plano/', PlanoList.as_view(), name='exibir-plano'),
    path('exibir/avaliacao/', AvaliacaoList.as_view(), name='exibir-avaliacao'),
    path('exibir/minha_avaliacao/', MinhaAvaliacaoList.as_view(), name='exibir-minha_avaliacao'),
]