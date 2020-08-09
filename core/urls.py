from django.urls import path
from core.views import ListarAlunos, ObterAluno, AlteraAluno

urlpatterns = [
    path('alunos/', ListarAlunos.as_view(), name="listar-alunos"),
    path('aluno/',ObterAluno.as_view(), name="Obter-aluno"),
    path('aluno/alterar', AlteraAluno.as_view(), name="Alterar Aluno")
]
