from django.contrib import admin

from .models import Pedido, PedidoArticulo


class PedidoArticuloAdmin(admin.ModelAdmin):

    list_display = [
        'articulo',
        'cantidad'
    ]


class PedidoAdmin(admin.ModelAdmin):

    list_display = [
        'fecha',
        'precio_compra',
        'observacion'
    ]


admin.site.register(Pedido, PedidoAdmin)
admin.site.register(PedidoArticulo, PedidoArticuloAdmin)
