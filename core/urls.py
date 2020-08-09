from django.urls import path
from core.views import Alunos

urlpatterns = [
    path('alunos/', Alunos.as_view(), name="listar-alunos"),

]
