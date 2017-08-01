from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projetos/', include('gestorprojeto.crudprojetos.urls')),
    #url(r'^conta/', include('simplemooc.accounts.urls')),
]
