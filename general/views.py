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
from django.contrib.auth.models import User

# Create your views here.
@login_required
def Register(request):
    if request.user.is_superuser:
        sede = Sede.objects.all()
        if request.method == "GET":
            return render(request, 'usuario/register.html', {'sede':sede})
        elif request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            email = request.POST["email"]
            auth.models.User.objects.create_user(username, email, password).save()
            user = User.objects.get(username=request.POST['username'])
            user.first_name=request.POST['nombres']
            user.last_name=request.POST['apellidos']
            user.save()
            SedeUsuario.objects.create(user=user, sede=Sede.objects.get(pk=int(request.POST['sede'])))
            mensaje = "Usuario creado exitoamente"
            return render(request, "usuario/register.html", {'mensaje':mensaje, 'sede':sede})
    else:
        return render(request, 'no_permitido.html')

def Home(request):
    sedes = Sede.objects.all()
    if request.user.is_authenticated:
        return render(request, "home.html")
    else:
        if request.method == "GET":
            return render(request, "usuario/login.html")
        elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    next = "/home"
                    if "next" in request.GET:
                        next = request.GET["next"]
                    if next == None or next == "":
                        next = "/"
                    return redirect(next)
                else:
                    return render(request, "usuario/login.html", {"mensaje": "Tu cuenta ha sido deshabilitada"})
            else:
                return render(request, "usuario/login.html", {"mensaje": "Usuario o contraseña incorrecta"})

@login_required
def Logout(request):
    auth.logout(request)
    return redirect("/")

class lista_usuario(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'general/usuario/lista_sede_usuario.html'
    def get_queryset(self):
        try:
            return User.objects.filter(Q(username__icontains=self.args[0]) | Q(first_name__icontains=self.args[0]) | Q(last_name__icontains=self.args[0])).order_by('username')
        except Exception as e:
            return super(lista_usuario, self).get_queryset().order_by('username')

class lista_sede(LoginRequiredMixin, ListView):
    model = Sede
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'general/sede/lista_sede.html'
    def get_queryset(self):
        try:
            return Sede.objects.filter(Q(nombre__icontains=self.args[0]) | Q(direccion__icontains=self.args[0])).order_by('nombre')
        except Exception as e:
            return super(lista_sede, self).get_queryset().order_by('nombre')

@login_required
def crear_sede(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CrearSedeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('lista_sede'))
        else:
            form = CrearSedeForm()
            return render(request, 'general/sede/sede_form.html', {'form':form})
    else:
        return render(request, 'no_permitido.html')

@login_required
def actualizar_sede(request, pk):
    if request.user.is_superuser:
        sede = get_object_or_404(Sede, pk=pk)
        if request.method == 'POST':
            form = CrearSedeForm(request.POST, instance=sede)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('lista_sede'))
        else:
            form = CrearSedeForm(instance = sede)
            form.fields['nombre'].widget = forms.HiddenInput()
            return render(request, 'general/sede/sede_form.html', {'form':form})
    else:
        return render(request, 'no_permitido.html')

