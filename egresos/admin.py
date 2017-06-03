from django.contrib import admin
from .models import *
# Register your models here.
class DetalleEgresaAdmin(admin.TabularInline):
    model = DetalleEgreso

class EgresoAdmin(admin.ModelAdmin):
    inlines = [
        DetalleEgresaAdmin,
    ]
admin.site.register(Egreso, EgresoAdmin)
