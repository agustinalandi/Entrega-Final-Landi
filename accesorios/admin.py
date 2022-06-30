from django.contrib import admin
from accesorios.models import Accesorio

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'talle_accesorio', 'color_accesorio', 'es_para_regalo']
