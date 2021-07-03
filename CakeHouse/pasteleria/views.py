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

def registrar_usuario(request):
    nombres = request.POST['nombres']
    apellidoP = request.POST['apellidoP']
    apellidoM = request.POST['apellidoM']    
    rut = request.POST['rut'] 
    email = request.POST['email'] 
    telefono = request.POST['telefono']
    direccion = request.POST['direccion'] 
    comuna = request.POST['comuna'] 
    region = request.POST['region'] 
    cliente = Cliente(nombres=nombres,apellidoP=apellidoP, apellidoM=apellidoM, rut=rut, email=email, telefono=telefono, direccion=direccion, comuna=comuna, region=region)
    cliente.save()
    return HttpResponseRedirect(reverse('pasteleria:index'))

def mostrar_producto(request):
    listado_productos = Producto.objects.all()
    carrito = {'listado_productos': listado_productos}
    return render(request, 'pasteleria/mostrar_productos.html', carrito)

    




