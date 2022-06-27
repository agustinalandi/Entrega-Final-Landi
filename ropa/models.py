from django.db import models
from django.utils.timezone import now

# Create your models here.

class Pedido(models.Model):
    prenda = models.CharField(max_length=100)
    precio = models.FloatField()
    fecha_pedido = models.DateField(default=now)
    es_temporada_actual = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

class Prenda(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True)
    talle = models.IntegerField()
    color = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Prenda'
        verbose_name_plural = 'Prendas'

class Accesorio(models.Model):
    tipo = models.CharField(max_length=50)
    talle_accesorio = models.IntegerField()
    color_accesorio = models.CharField(max_length=70)
    para_regalo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'
