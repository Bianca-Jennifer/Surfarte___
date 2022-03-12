from ast import cmpop
from django.contrib import admin
from .models import Professor, Plano, Avaliacao
#Importar classes

# Register your models here.
admin.site.register(Professor)
admin.site.register(Plano)
admin.site.register(Avaliacao)
