from django import forms

from .models import Marca


class MarcaForm(forms.ModelForm):

    descripcion = forms.CharField(max_length=800, required=True, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


    class Meta:
        fields = ['descripcion']
        model = Marca
