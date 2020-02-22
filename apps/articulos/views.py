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
