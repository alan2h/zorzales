from django import forms

from .models import Proveedor


class ProveedorForm(forms.ModelForm):

    '''
    razon_social = models.CharField(max_length=300, null=False, blank=False)
    cuit = models.CharField(max_length=300, null=True, blank=True)
    descripcion = models.TextField(max_length=800, null=True, blank=True)
    referente = models.ForeignKey(Persona, blank=True, null=True, 
    on_delete=models.CASCADE)
    contacto = models.ManyToManyField(Contacto, blank=True)
    '''

    razon_social = forms.CharField(max_length=300, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    cuit = forms.CharField(max_length=300, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    descripcion = forms.CharField(max_length=800, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    class Meta:
        model = Proveedor
        fields = ['razon_social', 'cuit', 'descripcion']
