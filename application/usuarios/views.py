from re import U
from unicodedata import name
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group #dá pra importar grupo
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Perfil

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('Página Inicial')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Registro de Usuário" 
        return context

    def form_valid(self, form):
        #Antes do super, não foi criado o objeto, nem salvo no banco
        grupo=get_object_or_404(Group, name="visitante")
        url = super().form_valid(form)
        #Depois do super, o objeto está criado
        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return  url             

class PerfilUpdate(UpdateView):
    template_name = "cadastros/form.html"
    model = Perfil
    fields = ['nome_completo', 'cpf', 'telefone']
    success_url = reverse_lazy('Página Inicial')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

              
