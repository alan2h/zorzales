from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, ListView, \
    UpdateView, DeleteView, DetailView, View

from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch, cm


from django.contrib.messages.views import SuccessMessageMixin

from .models import Articulo
from .forms import ArticuloForm

from apps.lib.delete.delete_logic import DeleteLogic


class ArticuloCreateView(SuccessMessageMixin, CreateView):

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo_form.html'
    success_url = '/articulos/listado'
    success_message = 'El artículo se registro con éxito'


class ArticuloListView(ListView):

    queryset = Articulo.objects.filter(baja=False)
    template_name = 'articulos_list.html'
    paginate_by = 10

    def get_queryset(self):

        queryset = Articulo.objects.filter(baja=False)
        if 'search' in self.request.GET:
            if self.request.GET.get('search') != '':
                queryset = Articulo.objects.filter(descripcion__icontains=self.request.GET.get('search'), baja=False)
                if len(queryset) == 0:
                    queryset = Articulo.objects.filter(
                        codigo_barra__icontains=self.request.GET.get('search'), baja=False)
                    if len(queryset) == 0:
                        queryset = Articulo.objects.filter(
                            marca__descripcion__icontains=self.request.GET.get('search'), baja=False)
                        if len(queryset) == 0:
                            queryset = Articulo.objects.filter(
                                rubro__descripcion__icontains=self.request.GET.get('search'), baja=False)
        return queryset


class ArticuloUpdateView(SuccessMessageMixin, UpdateView):

    model = Articulo
    form_class = ArticuloForm
    template_name = 'articulo_form.html'
    success_url = '/articulos/listado'
    success_message = 'El artículo se modifico con éxito'


class ArticuloDeleteView(DeleteLogic, DeleteView):

    model = Articulo
    template_name = 'articulo_delete_confirm.html'
    success_url = '/articulos/listado'


class ArticuloDetailView(DetailView):

    model = Articulo
    template_name = 'articulo_detail.html'


class ArticuloReportePDF(View):

    def cabecera(self,pdf):
            #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
            archivo_imagen = settings.MEDIA_ROOT+'/logos/logo.png'
            #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
            pdf.drawImage(archivo_imagen, 40, 750, 120, 90,preserveAspectRatio=True)

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Código', 'Descripcion', 'Marca', 'Venta', 'Costo', 'Stock')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(articulo.codigo_barra, articulo.descripcion, articulo.marca, articulo.precio_venta,\
             articulo.precio_compra, articulo.stock) for articulo in Articulo.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm, 3 * cm, 3 * cm, 3 * cm, 3 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
        [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)

    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            pdf.setFont("Helvetica", 14)
            pdf.drawString(200, 770, u"REPORTE DE ARTICULOS")
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            y = 540
            self.tabla(pdf, y)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response