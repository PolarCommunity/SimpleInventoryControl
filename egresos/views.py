from django.shortcuts import render, redirect
from decimal import Decimal
from .models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django import forms
from django.views.generic import *
from django.contrib import auth
from SimpleInventoryControl import settings
from django.db.models import Q
from .forms import *
from general.models import ArticuloSede, Articulo
from django.contrib.auth.models import User

class lista_egreso_sede(LoginRequiredMixin, ListView):
    model = Egreso
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'egreso/egreso_sede_lista.html'
    def get_queryset(self):
        try:
            return Egreso.objects.filter(descripcion__icontains=self.args[0]).order_by('-pk')
        except Exception as e:
            print(e)
            return super(lista_egreso_sede, self).get_queryset().order_by('-pk')

class lista_egreso_super(LoginRequiredMixin, ListView):
    model = Egreso
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'egreso/egreso_super_lista.html'
    def get_queryset(self):
        try:
            return Egreso.objects.filter(descripcion__icontains=self.args[0]).order_by('-pk')
        except Exception as e:
            print(e)
            return super(lista_egreso_super, self).get_queryset().order_by('-pk')

@login_required
def crear_egreso(request):
    if request.method=="POST":
        form = CrearEgresoForm(request.POST)
        if form.is_valid():
            egreso = form.save()
            return HttpResponseRedirect(reverse('crear_detalle_egreso', args={egreso.pk}))
    else:
        form = CrearEgresoForm(initial = {'user':request.user, 'sede':request.user.sedeusuario.sede})
        form.fields['user'].widget = forms.HiddenInput()
        form.fields['sede'].widget = forms.HiddenInput()
        form.fields['total'].widget = forms.HiddenInput()
        return render(request, 'egreso/egreso_form.html', {'form':form})

@login_required
def crear_detalle_egreso(request, pk):
    instance = get_object_or_404(Egreso, pk=pk)
    try:
        lista = DetalleEgreso.objects.filter(egreso=pk)
    except Exception as e:
        lista = False
    if request.method == 'POST':
        form = CrearDetalleEgresoForm(request.POST)
        try:
            for i in lista:
                if i.articulo.pk == int(request.POST['articulo']):
                    mensaje = "Ya ha ingresado este artículo"
                    form = CrearDetalleEgresoForm(initial = {'egreso':pk})
                    form.fields['egreso'].widget = forms.HiddenInput()
                    form.fields['total'].widget = forms.HiddenInput()
                    form.fields['articulo'].queryset = ArticuloSede.objects.filter(sede=Sede.objects.get(pk=request.user.sedeusuario.sede.pk))
                    return render(request, 'egreso/detalle_egreso_form.html', {'form':form, 'mensaje':mensaje, 'lista':lista, 'egreso':instance})
        except Exception as e:
            raise
        articulosede = ArticuloSede.objects.get(pk = int(request.POST['articulo']))
        articulo = Articulo.objects.get(pk=articulosede.articulo.pk)
        if form.is_valid():
            if Decimal(request.POST['cantidad']) > articulosede.cantidad:
                mensaje = "No cuenta con la cantidad suficiente de este artículo, usted tiene: " + str(articulosede.cantidad)
                form = CrearDetalleEgresoForm(initial = {'egreso':pk})
                form.fields['egreso'].widget = forms.HiddenInput()
                form.fields['total'].widget = forms.HiddenInput()
                form.fields['articulo'].queryset = ArticuloSede.objects.filter(sede=Sede.objects.get(pk=request.user.sedeusuario.sede.pk))
                return render(request, 'egreso/detalle_egreso_form.html', {'form':form, 'mensaje':mensaje, 'lista':lista, 'egreso':instance})
            detalle = form.save()
            detalle.total = detalle.cantidad * detalle.articulo.articulo.precio
            articulosede.cantidad -= detalle.cantidad
            articulosede.save()
            articulo.cantidad -= detalle.cantidad
            articulo.save()
            detalle.save()
            egreso = Egreso.objects.get(pk=pk)
            egreso.total += detalle.total
            egreso.save()
            return HttpResponseRedirect(reverse('crear_detalle_egreso', args={pk}))
    else:
        form = CrearDetalleEgresoForm(initial = {'egreso':pk})
        form.fields['egreso'].widget = forms.HiddenInput()
        form.fields['total'].widget = forms.HiddenInput()
        form.fields['articulo'].queryset = ArticuloSede.objects.filter(sede=Sede.objects.get(pk=request.user.sedeusuario.sede.pk))
        return render(request, 'egreso/detalle_egreso_form.html', {'form':form, 'lista':lista, 'egreso':instance})

@login_required
def ver_egreso(request, pk):
    egreso = get_object_or_404(Egreso, pk=pk)
    try:
        lista = DetalleEgreso.objects.filter(egreso=pk)
    except Exception as e:
        print(e)
        lista = False
    return render(request, 'egreso/detalle_egreso_form.html', {'lista':lista, 'egreso':egreso})

@login_required
def eliminar_detalle_egreso(request, pk):
    detalle = get_object_or_404(DetalleEgreso, pk=pk)
    egreso = Egreso.objects.get(pk=detalle.egreso.pk)
    articulo_aumentar = ArticuloSede.objects.get(pk = detalle.articulo.pk)
    articulo_general = Articulo.objects.get(pk = detalle.articulo.articulo.pk)
    articulo_aumentar.cantidad += detalle.cantidad
    articulo_general.cantidad += detalle.cantidad
    articulo_aumentar.save()
    articulo_general.save()
    detalle.delete()
    return redirect(reverse('crear_detalle_egreso', args={egreso.pk}))
