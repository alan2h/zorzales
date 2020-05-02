from rest_framework import viewsets, status
from rest_framework.response import Response

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

    queryset = Reserva.objects.all()
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
