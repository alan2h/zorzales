
from rest_framework import viewsets

from .models import Cabania
from .serializers import CabaniaSerializer


class CabaniaViewSet(viewsets.ModelViewSet):

    queryset = Cabania.objects.all()
    serializer_class = CabaniaSerializer
