from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

from apps.articulos.models import Articulo


def articulo_list(request):

    articulos = Articulo.objects.filter(baja=False)
    paginator = Paginator(articulos, 5)
    articulos_list = paginator.page(1)
    return JsonResponse(serializers.serialize('json', articulos_list), safe=False)
