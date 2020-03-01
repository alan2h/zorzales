from .models import Articulo
from rest_framework import serializers


class ArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articulo
        fields = '__all__'
