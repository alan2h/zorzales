from django.http import JsonResponse

from apps.complementos.articulos.marcas.forms import MarcaForm
from apps.complementos.articulos.rubros.forms import RubroForm


def guardar_marca(request):
    if request.is_ajax():
        marca_form = MarcaForm(data=request.POST)
        if marca_form.is_valid():
            marca = marca_form.save()
            return JsonResponse({'status':'200', 'id': marca.id})
        else:
            return JsonResponse({'status': '500'})



def guardar_rubro(request):
    if request.is_ajax():
        rubro_form = RubroForm(data=request.POST)
        if rubro_form.is_valid():
            rubro = rubro_form.save()
            return JsonResponse({'status':'200', 'id': rubro.id})
        else:
            return JsonResponse({'status': '500'})
