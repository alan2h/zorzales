from django.db import models


class Marca(models.Model):

    descripcion = models.CharField(max_length=800, blank=False, null=False)

    # para realizar bajas

    baja = models.BooleanField(default=False, null=True, blank=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        
        return str(self.descripcion)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
