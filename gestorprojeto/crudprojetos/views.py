# -*- coding: UTF-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestorprojeto.crudprojetos import manutencaoprojeto
from gestorprojeto.crudprojetos.models import Projetos

@api_view(['POST'])
def novoProjeto(request):
    retorno = manutencaoprojeto.novoProjeto(request)
    
    if type(retorno) is Projetos:
        return Response('Projeto criado com sucesso!', status=status.HTTP_201_CREATED)
    else:
        return Response('Erro ao criar projeto!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarProjeto(request):
    retorno = manutencaoprojeto.listarProjeto(request)
    if retorno is not None:
        return Response(retorno, status=status.HTTP_200_OK)
        
@api_view(['DELETE'])
def deletarProjeto(request, id):
    retorno = manutencaoprojeto.deletarProjetos(request, id)
    if retorno:
        return Response('Projeto deletado com sucesso!', status=status.HTTP_200_OK)
    else:
        return Response('Erro na remoção do Projeto!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def alterarProjeto(request):
    retorno  = manutencaoprojeto.alterarProjetos(request)
    if type(retorno) is Projetos:
        return Response('Projeto alterado com sucesso!', status=status.HTTP_200_OK)
    else:
        return Response('Erro ao alterar projeto!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def buscarProjetoPorId(request, id):
    retorno = manutencaoprojeto.buscarProjetoPorId(request, id)
    if retorno is not None:
        return Response(retorno, status=status.HTTP_200_OK)
    else:
        return Response(retorno, status=status.HTTP_400_BAD_REQUEST)