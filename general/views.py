from django.shortcuts import render
from decimal import Decimal
from .models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django import forms

# Create your views here.
@login_required
def Register(request):
    if request.method == "GET":
        return render(request, 'usuario/register.html')
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        auth.models.User.objects.create_user(username, email, password).save()
        user=auth.authenticate(username = username, password = password)
        auth.login(request, user)
        sede = Sede.objects.get(pk=request.POST['sede'])
        mensaje = "Usuario creado exitoamente"
        return render(request, "general/usuario/register.html", {'mensaje':mensaje})

def Home(request):
    if request.user.is_authenticated:
        return render(request, "base.html")
    else:
        if request.method == "GET":
            return render(request, "base.html")
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
                    return render(request, "base.html", {"mensaje": "Tu cuenta ha sido deshabilitada"})
            else:
                return render(request, "base.html", {"mensaje": "Usuario o contraseña incorrecta"})

@login_required
def Logout(request):
    auth.logout(request)
    return redirect("/")

@login_required
def lista_sede(request):
    print("hola")
    if request.user.is_superuser:
        try:
            sede = Sede.objects.all()
        except Exception as e:
            sede = False
        return render(request, 'general/sede/lista_sede.html', {'lista':sede})
    else:
        return render(request, 'no_permitido.html')

@login_required
def crear_sede(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CrearSedeForm()
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
            form.fields['nombre'].widget = forms.HiddenInput
            return render(request, 'general/sede/sede_form.html', {'form':form})
    else:
        return render(request, 'no_permitido.html')

@login_required
def lista_articulo(request):
    if request.user.is_superuser:
        articulo = Articulo.objects.all()
        return render(request, 'general/articulo/lista_articulo.html', {'lista':articulo})
    else:
        return render(request, 'no_permitido.html')

@login_required
def crear_articulo(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            if request.POST['descripcion']:
                descripcion = request.POST['descripcion']
                DescripcionArticulo.objects.create(articulo=Articulo.objects.get(pk=int(request.POST['articulo']), descripcion=descripcion))
            form = CrearArticuloForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('lista_articulo'))
        else:
            form = CrearArticuloForm()
            form.fields['cantidad'].widget = forms.HiddenInput()
            return render(request, 'general/articulo/articulo_form.html')
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
