from .models import Articulo
from rest_framework import serializers

# complementos
from apps.complementos.articulos.marcas.models import Marca
from apps.complementos.articulos.rubros.models import Rubro


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'


class RubroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rubro
        fields = '__all__'


class ArticuloSerializer(serializers.ModelSerializer):

    marca = MarcaSerializer(many=False)
    rubro = RubroSerializer(many=False)

    class Meta:
        model = Articulo
        fields = '__all__'
