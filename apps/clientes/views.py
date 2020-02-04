from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Cliente
from .forms import ClienteForm


class ClienteCreateView(CreateView):

    model = Cliente
    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = '/inicio'


class ClientesListView(ListView):

    model = Cliente
    template_name = 'clientes_listado.html'
