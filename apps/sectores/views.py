
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Sector
from .forms import SectorForm


class SectorCreateView(CreateView):

    model = Sector
    form_class = SectorForm
    template_name = 'sector_form.html'
