from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from .resources import *


# Register your models here.
class DescripsionArticuloAdmin(admin.TabularInline):
    model = DescripcionArticulo

class SedeArticuloAdmin(admin.TabularInline):
    model = ArticuloSede

class SedeUsuarioAdmin(admin.TabularInline):
    model = SedeUsuario

class SedeAdmin(admin.ModelAdmin):
    inlines = [
        SedeUsuarioAdmin,
        SedeArticuloAdmin,
    ]
    list_display = ['nombre','direccion']
    ordering = ['nombre']
    search_fields = ['nombre','direccion']

@admin.register(Articulo)
class ArticAdmin(ImportExportModelAdmin):
    resource_class = ArticuloResource
    inlines = [
        DescripsionArticuloAdmin,
        SedeArticuloAdmin,
    ]
    list_display = ['codigo','nombre','cantidad','precio']
    ordering = ['codigo']
    search_fields = ['codigo','nombre']

@admin.register(ArticuloSede)
class ArticAdmin(ImportExportModelAdmin):
    resource_class = SedeArticuloResource
    list_display = ['id','cantidad','articulo','sede']
    ordering = ['articulo']
    search_fields = ['articulo','sede']




admin.site.register(Sede, SedeAdmin)
