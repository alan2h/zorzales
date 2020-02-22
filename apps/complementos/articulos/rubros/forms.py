from django import forms

from .models import Rubro


class RubroForm(forms.ModelForm):

    descripcion = forms.CharField(max_length=800, required=True, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))


    class Meta:
        model = Rubro
        fields = ['descripcion']
