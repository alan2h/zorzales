from rest_framework import viewsets, status
from rest_framework.response import Response


from .models import Pedido, PedidoArticulo
from .serializers import PedidoSerializer, PedidoArticuloSerializer

from apps.articulos.models import Articulo


class PedidoViewSet(viewsets.ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request):
        
        '''
        request: 
        {'fecha': '2020-03-04', 'precio_compra': 73, 
        'articulos': [{'id': 15, 'cantidad': '3'}, {'id': 17, 'cantidad': '4'}]}
        '''
        fecha = request.data['fecha']
        if '/' in request.data['fecha']:
            fecha = request.data['fecha'].split('/')[2] + '-' + \
            request.data['fecha'].split('/')[1] + '-' + \
                 request.data['fecha'].split('/')[0]

        results_pedido = Pedido(
            fecha=fecha, 
            precio_compra=request.data['precio_compra'],
        )

        for articulos_pedidos in request.data['articulos']:
            articulo = Articulo.objects.get(pk=articulos_pedidos['id'])
            pedido = PedidoArticulo.objects.create(articulo=articulo, cantidad=articulos_pedidos['cantidad'])
            pedido.save()
            results_pedido.save()
            results_pedido.pedido_articulo.add(pedido)
        results_pedido.save()

        return Response({'ok': 'creado con exito'}, status=status.HTTP_201_CREATED)



class PedidoArticuloViewSet(viewsets.ModelViewSet):

    queryset = PedidoArticulo.objects.all()
    serializer_class = PedidoArticuloSerializer
