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
            print(user.username)
            SedeUsuario.objects.create(user=user, sede=Sede.objects.get(pk=int(request.POST['sede'])))
            mensaje = "Usuario creado exitoamente"
            return render(request, "usuario/register.html", {'mensaje':mensaje, 'sede':sede})
    else:
        return render(request, 'no_permitido.html')

def Home(request):
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
            return User.objects.filter(Q(username__icontains=self.args[0]) | Q(first_name__icontains=self.args[0]) | Q(last_name__icontains=self.args[0]) | Q(sede__nombre__icontains=self.args[0])).order_by('username')
        except:
            return super(lista_usuario, self).get_queryset().order_by('username')

class lista_sede(LoginRequiredMixin, ListView):
    model = Sede
    paginate_by = 50
    login_url = settings.LOGIN_URL
    template_name = 'general/sede/lista_sede.html'
    def get_queryset(self):
        try:
            return Articulo.objects.filter(Q(nombre__icontains=self.args[0]) | Q(direccion__icontains=self.args[0])).order_by('nombre')
        except:
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
        return render(request, 'no_permitido.html', {'form':form})

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
        lista = Sede_Articulo.objects.filter(sede=pk)
        return render(request, 'general/lista_sede_articulo.html', {'lista':lista})
    else:
        return render(request, 'no_permitido.html')

@login_required
def lista_sede_articulo(request):
    lista = Sede_Articulo.objects.filter(sede=request.user.sedeusuario.sede)
    return render(request, 'general/usuarios/lista_sede_articulo.html', {'lista':lista})

@login_required
def lista_sede_usuario_super(request, pk):
    if request.user.is_superuser:
        lista = SedeUsuario.objects.filter(sede=pk)
        return render(request, 'general/usuarios/lista_sede_usuario.html', {'lista':lista})
    else:
        return render(request, 'no_permitido.html')
