from django import forms 

from .models import Contacto, TipoContacto


class TipoContactoForm(forms.ModelForm):

    descripcion = forms.CharField(max_length=300, required=True, 
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control'
                                  }))

    class Meta:
        model = TipoContacto
        fields = '__all__'


class ContactoForm(forms.ModelForm):

    tipo_contacto = forms.ModelChoiceField(queryset=TipoContacto.objects.all(), 
                                           required=True, widget=forms.Select(attrs={
                                               'class': 'form-control'
                                           }))
    valor = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={
                                'class' : 'form-control'
                            }))

    class Meta:
        model = Contacto
        fields = '__all__'
