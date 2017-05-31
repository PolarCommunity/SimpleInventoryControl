from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):
    codigo = models.CharField(max_length=15, unique = True)
    nombre = models.CharField(max_length=150)
    cantidad = models.DecimalField(max_digits = 12, decimal_places = 2)
    def __str__(self):
        return self.nombre

class DescripcionArticulo(models.Model):
    descripcion = models.CharField(max_length=254)
    articulo = models.OneToOneField(Articulo)

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=154)

class ArticuloSede(models.Model):
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    articulo = models.ForeignKey(Articulo)
    sede = models.ForeignKey(Sede)

class SedeUsuario(models.Model):
    user = models.OneToOneField(User)
    sede = models.ForeignKey(Sede)
