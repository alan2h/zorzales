from django.db import models

from apps.articulos.models import Articulo


class PedidoArticulo(models.Model):

    articulo = models.ForeignKey(Articulo, related_name='articulos', blank=False,
    on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return '%s - %s' % (str(self.cantidad), str(self.articulo.descripcion))

    class Meta:
        verbose_name = 'Pedido-Articulo'
        verbose_name_plural = 'Pedidos-Articulos'


class Pedido(models.Model):

    fecha = models.DateField(null=False, blank=False)
    precio_compra = models.DecimalField(decimal_places=2, max_digits=12, 
    null=True, blank=True)
    observacion = models.TextField(max_length=300, null=True, blank=True)

    pedido_articulo = models.ManyToManyField(PedidoArticulo, related_name='articulos_pedidos', 
    blank=False)
    # para realizar bajas

    baja = models.BooleanField(default=False, null=True, blank=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):

        return str(self.fecha)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

