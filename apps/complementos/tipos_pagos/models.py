from django.db import models


class TipoPago(models.Model):

    descripcion = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Tipo de pago'
        verbose_name_plural = 'Tipos de pagos'
