from django.shortcuts import render
from django.views.generic import CreateView

from .models import Articulo
from .forms import ArticuloForm


class ArticuloCreateView(CreateView):

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo_form.html'
