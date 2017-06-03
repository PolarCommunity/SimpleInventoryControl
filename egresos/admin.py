from django.contrib import admin
from .models import *
# Register your models here.
class DetalleEgresaAdmin(admin.TabularInline):
    model = DetalleEgreso

class EgresoAdmin(admin.ModelAdmin):
    inlines = [
        DetalleEgresaAdmin,
    ]
    list_display = ['fecha','descripcion','user']
    ordering = ['user']
    list_filter = ('user','fecha')
    date_hierarchy = 'fecha'
    search_fields = ['descripcion']

admin.site.register(Egreso, EgresoAdmin)
