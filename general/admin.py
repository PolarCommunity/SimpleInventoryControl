from django.contrib import admin
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

class SedeAdmin(admin.ModelAdmin):
    inlines = [
        SedeUsuarioAdmin,
        SedeArticuloAdmin,
    ]


admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Sede, SedeAdmin)
