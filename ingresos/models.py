from django.db import models
from datetime import date
from django.contrib.auth.models import User
from general.models import Articulo

# Create your models here.
class Ingreso(models.Model):
    fecha = models.DateField(default = date.today)
    descripcion = models.CharField(max_length=150)
    comprobante = models.CharField(max_length=50)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.comprobante

class DetalleIngreso(models.Model):
    cantidad = models.DecimalField(max_digits=15, decimal_places=2)
    ingreso = models.ForeignKey(Ingreso)
    articulo = models.ForeignKey(Articulo)
    def __str__(self):
        return self.ingreso.comprobante
