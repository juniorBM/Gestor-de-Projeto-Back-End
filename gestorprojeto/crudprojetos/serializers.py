from rest_framework import serializers
from gestorprojeto.crudprojetos.models import Projetos

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = ('nomeProjeto','id', 'descricaoProjeto',)
