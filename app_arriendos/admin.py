from django.contrib import admin
from .models import Tipo_inmueble, Tipo_usuario, Ubicacion, Direccion, Usuarios, Inmuebles

admin.site.register(Tipo_inmueble)
admin.site.register(Tipo_usuario)
admin.site.register(Ubicacion)
admin.site.register(Direccion)
admin.site.register(Usuarios)
admin.site.register(Inmuebles)
