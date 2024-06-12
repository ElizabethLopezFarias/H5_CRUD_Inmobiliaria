##SE ABORDA EL REQUERIMIENTO DE FORMA LITERAL, SEPARANDO LOS INMUEBLES POR REGIÓN Y COMUNA EN SUS ARCHIVOS CORRESPONDIENTES

import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arriendos.settings')
django.setup()

from app_arriendos.models import Inmuebles

def listar_inmuebles_por_comuna():
    select_comuna = """
    SELECT 
        app_arriendos_inmuebles.id_inmueble,
        app_arriendos_ubicacion.nombre_comuna,
        app_arriendos_inmuebles.nombre,
        app_arriendos_inmuebles.descripcion
    FROM 
        app_arriendos_inmuebles
    JOIN 
        app_arriendos_direccion ON app_arriendos_inmuebles.id_direccion_id = app_arriendos_direccion.id_direccion
    JOIN 
        app_arriendos_ubicacion ON app_arriendos_direccion.id_ubicacion_id = app_arriendos_ubicacion.id_ubicacion
    ORDER BY 
        app_arriendos_ubicacion.nombre_comuna;
    """
    query_comuna = Inmuebles.objects.raw(select_comuna)

    comunas_list = {}

    for inmueble in query_comuna:
        nombre_comuna = inmueble.nombre_comuna
        nombre_inmueble = inmueble.nombre
        descripcion_inmueble = inmueble.descripcion
        
        if nombre_comuna not in comunas_list:
            comunas_list[nombre_comuna] = []
        comunas_list[nombre_comuna].append({
            'nombre': nombre_inmueble,
            'descripcion': descripcion_inmueble
        })

    return comunas_list

def listar_inmuebles_por_region():
    select_region = f"""
    SELECT 
        app_arriendos_inmuebles.id_inmueble,
        app_arriendos_ubicacion.nombre_region,
        app_arriendos_inmuebles.nombre,
        app_arriendos_inmuebles.descripcion
    FROM 
        app_arriendos_inmuebles
    JOIN 
        app_arriendos_direccion ON app_arriendos_inmuebles.id_direccion_id = app_arriendos_direccion.id_direccion
    JOIN 
        app_arriendos_ubicacion ON app_arriendos_direccion.id_ubicacion_id = app_arriendos_ubicacion.id_ubicacion
    ORDER BY 
        app_arriendos_ubicacion.nombre_region;
    """
    query_region = Inmuebles.objects.raw(select_region)

    regiones_list = {}

    for inmueble in query_region:
        nombre_region = inmueble.nombre_region
        nombre_inmueble = inmueble.nombre
        descripcion_inmueble = inmueble.descripcion
        
        if nombre_region not in regiones_list:
            regiones_list[nombre_region] = []
        regiones_list[nombre_region].append({
            'nombre': nombre_inmueble,
            'descripcion': descripcion_inmueble
        })

    return regiones_list


def guardar_inmuebles_en_archivo(grupo_list, categoria, archivo):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            for grupo, inmuebles in grupo_list.items():
                f.write(f"{categoria}: {grupo}\n")
                for inmueble in inmuebles:
                    f.write(f"  Nombre: {inmueble['nombre']}\n")
                    f.write(f"  Descripción: {inmueble['descripcion']}\n")
                f.write("\n")
    except IOError as e:
        print(f"Error al escribir en el archivo: {e}")

if __name__ == "__main__":
    # Archivo salida por comuna
    archivo_salida_comuna = 'inmuebles_por_comuna.txt'
    comunas_list = listar_inmuebles_por_comuna()
    guardar_inmuebles_en_archivo(comunas_list, "Comuna", archivo_salida_comuna)
    print(f"Listado de inmuebles por comuna guardado en {archivo_salida_comuna}")

    # Archivo salida por región
    archivo_salida_region = 'inmuebles_por_region.txt'
    regiones_list = listar_inmuebles_por_region()
    guardar_inmuebles_en_archivo(regiones_list, "Región", archivo_salida_region)
    print(f"Listado de inmuebles por región guardado en {archivo_salida_region}")