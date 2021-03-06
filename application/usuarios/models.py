from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
    cpf = models.CharField(max_length=20, null=True)
    telefone = models.CharField(max_length=20, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)