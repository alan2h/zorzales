from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Cliente
from .forms import ClienteForm

from apps.lib.delete.delete_logic import DeleteLogic


class ClienteCreateView(SuccessMessageMixin, CreateView):

    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = '/clientes/listado'
    success_message = 'El Cliente se registro con éxito'


class ClientesListView(ListView):

    queryset = Cliente.objects.filter(baja=False)
    template_name = 'clientes_listado.html'


class ClienteUpdateView(SuccessMessageMixin, UpdateView):

    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = '/clientes/listado'
    success_message = 'El Cliente se modifico con éxito'


class ClienteDeleteView(DeleteLogic, DeleteView):

    model = Cliente
    template_name = 'cliente_delete_confirm.html'
    success_url = '/clientes/listado'
    
