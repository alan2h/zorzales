from django.contrib import admin

from .models import Cabania, Inventario


class IventarioAdmin(admin.ModelAdmin):

    list_display = [
        'cantidad',
        'articulo'
    ]


class CabaniaAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion',
        'precio',
        'habitacion'
    ]

admin.site.register(Inventario, IventarioAdmin)
admin.site.register(Cabania, CabaniaAdmin)
