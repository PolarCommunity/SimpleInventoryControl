from django.contrib import admin
from .models import *
# Register your models here.
class DetalleIngresaAdmin(admin.TabularInline):
    model = DetalleIngreso

class IngresoAdmin(admin.ModelAdmin):
    inlines = [
        DetalleIngresaAdmin,
    ]
    list_display = ['comprobante','fecha','total','user']
    ordering = ['comprobante']
    date_hierarchy = 'fecha'
    list_filter = ('user','fecha')
    search_fields = ['comprobante']



admin.site.register(Ingreso, IngresoAdmin)
