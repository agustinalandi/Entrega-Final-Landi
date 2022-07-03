from django.contrib import admin
from ropa.models import Pedido, Prenda

# Register your models here.
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['prenda', 'talle', 'color', 'tiene_estampado', 'fecha_pedido', 'imagen_pedido']

@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color', 'tipo_tela', 'es_temporada_actual', 'precio', 'imagen_prenda']

