import json

# Lee el archivo original
with open('comunas_regiones.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Lista para almacenar los datos transformados
formato_data = []

# ID inicial para la tabla Ubicacion
id_ubicacion = 1

# Transformar los datos
for region in data['regiones']:
    nombre_region = region['region']
    for comuna in region['comunas']:
        # Crear un diccionario para cada ubicación
        entry = {
            "model": "app_arriendos.ubicacion",
            "pk": id_ubicacion,
            "fields": {
                "nombre_region": nombre_region,
                "nombre_comuna": comuna
            }
        }
        formato_data.append(entry)
        id_ubicacion += 1

# Guardar los datos transformados en un nuevo archivo JSON
with open('ubicaciones.json', 'w', encoding='utf-8') as file:
    json.dump(formato_data, file, ensure_ascii=False, indent=4)

print("Transformación completa. Los datos han sido guardados en 'ubicaciones_transformadas.json'.")
