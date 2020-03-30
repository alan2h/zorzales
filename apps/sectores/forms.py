from django import forms

from .models import Sector


class SectorForm(forms.ModelForm):

    descripcion = forms.CharField(max_length=300, required=True, 
    widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Sector
        fields = ['descripcion']
