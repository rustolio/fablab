#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Herramienta(models.Model):
	nombre = models.CharField(max_length=50)
	numserie = models.CharField(max_length=50)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=30)
	estado = models.TextField(help_text='Indica el estado de la herramienta')
	imagenHerramientas = models.ImageField(upload_to='Herramientas', verbose_name='ImagenH')
	tiempo_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.nombre

class Consumible(models.Model):
	nombre = models.CharField(max_length=50)
	cantidad = models.CharField(max_length=50)
	imagenConsumible = models.ImageField(upload_to='Consumibles', verbose_name='ImagenC')
	tiempo_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.cantidad

class Mueble(models.Model):
	nombre = models.CharField(max_length=50)	
	color = models.CharField(max_length=20)	
	imagenMuebles = models.ImageField(upload_to='Muebles', verbose_name='ImagenM')
	tiempo_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.color

class Pld(models.Model):
	nombre = models.CharField(max_length=50)
	numserie = models.CharField(max_length=50)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=30)
	estado = models.TextField(help_text='Indica el estado del PLD')
	imagenPld = models.ImageField(upload_to='Plds', verbose_name='ImagenP')
	tiempo_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.numserie

class Computadora(models.Model):
	nombre = models.CharField(max_length=50)
	numserie = models.CharField(max_length=50)
	marca = models.CharField(max_length=20)
	modelo = models.CharField(max_length=30)
	estado = models.TextField(help_text='Indica el estado de la Computadora')
	imagenComputadora = models.ImageField(upload_to='Computadoras', verbose_name='ImagenPC')
	tiempo_registro = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.marca
