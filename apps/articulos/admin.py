from django.contrib import admin

from .models import Articulo


class ArticuloAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion',
        'precio_compra'
    ]

    search_fields = [
        'descripcion'
    ]

    filter_fields = [
        'descripcion'
    ]


admin.site.register(Articulo, ArticuloAdmin)
