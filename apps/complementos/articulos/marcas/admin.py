from django.contrib import admin

from .models import Marca


class MarcaAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion'
    ]

    search_fields = [
        'descripcion'
    ]

    list_filter = [
        'descripcion'
    ]


admin.site.register(Marca, MarcaAdmin)
