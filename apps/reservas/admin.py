from django.contrib import admin

from .models import Reserva, Cobranza


class ReservaAdmin(admin.ModelAdmin):

    list_display = [
        'fecha_ingreso',
        'cliente',
        'cabania'
    ]


class CobranzaAdmin(admin.ModelAdmin):

    list_display = [
        'fecha',
        'monto'
    ]

admin.site.register(Reserva, ReservaAdmin)
