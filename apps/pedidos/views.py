from django.shortcuts import render

from django.views.generic import View
from django.contrib import messages

from .models import Pedido
from .forms import PedidoForm


class PedidoCreateView(View):

    def get(self, request, *args, **kwargs):
        pedido_form = PedidoForm()
        return render(request, 'pedido_form.html', context={'form': pedido_form})
