
from rest_framework import viewsets

from .serializers import ClienteSerializer
from .models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = Cliente.objects.all()
        if 'buscador' in self.request.GET:
            if self.request.GET.get('buscador') != '':
                queryset = Cliente.objects.filter(nombre__icontains=
                self.request.GET.get('buscador'))
                if len(queryset) == 0:
                    queryset = Cliente.objects.filter(apellido__icontains=
                    self.request.GET.get('buscador'))
                    if len(queryset) == 0:
                        queryset = Cliente.objects.filter(numero_documento__icontains=
                        self.request.GET.get('buscador'))
        return queryset
    