from django.contrib import admin


from .models import Rubro


class RubroAdmin(admin.ModelAdmin):

    list_display = [
        'descripcion'
    ]

    search_fields = [
        'descripcion'
    ]

    filter_fields = [
        'descripcion'
    ]


admin.site.register(Rubro, RubroAdmin)
