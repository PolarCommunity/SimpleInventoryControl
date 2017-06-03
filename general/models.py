from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Articulo(models.Model):
    codigo = models.CharField(max_length=15, unique = True)
    nombre = models.CharField(max_length=150)
    cantidad = models.DecimalField(max_digits = 12, decimal_places = 2, default=0)
    precio = models.DecimalField(max_digits = 12, decimal_places = 2, default=0)
    def __str__(self):
        return self.nombre

class DescripcionArticulo(models.Model):
    descripcion = models.CharField(max_length=254)
    articulo = models.OneToOneField(Articulo, on_delete=models.CASCADE)
    def __str__(self):
        return self.articulo.nombre

class Sede(models.Model):
    nombre = models.CharField(max_length=100, unique = True)
    direccion = models.CharField(max_length=154)
    def __str__(self):
        return self.nombre

class ArticuloSede(models.Model):
    cantidad = models.DecimalField(max_digits=12, decimal_places=2)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    def __str__(self):
        art = self.sede.nombre + self.articulo.nombre
        return art

class SedeUsuario(models.Model):
    user = models.OneToOneField(User)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    def __str__(self):
        usr = self.sede.nombre + self.user.username
        return usr
