from django.contrib import admin
from .models import *
# Register your models here.
class DetalleIngresaAdmin(admin.TabularInline):
    model = DetalleIngreso

class IngresoAdmin(admin.ModelAdmin):
    inlines = [
        DetalleIngresaAdmin,
    ]

admin.site.register(Ingreso, IngresoAdmin)
