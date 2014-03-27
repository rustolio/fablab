from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^$','inventario.views.inicio'),  
    url(r'^herramientas$','inventario.views.lista_tool'),
    url(r'^herramientas/nueva$','inventario.views.nueva_herramienta'),

    url(r'^consumibles$','inventario.views.lista_consu'),   
    url(r'^consumibles/nuevo$','inventario.views.nuevo_consumible'),

	url(r'^muebles$','inventario.views.lista_furniture'),
    url(r'^muebles/nuevo$','inventario.views.nuevo_mueble'),
	
	url(r'^dispositivos$','inventario.views.lista_dlp'),
    url(r'^dispositivos/nuevo$','inventario.views.nuevo_dispositivo'),

	url(r'^computadoras$','inventario.views.lista_computer'),
    url(r'^computadora/nueva$','inventario.views.nueva_computadora'),

    url(r'^usuarios$','inventario.views.usuarios'),
    url(r'^usuario/nuevo$','inventario.views.nuevo_usuario'),
    url(r'^ingresar$','inventario.views.ingresar'),

    url(r'^privado$','inventario.views.privado'),
    url(r'^cerrar$','inventario.views.cerrar'),

    


    url(r'^contacto$','inventario.views.contacto'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$', 'inventario.views.sobre'),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}
    ),
)
