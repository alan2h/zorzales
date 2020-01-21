
from django.shortcuts import redirect 
from django.views.generic import TemplateView


class Ingreso(TemplateView):

    template_name = 'login.html'

    def post(self, request):

        print(request)
        print('==========================')
        return redirect('Dashboard')


class Dashboard(TemplateView):

    template_name = 'dashboard.html'
