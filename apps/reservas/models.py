from django.db import models

from apps.clientes.models import Cliente
from apps.cabanias.models import Cabania

from apps.complementos.tipos_pagos.models import TipoPago


class Reserva(models.Model):

    fecha_ingreso = models.DateField(null=True, blank=True)
    hora_ingreso = models.TimeField(null=True, blank=True)
    fecha_salida = models.DateField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, 
     on_delete=models.CASCADE)
    cabania = models.ForeignKey(Cabania, null=False, blank=False, 
     on_delete=models.CASCADE)
    
    tipo_pago = models.ForeignKey(TipoPago, null=True, blank=True, 
    on_delete=models.CASCADE)
    monto_inicial = models.DecimalField(max_digits=12, decimal_places=2, 
    null=True, blank=True)
    
    observacion = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.fecha_ingreso, self.cliente, self.cabania)

    class Meta:
        
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


class Cobranza(models.Model):

    reserva = models.ForeignKey(Reserva, null=False, blank=False,
     on_delete=models.CASCADE)
    tipo_pago = models.ForeignKey(TipoPago, null=True, blank=True, 
    on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    monto = models.DecimalField(max_digits=12, decimal_places=2, 
    null=False, blank=False)

    def __str__(self):
        return f'{self.reserva} - {self.monto}'

    class Meta:
        verbose_name = 'Cobranza'
        verbose_name_plural = 'Cobranzas'
