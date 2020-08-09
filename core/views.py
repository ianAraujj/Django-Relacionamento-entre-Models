# rest_framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

# core
from core.serializers import AlunoSerializer
from core.models import Aluno


class Alunos(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = AlunoSerializer

    def get(self, request, format=None):
        queryset = Aluno.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        pass

""" class ObterAluno(APIView):
    serializer_class = AlunoSerializer

    def get_queryset(self):
        
        #print(self.request.method)

        matricula = self.request.GET.get('matricula', None)

        return Aluno.objects.filter(matricula=matricula)

class AlteraAluno(APIView):

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

        return aluno """