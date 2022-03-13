from dataclasses import fields
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Professor, Plano, Avaliacao
from django.urls import reverse_lazy

# Create your views here.
class ProfessorCreate(CreateView):
    model = Professor
    fields = ['nome', 'metodologia', 'email', 'aula']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')

class PlanoCreate(CreateView):
    model = Plano
    fields = ['nome', 'preco', 'dias', 'horario', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')  

class AvaliacaoCreate(CreateView):
    model = Avaliacao
    fields = ['autor', 'plano', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')            

# UPDATE #
class ProfessorUpdate(UpdateView):
    model = Professor
    fields = ['nome', 'metodologia', 'email', 'aula']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')

class PlanoUpdate(UpdateView):
    model = Plano
    fields = ['nome', 'preco', 'dias', 'horario', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')      

class AvaliacaoUpdate(UpdateView):
    model = Avaliacao
    fields = ['autor', 'plano', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')  

# DELETE #
class ProfessorDelete(DeleteView):
    model = Professor
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('Página Inicial')  

class PlanoDelete(DeleteView):
    model = Plano
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('Página Inicial')    

class AvaliacaoDelete(DeleteView):
    model = Avaliacao
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('Página Inicial') 

# LISTAR #
class ProfessorList(ListView):
    model = Professor
    template_name = 'cadastros/listas/professor.html' 

class PlanoList(ListView):
    model = Plano
    template_name = 'cadastros/listas/plano.html' 

class AvaliacaoList(ListView):
    model = Avaliacao
    template_name = 'cadastros/listas/avaliacao.html'         

