from dataclasses import fields
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Professor, Plano, Avaliacao
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

# Create your views here.
class ProfessorCreate(GroupRequiredMixin, CreateView):
    group_required = u"administrador"
    model = Professor
    fields = ['nome', 'metodologia', 'email', 'aula']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')

class PlanoCreate(GroupRequiredMixin, CreateView):
    group_required = u"administrador"
    model = Plano
    fields = ['nome', 'preco', 'dias', 'horario', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')  

class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['autor', 'plano', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')            

# UPDATE #
class ProfessorUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"administrador"
    model = Professor
    fields = ['nome', 'metodologia', 'email', 'aula']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')

class PlanoUpdate(GroupRequiredMixin, UpdateView):
    group_required = u"administrador"
    model = Plano
    fields = ['nome', 'preco', 'dias', 'horario', 'detalhes']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')      

class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['autor', 'plano', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial')  

# DELETE #
class ProfessorDelete(GroupRequiredMixin, DeleteView):
    group_required = u"administrador"
    model = Professor
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('Página Inicial')  

class PlanoDelete(GroupRequiredMixin, DeleteView):
    group_required = u"administrador"
    model = Plano
    template_name = 'cadastros/form-excluir.html' 
    success_url = reverse_lazy('Página Inicial')    

class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
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

