from django.db import models

class Projetos(models.Model):
    nomeProjeto = models.CharField('Nome do Projeto', max_length=50)
    descricaoProjeto = models.TextField('Descricao do Projeto')
    
    def __str__(self):
        return self.nomeProjeto