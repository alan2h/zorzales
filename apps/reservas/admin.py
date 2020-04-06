from django.contrib import admin

from .models import Reserva


class ReservaAdmin(admin.ModelAdmin):

    list_display = [
        'fecha_ingreso',
        'cliente',
        'alquiler'
    ]

admin.site.register(Reserva, ReservaAdmin)
