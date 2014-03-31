from django.shortcuts import render, render_to_response
from inventario.models import Herramienta
from inventario.models import Consumible
from django.conf import settings
from django.contrib import admin
from django.template import RequestContext

from inventario.models import Mueble
from inventario.models import Pld
from inventario.models import Computadora
from inventario.forms import ContactoForm, HerramientaForm, ConsumibleForm, MuebleForm, PldForm, ComputadoraForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):  
    return render_to_response('inicio.html', context_instance=RequestContext(request))


def lista_tool(request):
	herramienta = Herramienta.objects.all()
	return render_to_response('lista_herramientas.html',{'datos':herramienta})

def lista_consu(request):
	consum = Consumible.objects.all()
	return render_to_response('lista_consumibles.html',{'lista':consum}, context_instance=RequestContext(request))	

def sobre(request):
	html = "<html><body>* Anteproyecto sistema de Inventario FabLab Oaxaca *</body></html>"
	return HttpResponse(html)

def lista_furniture(request):
	mue = Mueble.objects.all()
	return render_to_response('lista_muebles.html',{'listamuebles':mue}, context_instance=RequestContext(request))

def lista_dlp(request):
	dispositivos = Pld.objects.all()
	return render_to_response('lista_dispositivos.html',{'lista':dispositivos}, context_instance=RequestContext(request))

def lista_computer(request):
	comp = Computadora.objects.all()
	return render_to_response('lista_computadoras.html',{'lista':comp}, context_instance=RequestContext(request))				

def usuarios(request):
    usuarios = User.objects.all()    
    return render_to_response('usuarios.html',{'usuarios':usuarios}, context_instance=RequestContext(request))


def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)    
		if formulario.is_valid():
			titulo = 'Mensaje desde el sistema de inventario FabLab Oaxaca'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
			correo = EmailMessage(titulo, contenido, to=['david.djdim@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contacto.html',{'formulario':formulario}, context_instance=RequestContext(request))	


def nueva_herramienta(request):
	if request.method=='POST':
		formulario = HerramientaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/herramientas')
	else:
		formulario = HerramientaForm()
	return render_to_response('herramientaform.html',{'formulario':formulario}, context_instance=RequestContext(request))		


def nuevo_consumible(request):
	if request.method=='POST':
		formulario = ConsumibleForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/consumibles')
	else:
		formulario = ConsumibleForm()
	return render_to_response('consumibleform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_mueble(request):
	if request.method=='POST':
		formulario = MuebleForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/muebles')
	else:
		formulario = MuebleForm()
	return render_to_response('muebleform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_dispositivo(request):
	if request.method=='POST':
		formulario = PldForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/dispositivos')
	else:
		formulario = PldForm()
	return render_to_response('pldform.html',{'formulario':formulario}, context_instance=RequestContext(request))			

def nueva_computadora(request):
	if request.method=='POST':
		formulario = ComputadoraForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/computadora')
	else:
		formulario = ComputadoraForm()
	return render_to_response('computadoraform.html',{'formulario':formulario}, context_instance=RequestContext(request))	

def nuevo_usuario(request):
	if request.method=='POST':
		formulario = UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))			

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method =='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))	
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()		
	return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))	

@login_required(login_url='/ingresar')	
def privado(request):
	usuario = request.user
	return render_to_response('privado.html',{'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')	
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/') 
	