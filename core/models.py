from __future__ import unicode_literals
from django.contrib import admin
from django.core.validators import MinValueValidator
from django.db import models
import decimal
from django.contrib.auth.models import User
from datetime import date
from multiselectfield import MultiSelectField

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256, null=False)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=256, null=False)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    paquetes = models.IntegerField(null=True)
    unidadPaquete = models.IntegerField(null=True)
    sueltas = models.IntegerField(default=0)
    existencias = models.IntegerField(default=0)
    
class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadPaquetes = models.IntegerField()
    cantidadTotal = models.IntegerField(null=False)
    existencias = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
    
class Salida(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidadPaquetes = models.IntegerField()
    cantidadTotal = models.IntegerField(null=False)
    existencias = models.DecimalField(max_digits=50, decimal_places=2, blank=False, default=0, validators=[MinValueValidator(0)])
    
    