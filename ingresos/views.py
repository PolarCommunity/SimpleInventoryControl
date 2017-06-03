from django.shortcuts import render, redirect
from django.views.generic import *
from .models import *
from SimpleInventoryControl import settings
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import *
from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.template import Context
from django import forms
from django.db.models import Sum
from django.db.models import Q
import time
# Create your views here.
class CrearIngreso(LoginRequiredMixin, CreateView):
    form_class = IngresoForm
    template_name = 'ingresos/ingreso_form.html'
    login_url = settings.LOGIN_URL
    success_url = reverse_lazy('ListaIngreso')
    def get(self, request):
        form = IngresoForm(initial = {'total':0, 'user':request.user})
        context = Context({'form': form})
        return render(request, 'ingresos/ingreso_form.html', context)

class ActualizarIngreso(LoginRequiredMixin, UpdateView):
    form_class = IngresoForm
    login_url = settings.LOGIN_URL
    success_url = reverse_lazy('ListaIngreso')

class EliminarIngreso(LoginRequiredMixin, DeleteView):
    model = Ingreso
    success_url = reverse_lazy('ListaIngreso')
    login_url = settings.LOGIN_URL

class ListaIngreso(LoginRequiredMixin, ListView):
    model = Ingreso
    paginate_by = 50
    login_url = settings.LOGIN_URL
