from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, \
    DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Rubro
from .forms import RubroForm

from apps.lib.delete.delete_logic import DeleteLogic


class RubroCreateView(SuccessMessageMixin, CreateView):

    model = Rubro
    form_class = RubroForm
    template_name = 'rubro_form.html'
    success_url = '/complementos/rubros/listado'
    success_message = 'El rubro se agrego con éxito'


class RubroListView(ListView):

    queryset = Rubro.objects.filter(baja=False)
    template_name = 'rubros_list.html'
    paginate_by = 10

    def get_queryset(self):

        queryset = Rubro.objects.filter(baja=False)
        if 'search' in self.request.GET:
            if self.request.GET.get('search') != '':
                queryset = Rubro.objects.filter(descripcion__icontains=\
                    self.request.GET.get('search'), baja=False)
        return queryset


class RubroUpdateView(SuccessMessageMixin, UpdateView):

    model = Rubro
    form_class = RubroForm
    template_name = 'rubro_form.html'
    success_url = '/complementos/rubros/listado'
    success_message = 'El rubro se agrego con éxito'


class RubroDeleteView(DeleteLogic, DeleteView):

    model = Rubro
    template_name = 'rubro_delete_confirm.html'
    success_url = '/complementos/rubros/listado'
