from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

from apps.articulos.models import Articulo


def articulo_list(request):

    print(request.GET)
    articulos = Articulo.objects.filter(baja=False)
    if 'search' in request.GET:
        if request.GET.get('search') != '':
            articulos = Articulo.objects.filter(baja=False, descripcion__icontains=request.GET.get('search'))
            if len(articulos) == 0:
                articulos = Articulo.objects.filter(baja=False, codigo_barra__icontains=request.GET.get('search'))
    paginator = Paginator(articulos, 5)
    articulos_list = paginator.page(request.GET.get('pagina'))
    return JsonResponse(serializers.serialize('json', articulos_list), safe=False)
