from django.db import models
from django.utils.timezone import now

class Accesorio(models.Model):
    tipo = models.CharField(max_length=50)
    color = models.CharField(max_length=70)
    es_resistente_agua = models.BooleanField(default=True)
    precio = models.IntegerField()
    imagen_accesorio = models.ImageField(upload_to='imagenes_accesorios', blank=True, null=True)

    class Meta:
        verbose_name = 'Accesorio'
        verbose_name_plural = 'Accesorios'
    
    def __str__(self):
        return self.tipo
