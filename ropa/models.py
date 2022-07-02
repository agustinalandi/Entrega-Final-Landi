from django.db import models
from django.utils.timezone import now

# Create your models here.

class Prenda(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50)
    tipo_tela = models.CharField(max_length=30)
    es_temporada_actual = models.BooleanField(default=True)
    precio = models.FloatField()
    imagen_prenda = models.ImageField(upload_to='imagenes_prendas')
    
    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'

class Pedido(models.Model):
    prenda = models.CharField(max_length=100)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)
    tiene_estampado = models.BooleanField(default=False)
    fecha_pedido = models.DateField(default=now)
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

