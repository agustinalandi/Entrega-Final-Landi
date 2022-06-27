from django.contrib import admin
from ropa.models import Accesorio, Pedido, Prenda

# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['prenda', 'fecha_pedido', 'precio', 'es_temporada_actual']

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'talle', 'color']

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ['tipo', 'talle_accesorio', 'color_accesorio', 'es_para_regalo']
