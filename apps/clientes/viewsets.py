
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ClienteSerializer
from .models import Cliente
from .forms import ClienteForm


class ClienteViewSet(viewsets.ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        queryset = Cliente.objects.all()
        if 'buscador' in self.request.GET:
            if self.request.GET.get('buscador') != '':
                queryset = Cliente.objects.filter(nombre__icontains=
                self.request.GET.get('buscador'))
                if len(queryset) == 0:
                    queryset = Cliente.objects.filter(apellido__icontains=
                    self.request.GET.get('buscador'))
                    if len(queryset) == 0:
                        queryset = Cliente.objects.filter(numero_documento__icontains=
                        self.request.GET.get('buscador'))
        return queryset
    
    def create(self, request):
        '''
        {'nombre': 'asd', 
        'apellido': 'asd', 
        'fecha_nacimiento': '2020-08-03', 
        'numero_documento': '1231231', 
        'email': '', 
        'telefono': '123123', 
        'user': 'admin', 
        'password1': 'se242403germanb', 
        'password2': 'se242403germanb'}
        '''

        user = User.objects.create_user(
            request.data.get('user'),
            request.data.get('email'),
            request.data.get('password1')
        )
        user.save()

        cliente = Cliente.objects.create(
            nombre=request.data.get('nombre'),
            apellido=request.data.get('apellido'),
            fecha_nacimiento=request.data.get('fecha_nacimiento'),
            email=request.data.get('email'),
            numero_documento=request.data.get('numero_documento'),
            telefono=request.data.get('telefono'),
            user=user,
            confirmacion_correo=False
        )

        return Response({'response': '200'}, status=status.HTTP_201_CREATED)
