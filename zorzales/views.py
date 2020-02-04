
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

# libs login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


class Ingreso(TemplateView):

    template_name = 'login.html'


    def post(self, request, *args, **kwargs):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'), 
                                 password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/inicio')

        return render(request, 'login.html', {'form': form})


class Dashboard(TemplateView):

    template_name = 'dashboard.html'


def salir(request):

    logout(request)
    return redirect('')