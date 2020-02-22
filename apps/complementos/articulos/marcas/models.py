from django.db import models


class Marca(models.Model):

    descripcion = models.CharField(max_length=800, blank=False, null=False)

    def __str__(self):
        
        return str(self.descripcion)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
