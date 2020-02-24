from django.db import models

from apps.articulos.models import Articulo


class Pedido(models.Model):

    fecha = models.DateField(null=False, blank=False)
    articulos = models.ManyToManyField(Articulo, related_name='articulos_pedidos', blank=False)
    precio_compra = models.DecimalField(decimal_places=2, max_digits=12, 
    null=True, blank=True)
    observacion = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):

        return str(self.fecha)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
