from django.db import models

# Create your models here.
class Professor(models.Model):
    SIM = 'SIM'
    NAO = 'NÃO'
    yes_or_no = [(SIM, 'SIM'), (NAO, 'NÃO') ]

    nome = models.CharField(max_length=50)
    metodologia = models.CharField(max_length=50)
    email = models.EmailField()
    aula = models.CharField(
        max_length=3,
        choices=yes_or_no,
        verbose_name='Aulas particulares?'
    )
    def __str__(self):
        return "{} ({})".format(self.nome, self.metodologia)

    

class Plano(models.Model):
    MANHA = 'MANHÃ'
    TARDE = 'TARDE'
    NOITE = 'NOITE'
    FLEXIVEL = 'FLEXÍVEL'
    momento = [(MANHA, 'MANHÃ'), (TARDE, 'TARDE'), (NOITE, 'NOITE'), (FLEXIVEL, 'FLEXÍVEL') ]

    nome = models.CharField(max_length=50)
    preco = models.CharField(verbose_name="Preço", max_length=100)
    dias = models.IntegerField(verbose_name="Quantidade de dias na semana")  
    horario = models.CharField(
        max_length=10,
        choices=momento,
        verbose_name='Horário'
    ) 
    detalhes = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.nome, self.preco)

class Avaliacao(models.Model):
    autor = models.CharField(max_length=50)
    plano = models.ForeignKey(Plano, on_delete=models.PROTECT)
    comentario = models.TextField(verbose_name='Comentário')

    def __str__(self):
        return "{} ({})".format(self.autor, self.comentario)
