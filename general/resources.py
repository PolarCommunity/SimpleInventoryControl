from import_export import resources
from .models import *

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo

class SedeArticuloResource(resources.ModelResource):
    class Meta:
        model = ArticuloSede
        fields = ('id', 'cantidad', 'articulo__nombre', 'sede__nombre',)
