
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

# libs login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# libs security
from apps.lib.security.login_required import LoginRequired


class Ingreso(TemplateView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated: # si esta autenticado mandarle al sistema
            return redirect('/inicio')
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request, *args, **kwargs):

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST.get('username'), 
                                 password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('/inicio')

        return render(request, self.template_name, {'form': form})


class Dashboard(LoginRequired, TemplateView):

    template_name = 'dashboard.html'


def salir(request):

    logout(request)
    return redirect('/')