from django.views.generic import TemplateView

# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "pag_inicial.html"

class Modalidades(TemplateView):
    template_name = "modalidades.html"

