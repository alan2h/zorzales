from django.db import models
from django.contrib.auth.models import User

from apps.personas.models import Persona


class Cliente(Persona):
    
    numero_documento = models.CharField(max_length=300, null=True, blank=True)
    foto = models.ImageField(upload_to='clientes', blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.CharField(max_length=300, blank=True, null=True)
    baja = models.BooleanField(default=False)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=600, blank=True, null=True)
    observacion = models.TextField(max_length=300, blank=True, null=True)
    # para el e-commerce
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # para realizar bajas

    baja = models.BooleanField(default=False, null=True, blank=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):

        return '%s, %s' % (self.apellido, self.nombre)
