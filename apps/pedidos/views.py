from django.shortcuts import render

from django.views.generic import View, ListView
from django.contrib import messages

from .models import Pedido
from .forms import PedidoForm


class PedidoCreateView(View):

    def get(self, request, *args, **kwargs):
        pedido_form = PedidoForm()
        return render(request, 'pedido_form.html', context={'form': pedido_form})

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        return False


class PedidoListView(ListView):

    template_name = 'pedidos_list.html'
    queryset = Pedido.objects.all()
