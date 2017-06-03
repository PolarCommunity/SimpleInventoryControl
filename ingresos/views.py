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

    def get_success_url(self):
        return reverse('crear_detalle_ingreso',args=(self.object.id,))

class ListaIngreso(LoginRequiredMixin, ListView):
    model = Ingreso
    paginate_by = 30
    login_url = settings.LOGIN_URL
    def get_queryset(self):
        try:
            return Ingreso.objects.filter(comprobante__icontains=self.args[0]).order_by('-pk')
        except Exception as e:
            print(e)
            return super(ListaIngreso, self).get_queryset().order_by('-pk')

@login_required
def crear_detalle_ingreso(request, pk):
    ingreso = Ingreso.objects.get(pk=pk)
    detalles = DetalleIngreso.objects.filter(ingreso=pk)
    if request.method=='POST':
        form = IngresoDetalleForm(request.POST)
        articulo = Articulo.objects.get(pk=int(request.POST['articulo']))
        for i in detalles:
            if i.articulo.pk == articulo.pk:
                form = IngresoDetalleForm(initial = {'ingreso':ingreso.pk})
                detalles = DetalleIngreso.objects.filter(ingreso=pk)
                status = 1
                mensaje = "Ya ingreso este articulo"
                context = Context({'ingreso':ingreso, 'form': form , 'detalles':detalles,'status':status, 'mensaje':mensaje})
                return render(request, 'ingresos/detalle_ingreso_form.html', context)

        if int(request.POST['cantidad']) < 1 or Decimal(request.POST['precio_unitario']) < 1:
            form = IngresoDetalleForm(initial = {'ingreso':ingreso.pk})
            detalles = DetalleIngreso.objects.filter(ingreso=pk)
            status = 2
            mensaje = "Ingrese un valor mayor a 0"
            context = Context({'ingreso':ingreso, 'form': form , 'detalles':detalles,'status':status, 'mensaje':mensaje})
            return render(request, 'ingresos/detalle_ingreso_form.html', context)

        if form.is_valid():
            detalle = form.save()
            detalle.precio_total += detalle.cantidad * detalle.precio_unitario
            detalle.save()
            ingreso.total += detalle.cantidad * detalle.precio_unitario
            ingreso.save()
            if(articulo.precio == 0):
                articulo.precio = detalle.precio_unitario
            else:
                articulo.precio = ((articulo.precio + detalle.precio_unitario)/2)
            articulo.cantidad += detalle.cantidad
            articulo.save()
            try:
                sedea = ArticuloSede.objects.get(articulo = articulo, sede__nombre="Central")
                sedea.cantidad += detalle.cantidad
                sedea.save()
            except:
                sede = Sede.objects.get(nombre="Central")
                ArticuloSede.objects.create(cantidad = detalle.cantidad, articulo=articulo, sede = sede)
            return HttpResponseRedirect(reverse('crear_detalle_ingreso', args={pk}))

        else:
            form = IngresoDetalleForm(initial = {'ingreso':ingreso.pk})
            detalles = DetalleIngreso.objects.filter(ingreso=pk)
            context = Context({'ingreso':ingreso, 'form': form , 'detalles':detalles})
            return render(request, 'ingresos/detalle_ingreso_form.html', context)

    else:
        form = IngresoDetalleForm(initial = {'ingreso':ingreso.pk})
        detalles = DetalleIngreso.objects.filter(ingreso=pk)
        context = Context({'ingreso':ingreso, 'form': form , 'detalles':detalles})
        return render(request, 'ingresos/detalle_ingreso_form.html', context)

@login_required
def eliminar_detalle_ingreso(request, pk):
    detalle = DetalleIngreso.objects.get(pk=pk)
    ingreso = Ingreso.objects.get(pk=detalle.ingreso.pk)
    articulo = Articulo.objects.get(pk=detalle.articulo.pk)
    sedea = ArticuloSede.objects.get(articulo = articulo, sede__nombre="Central")
    sedea.cantidad -= detalle.cantidad
    ingreso.total -= detalle.cantidad * detalle.precio_unitario
    articulo.cantidad -= detalle.cantidad
    if(articulo.precio == detalle.precio_unitario):
        articulo.precio = 0
    else:
        articulo.precio = ((articulo.precio*2)-detalle.precio_unitario)
    ingreso.save()
    articulo.save()
    sedea.save()
    detalle.delete()
    return HttpResponseRedirect(reverse('crear_detalle_ingreso', args={ingreso.pk}))
