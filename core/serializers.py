from rest_framework import serializers
from core.models import *

class AlunoSerializer(serializers.ModelSerializer):

    class Meta:
        model=Aluno
        fields= ('matricula', 'nome')