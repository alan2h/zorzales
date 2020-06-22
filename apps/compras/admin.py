from django.contrib import admin

from .models import Compra, CompraArticulo

class CompraAdmin(admin.ModelAdmin):
    
    list_display = [
        'fecha',
        'precio_compra'
    ]

admin.site.register(CompraArticulo)
admin.site.register(Compra, CompraAdmin)
