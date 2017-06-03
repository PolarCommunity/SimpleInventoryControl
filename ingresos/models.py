from django.db import models
from datetime import date
from django.contrib.auth.models import User
from general.models import *

# Create your models here.
class Ingreso(models.Model):
    fecha = models.DateField(default = date.today)
    descripcion = models.CharField(max_length=150)
    comprobante = models.CharField(max_length=50)
    sede = models.ForeignKey(Sede, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True)
    def __str__(self):
        return self.comprobante

class DetalleIngreso(models.Model):
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    articulo = models.ForeignKey(ArticuloSede, on_delete=models.CASCADE)
    def __str__(self):
        return self.ingreso.articulo
