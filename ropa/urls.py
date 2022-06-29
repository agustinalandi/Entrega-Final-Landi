from django.urls import path
from ropa.views import Crear_prenda, Listar_prendas, Detallar_prenda, Actualizar_prenda, Eliminar_prenda, Crear_pedido, Listar_pedidos, Detallar_pedido, Actualizar_pedido, Eliminar_pedido, buscar_pedido 

urlpatterns = [
    path('crear_prenda/', Crear_prenda.as_view(), name = 'crear_prenda'),
    path('listar_prendas/', Listar_prendas.as_view(), name = 'listar_prendas'),
    path('detalle_prenda/<int:pk>/', Detallar_prenda.as_view(), name = 'detalle_prenda'),
    path('actualizar_prenda/<int:pk>/', Actualizar_prenda.as_view(), name = 'actualizar_prenda'),
    path('eliminar_prenda/<int:pk>/', Eliminar_prenda.as_view(), name = 'eliminar_prenda'),
    
    path('crear_pedido/', Crear_pedido.as_view(), name = 'crear_pedido'),
    path('listar_pedidos/', Listar_pedidos.as_view(), name = 'lista_pedidos'),
    path('detalle_pedido/<int:pk>/', Detallar_pedido.as_view(), name = 'detalle_pedido'),
    path('actualizar_pedido/<int:pk>/', Actualizar_pedido.as_view(), name = 'actualizar_pedido'),
    path('eliminar_pedido/<int:pk>/', Eliminar_pedido.as_view(), name = 'eliminar_pedido'),
    path('buscar_pedido/', buscar_pedido, name = 'buscar_pedido'),

]
