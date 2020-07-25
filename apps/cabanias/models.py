from django.db import models

from apps.articulos.models import Articulo


choices_cabanias = (
    ('DISPONIBLE', 'DISPONIBLE'),
    ('OCUPADO', 'OCUPADO'),
    ('RESERVADO', 'RESERVADO'),
)


class Inventario(models.Model):

    cantidad = models.IntegerField(null=False, blank=False)
    articulo = models.ForeignKey(Articulo, null=False, blank=False, 
    on_delete=models.CASCADE, related_name='inventario_articulo')

    def __str__(self):
        return '%s - %s' % (self.cantidad, self.articulo)
    
    class Meta:

        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'


class Cabania(models.Model):

    descripcion = models.CharField(max_length=300, null=True, blank=True)
    inventario = models.ManyToManyField(Inventario, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=11, null=True, blank=True)
    habitacion = models.IntegerField(null=True, blank=True)
    estado = models.CharField(choices=choices_cabanias, max_length=300, 
    null=True, blank=True, default='DISPONIBLE')
    # imagenes para las cabanias 
    foto_exterior = models.ImageField(upload_to='cabanias', null=True, blank=True)
    foto_interior = models.ImageField(upload_to='cabanias', null=True, blank=True)
    foto_detalle = models.ImageField(upload_to='cabanias', null=True, blank=True)
    observacion = models.TextField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return str(self.descripcion)

    class Meta:

        verbose_name = 'Cabaña'
        verbose_name_plural = 'Cabañas'
