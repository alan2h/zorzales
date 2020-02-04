from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):

    '''
    fields:
    nombre = models.CharField(max_length=3000, blank=False, null=False)
    apellido = models.CharField(max_length=3000, blank=False, null=False)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    foto = models.ImageField(upload_to='clientes', blank=True, null=True)
    baja = models.BooleanField(default=False)
    fecha_baja = models.DateField(blank=True, null=True)
    motivo = models.CharField(max_length=600, blank=True, null=True)
    
    '''

    nombre = forms.CharField(required=True, max_length=3000, widget=forms.TextInput(
        attrs={'class': 'form-control'}
        ))
    apellido = forms.CharField(required=True, max_length=3000, widget=forms.TextInput(
        attrs={'class': 'form-control'}
        ))
    fecha_nacimiento = forms.DateField(required=False, widget=forms.DateInput(
        attrs={'class': 'form-control'}
    ))
    email = forms.CharField(required=True, max_length=300, widget=forms.TextInput(
        attrs={'class': 'form-control'}
        ))
    telefono = forms.CharField(required=True, max_length=300, widget=forms.TextInput(
        attrs={'class': 'form-control'}
        ))
    
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'fecha_nacimiento', 'email', 'telefono']
    