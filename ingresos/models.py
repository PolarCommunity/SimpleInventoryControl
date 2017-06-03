from django.db import models
from datetime import date
from django.contrib.auth.models import User
from general.models import *

# Create your models here.
class Ingreso(models.Model):
    fecha = models.DateField(default = date.today)
    descripcion = models.CharField(max_length=150)
    total = models.DecimalField(max_digits = 12, decimal_places = 2, default=0)
    comprobante = models.CharField(max_length=50)
    user = models.ForeignKey(User, blank=True)
    def __str__(self):
        return self.comprobante

class DetalleIngreso(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits = 12, decimal_places = 2, default=0)
    precio_total = models.DecimalField(max_digits = 12, decimal_places = 2, default=0)
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    def __str__(self):
        return self.ingreso.comprobante
