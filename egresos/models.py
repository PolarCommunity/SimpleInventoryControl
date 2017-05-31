from django.db import models
from datetime import date
from django.contrib.auth.models import User
from general.models import Articulo

# Create your models here.
class Egreso(models.Model):
    fecha = models.DateField(default = date.today)
    descripcion = models.CharField(max_length=150)
    user = models.ForeignKey(User)
    def __str__(self):
        try:
            retorno = str(self.fecha) + self.descripcion[:5]
        except Exception as e:
            retorno = str(self.fecha) + self.descripcion
        return retorno

class DetalleEgreso(models.Model):
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    egreso = models.ForeignKey(Egreso, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    def __str__(self):
        try:
            retorno = str(self.egreso.fecha) + self.egreso.descripcion[:5]
        except Exception as e:
            retorno = str(self.egreso.fecha) + self.egreso.descripcion
        return retorno
