from .models import Producto, Cliente
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.shortcuts import get_object_or_404, render


# Create your views here.

def index(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos': listado_productos}
    return render(request, 'pasteleria/index.html', carrito)

def frm_agregar_usuario(request):
        return render(request, 'pasteleria/frm_agregar_usuario.html')

def mendocinos(request):
    if request.user.has_perm('pasteleria.view_producto'):
        return render(request, 'pasteleria/mendocinos.html')
    else:
        return HttpResponse ("No posee permisos para ver esta pagina")

def torta_sanjorge(request):
    if request.user.has_perm('pasteleria.view_producto'):  
        return render(request, 'pasteleria/torta_sanjorge.html')
    else:
        return HttpResponse ("No posee permisos para ver esta pagina")

def caja_bombones(request):
    if request.user.has_perm('pasteleria.view_producto'):  
        return render(request, 'pasteleria/caja_bombones.html')
    else:
        return HttpResponse ("No posee permisos para ver esta pagina")

def iniciar_sesion(request):
    usuario = request.POST["usuario"]
    clave = request.POST["clave"]

    user = authenticate(request, username=usuario, password=clave)

    if user is not None:
        dj_login(request, user)
        return HttpResponseRedirect(reverse('pasteleria:index'))
    else:
        return HttpResponse("No se ingresaron datos validos")

def login(request):
    return render(request, 'pasteleria/login.html')


def registrar_usuario(request):
    nombres = request.POST['nombres']
    apellidoP = request.POST['apellidoP']
    apellidoM = request.POST['apellidoM'] 
    password = request.POST['password']   
    rut = request.POST['rut'] 
    email = request.POST['email'] 
    telefono = request.POST['telefono']
    direccion = request.POST['direccion'] 
    comuna = request.POST['comuna'] 
    region = request.POST['region'] 
    cliente = Cliente(nombres=nombres,apellidoP=apellidoP, apellidoM=apellidoM, password=password, rut=rut, email=email, telefono=telefono, direccion=direccion, comuna=comuna, region=region)
    cliente.save()
    return HttpResponseRedirect(reverse('pasteleria:index'))

def listar(request):
    return render(request, 'pasteleria/Listar_api.html',)


    




