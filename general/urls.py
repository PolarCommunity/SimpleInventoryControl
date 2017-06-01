from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^usuario/', Register, name ="Register"),
    url(r'^cerrar/', Logout, name ="Logout"),
    url(r'^sede/usuario/lista/(?P<pk>\d+)$', lista_sede_usuario_super, name ="lista_sede_usuario_super"),
    url(r'^sede/lista/', lista_sede, name ="lista_sede"),
    url(r'^sede/crear/', crear_sede, name ="crear_sede"),
    url(r'^sede/actualizar/', actualizar_sede, name ="actualizar_sede"),
    url(r'^articulo/lista/', lista_articulo, name ="lista_articulo"),
    url(r'^articulo/crear/', crear_articulo, name ="crear_articulo"),
    url(r'^articulo/actualizar/', actualizar_articulo, name ="actualizar_articulo"),
    url(r'^articulo/sede/lista/(?P<pk>\d+)$', lista_sede_articulo_super, name ="lista_sede_articulo_super"),
    url(r'^articulo/sede/lista/', lista_sede_articulo, name ="lista_sede_articulo"),
    url(r'^', Home, name ="Home"),

]
