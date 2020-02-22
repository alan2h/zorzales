from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, ListView

from django.contrib.messages.views import SuccessMessageMixin

from .models import Articulo
from .forms import ArticuloForm


class ArticuloCreateView(SuccessMessageMixin, CreateView):

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo_form.html'
    success_url = '/articulos/listado'
    success_message = 'El artículo se registro con éxito'


class ArticuloListView(ListView):

    queryset = Articulo.objects.all()
    template_name = 'articulos_list.html'
    paginate_by = 10

    def get_queryset(self):

        queryset = Articulo.objects.all()
        if 'search' in self.request.GET:
            if self.request.GET.get('search') != '':
                queryset = Articulo.objects.filter(descripcion__icontains=self.request.GET.get('search'))
                if len(queryset) == 0:
                    queryset = Articulo.objects.filter(codigo_barra__icontains=self.request.GET.get('search'))
        return queryset
