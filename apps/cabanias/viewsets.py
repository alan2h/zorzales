from datetime import date, timedelta

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Cabania
from .serializers import CabaniaSerializer

from apps.reservas.models import Reserva
from apps.reservas.serializers import ReservaSerializer


class CabaniaViewSet(viewsets.ModelViewSet):

    queryset = Cabania.objects.all()
    serializer_class = CabaniaSerializer


    @action(detail=True, methods=['get'])
    def get_reserva(self, request, pk=None):

        '''
            obtengo la reserva de acuerdo 
            a la fecha actual y a la cabania que intentan manejar

        '''
        reserva_result = []
        today = date.today()
        reserva = Reserva.objects.filter(cabania__id=pk, fecha_ingreso=today)
        if not reserva.exists():
            reserva = Reserva.objects.filter(cabania__id=pk, fecha_ingreso__lt=today)
            if reserva.exists():
                for r in reserva:
                    if r.fecha_salida >= today:
                        reserva_result = r
        else:
            reserva_result = reserva.first()

        if not reserva_result:
            return Response({
                'reserva': False,
                'fecha_ingreso': '',
                'hora_ingreso': '',
                'dia_actual': today,
                'cliente': '',
                'fecha_salida': ''
                })
        else:
            return Response({
                'reserva': True,
                'fecha_ingreso': reserva_result.fecha_ingreso,
                'hora_ingreso': reserva_result.hora_ingreso,
                'dia_actual': today,
                'cliente': reserva_result.cliente.nombre + ' ' + reserva_result.cliente.apellido,
                'fecha_salida': reserva_result.fecha_salida
            })
