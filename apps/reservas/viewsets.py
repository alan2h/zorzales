from rest_framework import viewsets

from .serializers import ReservaSerializer
from .models import Reserva


class ReservaViewSet(viewsets.ModelViewSet):

    '''
        para guardar reservas de los alquileres
        la relacion entre cliente y alquiler
    '''

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
