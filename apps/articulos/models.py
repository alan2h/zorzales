from django.db import models

# complementos
from apps.complementos.articulos.marcas.models import Marca
from apps.complementos.articulos.rubros.models import Rubro

# sectores --> representa en que lugar se encuentra el articulo
from apps.sectores.models import Sector


class Articulo(models.Model):

    codigo_barra = models.CharField(max_length=900, null=True, blank=True)
    descripcion = models.CharField(max_length=800, null=False, blank=False)
    marca = models.ForeignKey(Marca, null=True, blank=True, related_name='articulo_marca', on_delete=models.CASCADE)
    rubro = models.ForeignKey(Rubro, null=True, blank=True, related_name='articulo_rubro', on_delete=models.CASCADE)

    precio_compra = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)
    precio_venta = models.DecimalField(decimal_places=2, max_digits=8, null=True, blank=True)

    stock = models.IntegerField(null=True, blank=True)
    stock_minimo = models.IntegerField(null=True, blank=True)
    imagen = models.ImageField(upload_to='articulos', null=True, blank=True)
    alicuota_iva = models.DecimalField(max_digits=12, decimal_places=2, default=21, 
    blank=True, null=True)
    fecha_compra = models.DateTimeField(auto_created=True, blank=True, null=True)

    referencia = models.CharField(max_length=300, blank=True, null=True) # campo de tipo observacion
    para_venta = models.BooleanField(default=True, blank=True, null=True) # si tiene tildado es para venderlo
    #, caso contrario es solo inventario

    sector = models.ForeignKey(Sector, null=True, blank=True, on_delete=models.CASCADE) # a que sector pertenece el articulo

    # para realizar bajas

    baja = models.BooleanField(default=False, blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.descripcion)

    class Meta:
        verbose_name = 'Artículos'
        verbose_name_plural = 'Artículos'
