from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Proveedor
from .forms import ProveedorForm


class ProveedorListView(ListView):

    model = Proveedor
    template_name = 'proveedores_list.html'


class ProveedorCreateView(SuccessMessageMixin, CreateView):

    model = Proveedor
    template_name = 'proveedor_form.html'
    form_class = ProveedorForm
