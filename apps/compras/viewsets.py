
from .models import CompraArticulo, Compra, TipoComprobante

from rest_framework import viewsets

from .serializers import CompraArticuloSerializer, CompraSerializer, TipoComprobanteSerializer


class CompraViewSet(viewsets.ModelViewSet):

    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

