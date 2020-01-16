
from django.views.generic import TemplateView


class Ingreso(TemplateView):

    template_name = 'login.html'


class Dashboard(TemplateView):

    template_name = 'base.html'