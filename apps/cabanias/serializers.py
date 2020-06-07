from rest_framework import serializers

from .models import Cabania, Inventario

from apps.articulos.serializer import ArticuloSerializer


class InventarioSerializer(serializers.ModelSerializer):

    articulo = ArticuloSerializer()

    class Meta:

        model = Inventario
        fields = '__all__'


class CabaniaSerializer(serializers.ModelSerializer):

    inventario = InventarioSerializer(many=True)

    class Meta:

        model = Cabania
        fields = '__all__'
