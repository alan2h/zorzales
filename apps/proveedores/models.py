from django.db import models

from apps.personas.models import Persona

from apps.complementos.contactos.models import Contacto


class Proveedor(models.Model):

    razon_social = models.CharField(max_length=300, null=False, blank=False)
    cuit = models.CharField(max_length=300, null=True, blank=True)
    descripcion = models.TextField(max_length=800, null=True, blank=True)
    referente = models.ForeignKey(Persona, blank=True, null=True, 
    on_delete=models.CASCADE)
    contacto = models.ManyToManyField(Contacto, blank=True)

    def __str__(self):
        return self.razon_social

    class Meta: 

        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'


