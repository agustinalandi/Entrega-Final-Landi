from django.urls import path
from ropa.views import eliminar_prenda, listar_pedidos, crear_pedido, buscar_pedido, crear_prenda, listar_prendas, detallar_prenda

urlpatterns = [
    path('listar_pedidos/', listar_pedidos, name = 'lista_pedidos'),
    path('crear_pedido/', crear_pedido, name = 'crear_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),
    path('crear_prenda/', crear_prenda, name = 'crear_prenda'),
    path('listar_prendas/', listar_prendas, name = 'listar_prendas'),
    path('detalle_prenda/<int:pk>/', detallar_prenda, name = 'detalle_prenda'),
    path('eliminar_prenda/<int:pk>/', eliminar_prenda, name = 'eliminar_prenda'),
]