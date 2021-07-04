from .models import Producto, Cliente
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos': listado_productos}
    return render(request, 'pasteleria/index.html', carrito)

def frm_agregar_usuario(request):
        return render(request, 'pasteleria/frm_agregar_usuario.html')

def mendocinos(request):
    return render(request, 'pasteleria/mendocinos.html')

def torta_sanjorge(request):
    return render(request, 'pasteleria/torta_sanjorge.html')

def caja_bombones(request):
    return render(request, 'pasteleria/caja_bombones.html')

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


def login(request):
    return render(request, 'pasteleria/login.html')
    




