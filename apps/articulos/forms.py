from django import forms

from .models import Articulo

# complementos
from apps.complementos.articulos.marcas.models import Marca
from apps.complementos.articulos.rubros.models import Rubro

# sectores
from apps.sectores.models import Sector


class ArticuloForm(forms.ModelForm):

    codigo_barra = forms.CharField(required=False, max_length=900, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    descripcion = forms.CharField(required=True, max_length=800, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    referencia = forms.CharField(required=False, max_length=300, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    marca = forms.ModelChoiceField(required=False, queryset=Marca.objects.filter(baja=False), 
    widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    rubro = forms.ModelChoiceField(required=False, queryset=Rubro.objects.filter(baja=False), 
    widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    precio_compra = forms.DecimalField(decimal_places=2, max_digits=12, required=False, 
    widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    precio_venta = forms.DecimalField(decimal_places=2, max_digits=12, required=False,
    widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    stock = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    stock_minimo = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    imagen = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    alicuota_iva = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))

    para_venta = forms.BooleanField(required=False, initial=True, widget=forms.CheckboxInput(
        attrs=({
            'class': 'form-control'
        })
    ))

    sector = forms.ModelChoiceField(required=True, queryset=Sector.objects.filter(baja=False),
    widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        fields = '__all__'
        model = Articulo
