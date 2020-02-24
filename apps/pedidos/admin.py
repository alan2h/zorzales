from django.contrib import admin

from .models import Pedido


class PedidoAdmin(admin.ModelAdmin):

    list_display = [
        'fecha',
        'precio_compra',
        'observacion'
    ]


admin.site.register(Pedido, PedidoAdmin)
