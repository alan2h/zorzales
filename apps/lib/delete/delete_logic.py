
from django.shortcuts import redirect
from datetime import datetime

from django.contrib import messages


class DeleteLogic(object):

    def delete(self, request, *args, **kwargs):
        
        print(self.model, '============')
        articulo = self.model.objects.get(pk=kwargs['pk'])
        articulo.baja = True
        articulo.fecha_baja = datetime.now()
        articulo.save()
        messages.warning(request, 'El registro se elimino con éxito')
        return redirect(self.success_url)
