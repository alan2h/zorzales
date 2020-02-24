
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Marca
from .forms import MarcaForm

from apps.lib.delete.delete_logic import DeleteLogic


class MarcaCreateView(SuccessMessageMixin, CreateView):

    model = Marca
    template_name = 'marca_form.html'
    success_url = '/complementos/marcas/listado'
    success_message = 'La marca fue agregada con éxito.'
    form_class = MarcaForm


class MarcaListView(ListView):

    queryset = Marca.objects.filter(baja=False)
    template_name = 'marcas_list.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = Marca.objects.filter(baja=False)
        print('entrar aca ')
        if 'search' in self.request.GET:
            if self.request.GET.get('search') != '':
                print(self.request.GET, '========')
                queryset = Marca.objects.filter(descripcion__contains=self.request.GET.get('search'),\
                     baja=False)
        return queryset


class MarcaDeleteView(DeleteLogic, DeleteView):

    model = Marca
    template_name = 'marca_delete_confirm.html'
    success_url = '/complementos/marcas/listado'


class MarcaUpdateView(SuccessMessageMixin, UpdateView):

    model = Marca
    template_name = 'marca_form.html'
    success_url = '/complementos/marcas/listado'
    success_message = 'La marca fue modificada con éxito.'
    form_class = MarcaForm
