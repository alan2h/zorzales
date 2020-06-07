from django import forms

from .models import Cobranza
from apps.complementos.tipos_pagos.models import TipoPago


class CobranzaForm(forms.ModelForm):

    '''
        forms of cobranza
    '''
    tipo_pago = forms.ModelChoiceField(queryset=TipoPago.objects.all(), 
    required=True, widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    monto = forms.DecimalField(max_digits=12, decimal_places=2,
    required=True, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    class Meta:

        model = Cobranza
        fields = ['tipo_pago', 'monto']

