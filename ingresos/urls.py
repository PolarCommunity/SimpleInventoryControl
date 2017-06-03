from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^lista/$', ListaIngreso.as_view(), name ="ListaIngreso"),
    url(r'^lista/([\w-]+)$', ListaIngreso.as_view(), name ="ListaIngreso"),
    url(r'^crear/$', CrearIngreso.as_view(), name ="CrearIngreso"),
    url(r'^detalle/(?P<pk>\d+)$', crear_detalle_ingreso, name ="crear_detalle_ingreso"),
    url(r'^detalle/eliminar/(?P<pk>\d+)$', eliminar_detalle_ingreso, name ="eliminar_detalle_ingreso"),

]
