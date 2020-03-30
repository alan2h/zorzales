from django.db import models


class Sector(models.Model):

    descripcion = models.CharField(max_length=300, null=False, blank=False)

    baja = models.BooleanField(default=False, null=True, blank=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.descripcion)
    
    class Meta:

        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
