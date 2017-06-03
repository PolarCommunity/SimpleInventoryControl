from django.contrib import admin
ontrib import admin
from .models import *
# Register your models here.
class DescripsionArticuloAdmin(admin.TabularInline):
    model = DescripcionArticulo

class SedeArticuloAdmin(admin.TabularInline):
    model = ArticuloSede

class SedeUsuarioAdmin(admin.TabularInline):
    model = SedeUsuario

class ArticuloAdmin(admin.ModelAdmin):
    inlines = [
        DescripsionArticuloAdmin,
        SedeArticuloAdmin,
    ]
    list_display = ['codigo','nombre','cantidad','precio']
    ordering = ['codigo']
    search_fields = ['codigo','nombre']


class SedeAdmin(admin.ModelAdmin):
    inlines = [
        SedeUsuarioAdmin,
        SedeArticuloAdmin,
    ]
    list_display = ['nombre','direccion']
    ordering = ['nombre']
    search_fields = ['nombre','direccion']



admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Sede, SedeAdmin)
