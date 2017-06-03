from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sede/lista/$', lista_egreso_sede.as_view(), name ="lista_egreso_sede"),
    url(r'^super/lista/$', lista_egreso_super.as_view(), name ="lista_egreso_super"),
    url(r'^sede/crear/$', crear_egreso, name ="crear_egreso"),
    url(r'^sede/detalle/crear/(?P<pk>\d+)$', crear_detalle_egreso, name ="crear_detalle_egreso"),

]
