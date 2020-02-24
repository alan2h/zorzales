from django.db import models

from apps.personas.models import Persona


class Cliente(Persona):

    foto = models.ImageField(upload_to='clientes', blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.CharField(max_length=300, blank=True, null=True)
    baja = models.BooleanField(default=False)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=600, blank=True, null=True)
    observacion = models.TextField(max_length=300, blank=True, null=True)

    # para realizar bajas

    baja = models.BooleanField(default=False, null=True, blank=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):

        return '%s, %s' % (self.apellido, self.nombre)
