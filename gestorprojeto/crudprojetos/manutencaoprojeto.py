from gestorprojeto.crudprojetos.models import Projetos
from gestorprojeto.crudprojetos.serializers import ProjetoSerializer
from django.template.context_processors import request


def novoProjeto(request):
    nomeProjeto = request.data['nomeProjeto']
    descricaoProjeto = request.data['descricaoProjeto']
    
    if nomeProjeto != '' and descricaoProjeto != '':
        projeto = Projetos()
        projeto.nomeProjeto = nomeProjeto
        projeto.descricaoProjeto = descricaoProjeto
        projeto.save()
        return projeto
    else:
        return 'Informe todos os campos para criar um projeto!'

def listarProjeto(request):
    projetos = Projetos.objects.all()
    #projetos = Projetos.objects.get(pk=1)
    #cursos = Course.objects.all()
    serializer = ProjetoSerializer(projetos, many=True)
    return serializer.data

def deletarProjetos(request, id):
    projeto = Projetos.objects.get(pk=id)
    if projeto is not None:
        projeto.delete()
        deletado = True
        return deletado
    else:
        deletado = False
        return deletado

def alterarProjetos(request):
    id = request.data['id']
    nomeProjeto = request.data['nomeProjeto']
    descricaoProjeto = request.data['descricaoProjeto']
    projeto = Projetos()
    projeto = Projetos.objects.get(pk=id)
    if projeto is not None:
        projeto.nomeProjeto = nomeProjeto
        projeto.descricaoProjeto = descricaoProjeto
        projeto.save()
        return projeto
    else:
        return 'Erro ao alterar o projeto!'

def buscarProjetoPorId(request, id):
    projeto = Projetos.objects.get(pk=id)
    if projeto is not None:
        serializer = ProjetoSerializer(projeto)
        return serializer.data
    else:
        return 'Erro ao buscar projeto pelo id!'
        