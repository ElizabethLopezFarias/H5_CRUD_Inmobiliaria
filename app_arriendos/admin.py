from django.contrib import admin
from .models import Tipo_inmueble, Tipo_usuario, Ubicacion, Direccion, Usuarios, Inmuebles

admin.site.register(Tipo_inmueble)
admin.site.register(Tipo_usuario)
admin.site.register(Ubicacion)
admin.site.register(Direccion)
admin.site.register(Inmuebles)

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_usuario', 'rut', 'nombre',  'apellido',  'id_direccion',  'telefono', 'correo')

