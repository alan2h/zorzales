from rest_framework import serializers

from .models import Reserva

from apps.cabanias.serializers import CabaniaSerializer
from apps.clientes.serializers import ClienteSerializer


class ReservaSerializer(serializers.ModelSerializer):

    cabania = CabaniaSerializer()
    cliente = ClienteSerializer()

    class Meta:
        
        model = Reserva
        fields = '__all__'
