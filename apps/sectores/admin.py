from django.contrib import admin


from .models import Sector


class SectorAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion'
    ]

    list_search = [
        'descripcion'
    ]

admin.site.register(Sector, SectorAdmin)
