from django.shortcuts import render
from rest_framework import generics
from core.serializers import AlunoSerializer
from core.models import Aluno

class ListarAlunos(generics.ListCreateAPIView):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ObterAluno(generics.ListCreateAPIView):
    serializer_class = AlunoSerializer

    def get_queryset(self):
        
        #print(self.request.method)

        matricula = self.request.GET.get('matricula', None)

        return Aluno.objects.filter(matricula=matricula)

class AlteraAluno(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = AlunoSerializer

    def get_queryset(self):
        matricula = self.request.GET.get('matricula', None)
        novo_nome = self.request.GET.get('nome', None)

        print("aoooooooooooooooo")
        print(matricula)
        print(novo_nome)

        aluno = Aluno.objects.filter(matricula=matricula)
        aluno.nome = novo_nome
        aluno.save()

        return aluno