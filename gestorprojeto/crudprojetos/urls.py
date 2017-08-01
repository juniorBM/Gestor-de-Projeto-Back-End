from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from gestorprojeto.crudprojetos import views

urlpatterns = [
    url(r'^novo/projeto/$', views.novoProjeto),
    url(r'^listar/projetos/$', views.listarProjeto),
    url(r'^deletar/projeto/(?P<id>\d+)/$', views.deletarProjeto),
    url(r'^alterar/projeto/$', views.alterarProjeto),
    url(r'^buscar/projeto/(?P<id>\d+)/$', views.buscarProjetoPorId),
]

urlpatterns = format_suffix_patterns(urlpatterns)
