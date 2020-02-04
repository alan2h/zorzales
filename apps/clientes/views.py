from django.shortcuts import render
from django.views.generic import CreateView

from .models import Cliente
from .forms import ClienteForm


class ClienteCreateView(CreateView):

    template_name = 'cliente_form.html'
    form_class = ClienteForm
    success_url = '/inicio'
