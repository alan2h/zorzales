
from rest_framework import viewsets

from .serializer import ArticuloSerializer
from .models import Articulo

from apps.lib.api_rest import StandardResultsSetPagination


class ArticuloViewSet(viewsets.ModelViewSet):

    queryset = Articulo.objects.filter(baja=False)
    serializer_class = ArticuloSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        """
        busqued de los articulos segun su descripcion dentro 
        """
        articulos = Articulo.objects.filter(baja=False)
        if 'search' in self.request.GET:
            if self.request.GET.get('search') != '':
                search = self.request.GET['search']
                articulos = Articulo.objects.filter(descripcion__icontains=search)
                if len(articulos) == 0:
                    articulos = Articulo.objects.filter(marca__descripcion__icontains=search)
                    if len(articulos) == 0:
                        articulos = Articulo.objects.filter(rubro__descripcion__icontains=search)
        return articulos

