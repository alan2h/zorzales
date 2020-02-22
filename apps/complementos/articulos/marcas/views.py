
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Marca
from .forms import MarcaForm


class MarcaCreateView(SuccessMessageMixin, CreateView):

    model = Marca
    template_name = 'marca_form.html'
    success_url = '/complementos/marcas/listado'
    success_message = 'La marca fue agregada con éxito.'
    form_class = MarcaForm


class MarcaListView(ListView):

    queryset = Marca.objects.all()
    template_name = 'marcas_list.html'


class MarcaDeleteView(DeleteView):

    model = Marca
    template_name = 'marca_delete_confirm.html'
    success_url = '/complementos/marcas/listado'


class MarcaUpdateView(SuccessMessageMixin, UpdateView):

    model = Marca
    template_name = 'marca_form.html'
    success_url = '/complementos/marcas/listado'
    success_message = 'La marca fue modificada con éxito.'
    form_class = MarcaForm
