from django.db import models

# Create your models here.


class Aluno(models.Model):
    matricula = models.IntegerField(verbose_name="Matricula", null=False, unique=True)
    nome = models.CharField(verbose_name="Nome do Aluno", null=False,blank=False, max_length=90)
    def __str__(self):
        return self.nome

class Participa(models.Model):
    titulo = models.CharField(verbose_name="Titulo do Projeto", max_length=300)
    ano = models.IntegerField("Ano do Projeto")
    aprovado = models.BooleanField(verbose_name="Aprovado SIM ou NAO", default=False)
    #orientador

    Aluno = models.ManyToManyField(Aluno, verbose_name="Aluno")

    def __str__(self):
        return str(self.ano)

class Seminario(models.Model):
    nome = models.CharField(verbose_name="Nome", null=False,blank=False, max_length=300)

    def __str__(self):
        return self.nome
