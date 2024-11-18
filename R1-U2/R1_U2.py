from flask import Flask, jsonify, request

app = Flask(__name__)

# Manejar los datos mediante un diccionario 
#listaMascotas = {}
lista_mascotas = {
    'Negro': {
        "nombre": "Negro",
        "edad": "19 meses",
        "raza": "Pitbull",
        "alergias": "Polen",
        "genero": "Macho",
        "observaciones": "Muy rabioso"
    },
    'Luna': {
        "nombre": "Luna",
        "edad": "1 mes",
        "raza": "Chihuahua",
        "alergias": "Polvo",
        "genero": "Hembra",
        "observaciones": "Un poco tragona"
    }
}

# Crear un servicio en donde se permita el listado de todas las mascotas a través del
#método GET, regresar el código 200
def mascota_existe(nombre):
    return nombre in lista_mascotas

@app.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    return jsonify(lista_mascotas), 200

#Crear un servicio en donde se permita la búsqueda de una mascota mediante el nombre
#o la raza mediante el método GET, regresar el código 200
@app.route('/mascotas/buscar', methods=['GET'])
def buscar_mascota():
    nombre = request.args.get('nombre')
    raza = request.args.get('raza')

    
    resultado = [
        mascota for mascota in lista_mascotas.values()
        if (nombre and mascota['nombre'] == nombre) or (raza and mascota['raza'] == raza)
    ]

    # Retornar la primera coincidencia encontrada
    if resultado:
        return jsonify(resultado[0]), 200

    return jsonify({"mensaje": "Mascota no encontrada"}), 404
#Agregar una mascota al diccionario y validar que los datos sean válidos o no sean vacíos,
#método POST, regresar el código 201.
@app.route('/mascotas', methods=['POST'])
def agregar_mascota():
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    if mascota_existe(datos['nombre']):
        return jsonify({"mensaje": "La mascota ya existe"}), 400

    lista_mascotas[datos['nombre']] = datos
    return jsonify(datos), 201

# Modificar mascota del diccionario y validar que los datos sean correctos o no sean vacíos,método PUT 
@app.route('/mascotas/<string:nombre>', methods=['PUT'])
def modificar_mascota(nombre):
    if not mascota_existe(nombre):
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    nuevo_nombre = datos.get('nombre', nombre)
    if nuevo_nombre != nombre and mascota_existe(nuevo_nombre):
        return jsonify({"mensaje": "Ya existe una mascota con ese nombre"}), 400

    if nuevo_nombre != nombre:
        lista_mascotas[nuevo_nombre] = lista_mascotas.pop(nombre)

    return jsonify(lista_mascotas[nuevo_nombre]), 201

# Eliminar una mascota mediante método DELETE 
@app.route('/mascotas/<string:nombre>', methods=['DELETE'])
def eliminar_mascota(nombre):
    if not mascota_existe(nombre):
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    del lista_mascotas[nombre]
    return jsonify({"mensaje": f"Mascota {nombre} eliminada correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
