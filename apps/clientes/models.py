from django import models

from apps.personas.models import Persona


class Cliente(Persona):

    baja = models.BooleanField(default=False)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=600, blank=True, null=True)

    def __str__(self):

        return '%s, %s' % (self.apellido, self.nombre)
