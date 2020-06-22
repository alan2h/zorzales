from django.shortcuts import render

from django.views.generic import ListView

from .models import Proveedor


class ProveedorListView(ListView):

    model = Proveedor
    template_name = 'proveedores_list.html'
