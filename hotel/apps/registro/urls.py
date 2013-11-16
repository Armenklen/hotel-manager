from django.conf.urls import patterns, include, url
from views import login,exito,autenticacion,bienvenido

urlpatterns = patterns('',
    #url(r'^index/',preguntas),
    url(r'^$',login),
    url(r'^registro/exito/$',exito),
    url(r'^registro/login/$',autenticacion),
    url(r'^usuario/bienvenido/$',bienvenido),
)
