from django.contrib import admin

from .models import Alquiler, Inventario


class InventarioAdmin(admin.ModelAdmin):

    list_display = [
        'cantidad',
        'articulo'
    ]

class AlquilerAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion'
    ]

admin.site.register(Alquiler, AlquilerAdmin)
admin.site.register(Inventario, InventarioAdmin)
