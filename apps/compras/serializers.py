from rest_framework import serializers

from .models import Compra, CompraArticulo, TipoComprobante


class CompraSerializer(serializers.ModelSerializer):

    class Meta:

        model = Compra
        fields = '__all__'


class CompraArticuloSerializer(serializers.ModelSerializer):

    class Meta:

        model = CompraArticulo
        fields = '__all__'


class TipoComprobanteSerializer(serializers.ModelSerializer):


    class Meta:

        model = TipoComprobante
        fields = '__all__'
