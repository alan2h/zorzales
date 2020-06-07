from django.views.generic import TemplateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Cobranza, Reserva
from .forms import CobranzaForm

from apps.complementos.tipos_pagos.models import TipoPago


class ReservaView(TemplateView):

    template_name = 'reservas_view.html'


class CobranzaCreateView(SuccessMessageMixin, CreateView):

    model = Cobranza
    template_name = 'cobranza_form.html'
    form_class = CobranzaForm
    success_url = '/reservas/listado'
    success_message = 'Esta reserva se cobro con éxito'

    def post(self, request, *args, **kwargs):
        print(self.request.POST)
        cobranza_form = CobranzaForm(data=self.request.POST)
        if cobranza_form.is_valid():
            reserva = Reserva.objects.get(pk=kwargs['id'])
            tipo_pago = TipoPago.objects.get(pk=self.request.POST['tipo_pago'])

            Cobranza.objects.create(
                reserva=reserva,
                tipo_pago=tipo_pago,
                monto=self.request.POST['monto']
            )
            messages.success(self.request, self.success_message)

            return redirect(self.success_url)
        else:
            messages.error(self.request, 'Error de carga en el formulario')
            return render(request, self.template_name, context={'form': cobranza_form})