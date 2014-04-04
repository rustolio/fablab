#encoding: utf-8
from django.forms import ModelForm
from django import forms
from  inventario.models import Herramienta, Consumible, Mueble, Pld, Computadora

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Por favor, escribe aquí tu correo electrónico')
	mensaje = forms.CharField(widget=forms.Textarea)

class HerramientaForm(ModelForm):
	class Meta:
		model = Herramienta

class ConsumibleForm(ModelForm):
	class Meta:
		model = Consumible

class MuebleForm(ModelForm):
	class Meta:
		model = Mueble

class PldForm(ModelForm):
	class Meta:
		model = Pld

class ComputadoraForm(ModelForm):
	class Meta:
		model = Computadora


			