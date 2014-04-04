from django.contrib import admin
from inventario.models import Herramienta
from inventario.models import Consumible
from inventario.models import Mueble
from inventario.models import Pld
from inventario.models import Computadora

# Register your models here.

admin.site.register(Herramienta)
admin.site.register(Consumible)
admin.site.register(Mueble)
admin.site.register(Pld)
admin.site.register(Computadora)