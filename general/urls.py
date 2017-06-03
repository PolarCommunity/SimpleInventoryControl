from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sede/usuario/lista/(?P<pk>\d+)$', lista_sede_usuario_super, name ="lista_sede_usuario_super"),
    url(r'^sede/lista/$', lista_sede.as_view(), name ="lista_sede"),
    url(r'^sede/lista/([\w-]+)$', lista_sede.as_view(), name ="lista_sede"),
    url(r'^sede/crear/$', crear_sede, name ="crear_sede"),
    url(r'^sede/actualizar/(?P<pk>\d+)$', actualizar_sede, name ="actualizar_sede"),
    url(r'^sede/detalle/(?P<pk>\d+)$', detalle_sede.as_view(), name ="detalle_sede"),


    url(r'^articulo/lista/$', lista_articulo.as_view(), name ="lista_articulo"),
    url(r'^articulo/lista/impresion/$', imp_inventario, name ="imp_inventario"),
    url(r'^articulo/lista/([\w-]+)$', lista_articulo.as_view(), name ="lista_articulo"),
    url(r'^articulo/crear/$', crear_articulo, name ="crear_articulo"),
    url(r'^articulo/actualizar/(?P<pk>\d+)$', actualizar_articulo, name ="actualizar_articulo"),
    url(r'^articulo/ver/(?P<pk>\d+)$', detalle_articulo.as_view(), name ="detalle_articulo"),
    url(r'^articulo/sede/lista/seleccion/$', seleccion_sede_lista_articulo, name="seleccion_sede_lista_articulo"),

    url(r'^articulo/sede/lista/(?P<pk>\d+)$', lista_sede_articulo_super, name ="lista_sede_articulo_super"),
    url(r'^articulo/sede/lista/$', lista_sede_articulo, name ="lista_sede_articulo"),
    url(r'^articulo/sede/impresion/$', imp_inventario_sede, name ="imp_inventario_sede"),


    url(r'^transferencia/sedes/lista/$', ListaTransferencia.as_view(), name ="ListaTransferencia"),


    url(r'^usuario/lista/$', lista_usuario.as_view(), name ="lista_usuario"),
    url(r'^usuario/lista/([\w-]+)$', lista_usuario.as_view(), name ="lista_usuario"),
    url(r'^usuario/eliminar/(?P<pk>\d+)$', eliminar_usuario, name ="eliminar_usuario"),
    url(r'^usuario/$', Register, name ="Register"),
    url(r'^cerrar/$', Logout, name ="Logout"),
    url(r'^', Home, name ="Home"),
]
