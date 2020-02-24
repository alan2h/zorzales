from datetime import datetime

from django import forms

from .models import Pedido


class PedidoForm(forms.ModelForm):

    '''fecha = models.DateField(null=False, blank=False)
    articulos = models.ManyToManyField(Articulo, related_name='articulos_pedidos', blank=False)
    precio_compra = models.DecimalField(decimal_places=2, max_digits=12, 
    null=True, blank=True)
    observacion = models.TextField(max_length=300, null=True, blank=True)'''
    fecha = forms.DateField(initial=datetime.now(), required=True, widget=forms.DateInput(attrs={
        'class': 'form-control'
    }))
    precio_compra = forms.DecimalField(required=True, decimal_places=2, max_digits=12, 
    widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'disabled': 'disabled'
    }))
    observacion = forms.CharField(required=True, max_length=300, widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Pedido
        fields = ['fecha', 'precio_compra', 'observacion']
