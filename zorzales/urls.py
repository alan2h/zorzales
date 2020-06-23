"""zorzales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="API de zorzales",
      default_version='v1',
      description="Pruebas para apis",
      contact=openapi.Contact(email="beckalan303@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Ingreso.as_view(), name='login'),
    path('salir', views.salir, name='logout'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('inicio', views.Dashboard.as_view(), name='dashboard'),
    path('clientes/', include('apps.clientes.urls')),
    path('articulos/', include('apps.articulos.urls')),
    path('pedidos/', include('apps.pedidos.urls')),
    path('reservas/', include('apps.reservas.urls')),
    path('cabanias/', include('apps.cabanias.urls')),
    path('compras/', include('apps.compras.urls')),
    path('proveedores/', include('apps.proveedores.urls')),
    # complementos
    path('complementos/marcas/', include('apps.complementos.articulos.marcas.urls')),
    path('complementos/rubros/', include('apps.complementos.articulos.rubros.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
