from datetime import date, timedelta

from django.http import JsonResponse

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
        result = []
        today = date.today()
        cabanias = Cabania.objects.all()
        i = 0
        for cabania in cabanias:
            pk = cabania.id
            i += 1
            reserva = Reserva.objects.filter(cabania__id=pk, fecha_ingreso=today)
            if not reserva.exists():
                reserva = Reserva.objects.filter(cabania__id=pk, fecha_ingreso__lt=today)
                if reserva.exists():
                    for r in reserva:
                        if r.fecha_salida >= today:
                            reserva_result = r
                            result.append({
                                'id':i,
                                'reserva': True,
                                'cabania': cabania.descripcion,
                                'fecha_ingreso': reserva_result.fecha_ingreso,
                                'hora_ingreso': reserva_result.hora_ingreso,
                                'dia_actual': today,
                                'cliente': reserva_result.cliente.nombre + ' ' + reserva_result.cliente.apellido,
                                'fecha_salida': reserva_result.fecha_salida
                            })
                        else:
                            result.append({
                            'id': i,
                            'reserva': False,
                            'cabania': cabania.descripcion,
                            'fecha_ingreso': '',
                            'hora_ingreso': '',
                            'dia_actual': today,
                            'cliente': '',
                            'fecha_salida': ''
                            })
                else:
                    result.append({
                        'id': i,
                        'reserva': False,
                        'fecha_ingreso': '',
                        'cabania': cabania.descripcion,
                        'hora_ingreso': '',
                        'dia_actual': today,
                        'cliente': '',
                        'fecha_salida': ''
                        })
            else:
                reserva_result = reserva.first()
                result.append({
                        'id':i,
                        'reserva': True,
                        'cabania': cabania.descripcion,
                        'fecha_ingreso': reserva_result.fecha_ingreso,
                        'hora_ingreso': reserva_result.hora_ingreso,
                        'dia_actual': today,
                        'cliente': reserva_result.cliente.nombre + ' ' + reserva_result.cliente.apellido,
                        'fecha_salida': reserva_result.fecha_salida
                    })
        print(result)
        return JsonResponse(result, safe=False)
