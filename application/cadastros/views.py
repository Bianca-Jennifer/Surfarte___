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
    fields = ['plano', 'comentario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('Página Inicial') 

    def form_valid(self, form):
        #Antes do super, não foi criado o objeto, nem salvo no banco
        form.instance.autor = self.request.user
        url = super().form_valid(form)
        #Depois do super, o objeto está criado
        return  url             

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

    def get_object(self, queryset=None):
        self.object = Avaliacao.objects.get(pk=self.kwargs['pk'], autor=self.request.user) #kwargs pega o valor que vc digitou na url(:pk)
        return self.object 

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
 

class MinhaAvaliacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    template_name = 'cadastros/listas/minhas_avaliacoes.html' 

    def get_queryset(self):
        self.object_list = Avaliacao.objects.filter(autor=self.request.user)
        return self.object_list 
