from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
import datetime

from .serializers import ReservaSerializer
from .models import Reserva

from apps.clientes.models import Cliente
from apps.cabanias.models import Cabania

from apps.lib.api_rest import StandardResultsSetPagination


class ReservaViewSet(viewsets.ModelViewSet):

    '''
        para guardar reservas de los alquileres
        la relacion entre cliente y alquiler
    '''

    queryset = Reserva.objects.filter(activo=True)
    serializer_class = ReservaSerializer
    pagination_class = StandardResultsSetPagination

    def create(self, request):
        '''
        methods: create
        {'cabania': 1, 'cliente': 1, 
        'fecha_ingreso': '2020-04-28', 
        'hora_ingreso': '2020-04-26T13:03:03.000Z', 
        'observacion': ''}
        '''
        errors = []

        if request.data.get('cabania') == '':
            errors.append('cabania')

        if request.data.get('cliente') == '':
            errors.append('cliente')

        if request.data.get('fecha_ingreso') == None:
            errors.append('fecha_ingreso')

        if request.data.get('hora_ingreso') == None:
            errors.append('hora_ingreso')

        if request.data.get('fecha_salida') == None:
            errors.append('fecha_salida')

        if len(errors) == 0:
            cabania = Cabania.objects.get(pk=request.data.get('cabania'))
            cliente = Cliente.objects.get(pk=request.data.get('cliente'))
            reserva = Reserva.objects.create(
                cabania=cabania,
                cliente=cliente,
                fecha_ingreso=request.data.get('fecha_ingreso'),
                hora_ingreso=request.data.get('hora_ingreso').split('T')[1],
                fecha_salida=request.data.get('fecha_salida')
            )
            return Response({'ok': '200'}, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def get_reserva_cabania(self, request, pk=None):
        """
        Return a list of bookings
        """
        print(self.request.query_params)
        response = {'fecha_ingreso': '', 'fecha_salida': ''}
        booking = Reserva.objects.filter(cabania__id=self.request.query_params.get('cabania'), fecha_ingreso__gte=datetime.datetime.now()).order_by('-id')
        if booking.exists():
            response = {
                'fecha_ingreso': booking[0].fecha_ingreso,
                'fecha_salida': booking[0].fecha_salida
            }
        return Response(response)


    @action(detail=True, methods=['post'])
    def set_reserva_web(self, request, pk=None):
        '''
        {'fecha_ingreso': '2020-08-04T03:00:00.000Z', 
        'fecha_salida': '2020-08-27T03:00:00.000Z', 
        'hora_ingreso': '', 
        'cabania': '3', 
        'username': 'admin'}
        '''
        errors = []

        if request.data.get('cabania') == '':
            errors.append('cabania')

        if request.data.get('fecha_ingreso') == None:
            errors.append('fecha_ingreso')

        if request.data.get('fecha_salida') == None:
            errors.append('fecha_salida')

        if len(errors) == 0:
            cabania = Cabania.objects.get(pk=request.data.get('cabania'))

            cliente = Cliente.objects.filter(user__username=request.data.get('username')).first()

            reserva_filter = Reserva.objects.filter(
                fecha_ingreso__range=[request.data.get('fecha_ingreso').split('T')[0], request.data.get('fecha_salida').split('T')[0]],
                cabania__id=request.data.get('cabania')
            )

            if reserva_filter.exists():
                errors.append('reserva_repetida')
                return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                reserva_filter = Reserva.objects.filter(
                    fecha_salida__range=[request.data.get('fecha_ingreso').split('T')[0], request.data.get('fecha_salida').split('T')[0]],
                    cabania__id=request.data.get('cabania')
                )
                if reserva_filter.exists():
                    errors.append('reserva_repetida')
                    return Response(errors, status=status.HTTP_400_BAD_REQUEST)

            reserva = Reserva.objects.create(
                cabania=cabania,
                cliente=cliente,
                fecha_ingreso=request.data.get('fecha_ingreso').split('T')[0],
                hora_ingreso=request.data.get('fecha_ingreso').split('T')[1],
                fecha_salida=request.data.get('fecha_salida').split('T')[0]
            )
            return Response({'ok': '200'}, status=status.HTTP_201_CREATED)
        else:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        


    def get_queryset(self):
        queryset = Reserva.objects.filter(activo=True)
        if 'buscador' in self.request.query_params:
            if self.request.query_params.get('buscador') != '':
                queryset = Reserva.objects.filter(cliente__nombre__icontains=self.request.query_params.get('buscador'), activo=True)
                if len(queryset) == 0:
                    queryset = Reserva.objects.filter(cliente__apellido__icontains=self.request.query_params.get('buscador'), activo=True)
                    if len(queryset) == 0:
                        queryset = Reserva.objects.filter(activo=True)
        return queryset
