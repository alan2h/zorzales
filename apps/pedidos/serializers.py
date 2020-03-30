
from rest_framework import serializers

from .models import Pedido, PedidoArticulo



class PedidoArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = PedidoArticulo
        fields = '__all__'


class PedidoSerializer(serializers.ModelSerializer):

    pedido_articulo = PedidoArticuloSerializer(many=True)

    class Meta:
        model = Pedido
        fields = '__all__'
