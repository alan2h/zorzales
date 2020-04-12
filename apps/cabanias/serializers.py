from rest_framework import serializers

from .models import Cabania, Inventario


class InventarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Inventario
        fields = '__all__'


class CabaniaSerializer(serializers.ModelSerializer):

    inventario = InventarioSerializer(many=True)

    class Meta:

        model = Cabania
        fields = '__all__'
