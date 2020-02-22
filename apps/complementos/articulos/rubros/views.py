from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Rubro
from .forms import RubroForm


class RubroCreateView(SuccessMessageMixin, CreateView):

    model = Rubro
    form_class = RubroForm
    template_name = 'rubro_form.html'
    success_url = '/complementos/rubros/listado'
    success_message = 'El rubro se agrego con éxito'


class RubroListView(ListView):

    queryset = Rubro.objects.all()
    template_name = 'rubros_list.html'
