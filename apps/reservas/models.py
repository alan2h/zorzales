from django.db import models

from apps.clientes.models import Cliente
from apps.alquileres.models import Alquiler


class Reserva(models.Model):

    fecha_ingreso = models.DateField(null=True, blank=True)
    hora_ingreso = models.TimeField(null=True, blank=True)
    fecha_salida = models.DateField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, 
     on_delete=models.CASCADE)
    alquiler = models.ForeignKey(Alquiler, null=False, blank=False, 
     on_delete=models.CASCADE)
    observacion = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return '%s - %s - %s' % (self.fecha_ingreso, self.cliente, self.alquiler)

    class Meta:
        
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
