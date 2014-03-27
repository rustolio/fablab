from inventario.models import Herramienta
from inventario.models import Consumible
from inventario.models import Mueble
from inventario.models import Pld
from inventario.models import Computadora
from django.contrib import admin

admin.site.register(Herramienta)
admin.site.register(Consumible)
admin.site.register(Mueble)
admin.site.register(Pld)
admin.site.register(Computadora)

