from app_arriendos.models import Usuarios, Direccion, Ubicacion, Tipo_usuario

def crear_usuario(rut: str, nombre: str, apellido: str, calle: str, numero: str, depto: str, region: str, comuna: str, tipo_usuario: str, telefono: str, correo: str) -> Usuarios:
    # Crear o obtener la ubicación
    ubicacion, created = Ubicacion.objects.get_or_create(
        nombre_region=region,
        nombre_comuna=comuna
    )
    
    # Crear la dirección
    direccion = Direccion.objects.create(
        calle=calle,
        numero=numero,
        depto=depto,
        id_ubicacion=ubicacion
    )
    
    # Obtener el tipo de usuario
    tipo_usuario_obj = Tipo_usuario.objects.get(tipo=tipo_usuario)
    
    # Crear el usuario
    usuario = Usuarios.objects.create(
        rut=rut,
        nombre=nombre,
        apellido=apellido,
        id_direccion=direccion,
        tipo_usuario=tipo_usuario_obj,
        telefono=telefono,
        correo=correo
    )
    
    return usuario

#listar usuarios
def listar_usuarios():
    usuarios = Usuarios.objects.select_related('tipo_usuario').all()
    for usuario in usuarios:
        print(f'Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Tipo de Usuario: {usuario.tipo_usuario.tipo}')


#actualizar usuario
def actualizar_usuario(rut: str, nombre: str = None, apellido: str = None, calle: str = None, numero: str = None, depto: str = None, region: str = None, comuna: str = None, tipo_usuario: str = None, telefono: str = None, correo: str = None):
    try:
        # Buscar el usuario por su RUT
        usuario = Usuarios.objects.get(rut=rut)
        
        # Actualizar los campos si se proporcionan nuevos valores
        if nombre:
            usuario.nombre = nombre
        if apellido:
            usuario.apellido = apellido
        if telefono:
            usuario.telefono = telefono
        if correo:
            usuario.correo = correo
        if tipo_usuario:
            tipo_usuario_obj = Tipo_usuario.objects.get(tipo=tipo_usuario)
            usuario.tipo_usuario = tipo_usuario_obj
        
        # Actualizar la dirección si se proporcionan nuevos valores
        if calle or numero or depto or region or comuna:
            direccion = usuario.id_direccion
            if calle:
                direccion.calle = calle
            if numero:
                direccion.numero = numero
            if depto is not None:
                direccion.depto = depto
            
            if region or comuna:
                ubicacion = direccion.id_ubicacion
                if region:
                    ubicacion.nombre_region = region
                if comuna:
                    ubicacion.nombre_comuna = comuna
                ubicacion.save()
                
            direccion.save()
        
        # Guardar los cambios en el usuario
        usuario.save()
        return usuario
    # excepción por si no encuentra el usuario mediante su rut
    except Usuarios.DoesNotExist:
        print('Usuario no encontrado')
        return None

# -> bool indica que la función devolverá un valor booleano (True o False) para ejecutar la excepción
def eliminar_usuario(rut: str) -> bool:
    try:
        # Buscar el usuario por su RUT
        usuario = Usuarios.objects.get(rut=rut)
        usuario.delete()
        print(f'Usuario con RUT {rut} eliminado exitosamente.')
        return True
    except Usuarios.DoesNotExist:
        print('Usuario no encontrado')
        return False