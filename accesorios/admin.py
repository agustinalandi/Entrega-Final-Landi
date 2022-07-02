from django.contrib import admin
from accesorios.models import Accesorio

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'color', 'es_resistente_agua', 'precio', 'imagen_accesorio']
