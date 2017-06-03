from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^lista/$', ListaIngreso.as_view(), name ="ListaIngreso"),
    url(r'^lista/([\w-]+)$', ListaIngreso.as_view(), name ="ListaIngreso"),
    url(r'^crear/$', CrearIngreso.as_view(), name ="CrearIngreso"),
    url(r'^actualizar/(?P<pk>\d+)$', ActualizarIngreso.as_view(), name ="ActualizarIngreso"),
    url(r'^eliminar/(?P<pk>\d+)$', EliminarIngreso.as_view(), name ="EliminarIngreso"),
]
