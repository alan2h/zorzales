from django.db import models


class Persona(models):

    nombre = models.CharField(max_length=3000, blank=False, null=False)
    apellido = models.CharField(max_length=3000, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)


    def __str__(self):

        return '%s, %s' % (self.apellido, self.nombre)
