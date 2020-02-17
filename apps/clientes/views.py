from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Cliente
from .forms import ClienteForm


class ClienteCreateView(SuccessMessageMixin, CreateView):

    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = '/clientes/listado'
    success_message = 'El Cliente se registro con éxito'


class ClientesListView(ListView):

    model = Cliente
    template_name = 'clientes_listado.html'
