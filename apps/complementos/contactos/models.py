from django.db import models

class TipoContacto(models.Model):

    descripcion = models.CharField(max_length=300, blank=False, null=False)

    class Meta:

        verbose_name = 'Tipo de Contacto'
        verbose_name_plural = 'Tipos de Contactos'

    def __str__(self):
        return self.descripcion


class Contacto(models.Model):

    tipo_contacto = models.ForeignKey(TipoContacto, null=True, blank=True, 
    on_delete=models.CASCADE)
    valor = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f'{self.tipo_contacto}-{self.valor}'
    
    class Meta:

        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    