@login_required
def eliminar_usuario(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect(reverse('lista_usuario'))
    else:
        return render(request, 'no_permitido')

class detalle_sede(LoginRequiredMixin, DetailView):
    model = Sede
    template_name = 'general/sede/detalle_sede.html'

class lista_articulo(LoginRequiredMixin, ListView):
    model = Articulo
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'general/articulo/lista_articulo.html'
    def get_queryset(self):
        try:
            return Articulo.objects.filter(Q(nombre__icontains=self.args[0]) | Q(codigo__icontains=self.args[0])).order_by('nombre')
        except Exception as e:
            return super(lista_articulo, self).get_queryset().order_by('nombre')

class detalle_articulo(LoginRequiredMixin, DetailView):
    model = Articulo
    template_name = 'general/articulo/detalle_articulo.html'

@login_required
def crear_articulo(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            descripcion = request.POST['descripcion']
            print(descripcion)
            form = CrearArticuloForm(request.POST)
            if form.is_valid():
                articulo = form.save()
                if descripcion:
                    descripcion = request.POST['descripcion']
                    DescripcionArticulo.objects.create(articulo=articulo, descripcion=descripcion)
                return HttpResponseRedirect(reverse('lista_articulo'))
        else:
            form = CrearArticuloForm()
            form.fields['cantidad'].widget = forms.HiddenInput()
            form.fields['precio'].widget = forms.HiddenInput()
            return render(request, 'general/articulo/articulo_form.html', {'form':form})
    else:
        return render(request, 'no_permitido.html')

@login_required
def actualizar_articulo(request, pk):
    if request.user.is_superuser:
        articulo = get_object_or_404(Articulo, pk=pk)
        if request.method=='POST':
            if request.POST['descripcion']:
                descripcion = request.POST['descripcion']
                try:
                    DescripcionArticulo.objects.create(articulo=Articulo.objects.get(pk=int(request.POST['articulo']), descripcion=descripcion))
                except Exception as e:
                    desc = DescripcionArticulo.objects.get(articulo=Articulo.objects.get(pk=int(request.POST['articulo'])))
                    desc.descripcion = descripcion
                    desc.save()
            form = CrearArticuloForm(request.POST, instance=articulo)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('lista_articulo'))
        else:
            form = CrearArticuloForm(instance=articulo)
            form.fields['cantidad'].widget = forms.HiddenInput()
            form.fields['precio'].widget = forms.HiddenInput()
            return render(request, 'general/articulo/articulo_form.html', {'form':form})
    else:
        return render(request, 'no_permitido.html')

@login_required
def lista_sede_articulo_super(request, pk):
    if request.user.is_superuser:
        lista = ArticuloSede.objects.filter(sede=pk)
        return render(request, 'general/articulo/lista_sede_articulo.html', {'object_list':lista})
    else:
        return render(request, 'no_permitido.html')

@login_required
def lista_sede_articulo(request):
    try:
        lista = ArticuloSede.objects.filter(sede=request.user.sedeusuario.sede)
    except Exception as e:
        print(e)
        lista=False
    return render(request, 'general/articulo/lista_sede_articulo.html', {'object_list':lista})

@login_required
def lista_sede_usuario_super(request, pk):
    if request.user.is_superuser:
        lista = SedeUsuario.objects.filter(sede=pk)
        return render(request, 'general/usuarios/lista_sede_usuario.html', {'lista':lista})
    else:
        return render(request, 'no_permitido.html')

@login_required
def seleccion_sede_lista_articulo(request):
    if request.user.is_superuser:
        sede = Sede.objects.all()
        return render(request, 'general/articulo/seleccion_sede_lista_articulo.html', {'sede':sede})

@login_required
def lista_transferencia(request, par=""):
    print(par)
    try:
        lista = TransferenciaArticuloSede.objects.filter(Q(sede_destino__nombre__icontains=par) | Q(descripcion__icontains=par), sede_origen=request.user.sedeusuario.sede).order_by('-pk')
    except Exception as e:
        lista = TransferenciaArticuloSede.objects.filter(sede_origen=request.user.sedeusuario.sede).order_by('-pk')
    return render(request, 'general/transferencia/lista_transferencia.html', {'object_list':lista})

@login_required
def crear_transferencia_articulo_sede(request):
    if request.method == 'POST':
        form = CrearTransferenciaForm(request.POST)
        if request.POST['sede_origen'] == request.POST['sede_destino']:
            form = CrearTransferenciaForm(initial={'sede_origen':request.user.sedeusuario.sede})
            form.fields['sede_origen'].widget = forms.HiddenInput()
            mensaje = "No puede realizar una transferencia a su propia sede"
            return render(request, 'general/transferencia/transferencia_form.html', {'form':form, 'mensaje':mensaje})
        if form.is_valid():
            tr = form.save()
            return HttpResponseRedirect(reverse('crear_detalle_transferencia_articulo_sede', args={tr.pk}))
    else:
        form = CrearTransferenciaForm(initial={'sede_origen':request.user.sedeusuario.sede})
        form.fields['sede_origen'].widget = forms.HiddenInput()
        return render(request, 'general/transferencia/transferencia_form.html', {'form':form})

@login_required
def crear_detalle_transferencia_articulo_sede(request, pk):
    transferencia = get_object_or_404(TransferenciaArticuloSede, pk=pk)
    try:
        lista = DetalleTransferenciaArticuloSede.objects.filter(transferencia=transferencia)
    except Exception as e:
        lista=False
    if request.method == "POST":
        form = CrearDetalleTransferenciaForm(request.POST)
        sede_articulo = ArticuloSede.objects.get(pk=request.POST['articulo'])
        articulo = Articulo.objects.get(pk=sede_articulo.articulo.pk)
        if form.is_valid():
            if int(request.POST['cantidad']) > sede_articulo.cantidad:
                mensaje = "No cuenta con la cantidad suficiente de este artículo"
                form.fields['transferencia'].widget = forms.HiddenInput()
                return render(request, 'general/transferencia/detalle_transferencia_form.html', {'form':form, 'transferencia':transferencia, 'lista':lista, 'mensaje':mensaje})
            detalle = form.save()
            try:
                sede_articulo_aumentar = ArticuloSede.objects.get(articulo=articulo, sede=Sede.objects.get(pk=transferencia.sede_destino.pk))
                sede_articulo_aumentar.cantidad += detalle.cantidad
                sede_articulo_aumentar.save()
            except Exception as e:
                print(articulo.nombre)
                try:
                    sede_articulo_aumentar = ArticuloSede.objects.create(cantidad=Decimal(request.POST['cantidad']), articulo=articulo, sede=Sede.objects.get(pk=transferencia.sede_destino))
                except Exception as e:
                    print(e)
            sede_articulo.cantidad -= detalle.cantidad
            sede_articulo.save()
            return HttpResponseRedirect(reverse('crear_detalle_transferencia_articulo_sede', args={pk}))
    else:
        form = CrearDetalleTransferenciaForm(initial = {'transferencia':transferencia})
        form.fields['transferencia'].widget = forms.HiddenInput()
        form.fields['articulo'].queryset = ArticuloSede.objects.filter(sede=Sede.objects.get(pk=transferencia.sede_origen.pk))
        return render(request, 'general/transferencia/detalle_transferencia_form.html', {'form':form, 'transferencia':transferencia, 'lista':lista})


@login_required
def imp_inventario_sede(request):
        lista = ArticuloSede.objects.filter(sede=request.user.sedeusuario.sede)
        mensaje = request.GET.get('mensaje', None)
        if mensaje:
            return redirect(reverse('lista_sede_articulo'))
        return render(request, 'general/impresion/lista_sede_articulo.html', {'object_list':lista})

@login_required
def imp_inventario(request):
        lista = Articulo.objects.all()
        mensaje = request.GET.get('mensaje', None)
        if mensaje:
            return redirect(reverse('lista_articulo'))
        return render(request, 'general/impresion/lista_articulo.html', {'object_list':lista})

@login_required
def imp_transferencia(request,pk):
        transferencia = TransferenciaArticuloSede.objects.get(pk=pk)
        detalle = DetalleTransferenciaArticuloSede.objects.filter(transferencia=transferencia.pk)
        mensaje = request.GET.get('mensaje', None)
        if mensaje:
            return redirect(reverse('lista_transferencia'))
        return render(request, 'general/impresion/lista_transferencia.html', {'transferencia':transferencia,'lista':detalle})
