from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Proveedor
from .forms import ProveedorForm


from apps.complementos.contactos.models import Contacto


class ProveedorListView(ListView):

    model = Proveedor
    template_name = 'proveedores_list.html'


class ProveedorCreateView(SuccessMessageMixin, CreateView):

    model = Proveedor
    template_name = 'proveedor_form.html'
    form_class = ProveedorForm
    success_url = '/proveedores/listado'
    success_message = 'El proveedor se registro con éxito'


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):

    model = Proveedor
    template_name = 'proveedor_form.html'
    form_class = ProveedorForm
    success_url = '/proveedores/listado'
    success_message = 'El proveedor se modifico con éxito'
