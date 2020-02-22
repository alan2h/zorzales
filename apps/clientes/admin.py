from django.contrib import admin

from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):

    list_display = [
        'nombre',
        'apellido'
    ]


admin.site.register(Cliente, ClienteAdmin)
