from django.shortcuts import render, redirect

from django.views.generic import (
                                  ListView, 
                                  CreateView, 
                                  UpdateView,
                                  DetailView,
                                  DeleteView
                                  )

from django.contrib.messages.views import SuccessMessageMixin

from .models import Proveedor
from .forms import ProveedorForm

from apps.complementos.contactos.forms import ContactoForm
from apps.complementos.contactos.models import Contacto


class ProveedorListView(ListView):

    model = Proveedor
    template_name = 'proveedores_list.html'


class ProveedorCreateView(SuccessMessageMixin, CreateView):

    model = Proveedor
    template_name = 'proveedor_form.html'
    form_class = ProveedorForm
    success_url = '/proveedores/listado'
    success_message = 'El proveedor se registro con éxito'


class ProveedorUpdateView(SuccessMessageMixin, UpdateView):

    model = Proveedor
    template_name = 'proveedor_form.html'
    form_class = ProveedorForm
    success_url = '/proveedores/listado'
    success_message = 'El proveedor se modifico con éxito'


class ProveedorDetailView(DetailView):

    model = Proveedor
    template_name = 'proveedor_detail.html'



class ContactoCreateView(CreateView):

    model = Contacto
    form_class = ContactoForm
    template_name = 'contacto_form.html'
    success_url = '/proveedores/listado'
    success_message = 'El contacto se registro con éxito'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_proveedor"] = self.kwargs['id_proveedor'] 
        context['object_list'] = Proveedor.objects.get(pk=self.kwargs['id_proveedor']).contacto.all()
        return context
    
    def post(self, request, id_proveedor):

        #id_proveedor_contacto
        contacto_form = ContactoForm(data=self.request.POST)
        object_list = Proveedor.objects.get(pk=id_proveedor).contacto.all()
        proveedor = Proveedor.objects.get(pk=id_proveedor)
        if contacto_form.is_valid():
            contacto = contacto_form.save()
            proveedor.contacto.add(contacto)
            proveedor.save()
            return redirect('/proveedores/contactos/{}'.format(id_proveedor))
        else:
            return render('contacto_form.html', 
                          context={
                              'form': contacto_form,
                              'object_list': object_list
                           })


class ContactoDeleteView(DeleteView):

    model = Contacto
    template_name = 'contacto_delete_confirm.html'
    success_url = '/proveedores/listado'