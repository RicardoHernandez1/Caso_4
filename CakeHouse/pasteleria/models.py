from django.db import models
from django.db.models.base import Model

# Create your models here.

class Cliente(models.Model):
    nombres      = models.CharField(max_length=50)
    apellidoP  = models.CharField(max_length=50)
    apellidoM  = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    rut       = models.IntegerField()
    email    = models.CharField(max_length=50)
    telefono = models.IntegerField()
    direccion    = models.CharField(max_length=50)
    comuna    = models.CharField(max_length=50)
    region   = models.CharField(max_length=50)


    def __str__(self):
        return self.nombres

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.IntegerField(default=0)
    activo = models.BooleanField(default=False)

    
    def __str__(self):
        return self.nombre

