'''
from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario para almacenar las mascotas
lista_mascotas = {
    'Pluto': {
        "nombre": "Pluto",
        "edad": "18 meses",
        "raza": "Pitbull",
        "alergias": "Ninguna",
        "genero": "Macho",
        "observaciones": "Ninguna"
    }
}

# Función auxiliar para validar si una mascota existe
def mascota_existe(nombre):
    return nombre in lista_mascotas

# Método GET para listar todas las mascotas
@app.route('/mascotas', methods=['GET'])
def obtener_mascotas():
    return jsonify(lista_mascotas), 200

# Método GET para buscar una mascota por nombre o raza
@app.route('/mascotas/buscar', methods=['GET'])
def buscar_mascota():
    nombre = request.args.get('nombre')
    raza = request.args.get('raza')

    # Filtrar las mascotas que coinciden con el nombre o raza
    resultado = [
        mascota for mascota in lista_mascotas.values()
        if (nombre and mascota['nombre'] == nombre) or (raza and mascota['raza'] == raza)
    ]

    # Retornar la primera coincidencia encontrada
    if resultado:
        return jsonify(resultado[0]), 200

    return jsonify({"mensaje": "Mascota no encontrada"}), 404

# Método POST para agregar una nueva mascota
@app.route('/mascotas', methods=['POST'])
def agregar_mascota():
    datos = request.get_json()

    if not datos or 'nombre' not in datos or 'edad' not in datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    if mascota_existe(datos['nombre']):
        return jsonify({"mensaje": "La mascota ya existe"}), 400

    lista_mascotas[datos['nombre']] = datos
    return jsonify(datos), 201

# Método PUT para modificar una mascota existente (permite modificaciones parciales)
@app.route('/mascotas/<string:nombre>', methods=['PUT'])
def modificar_mascota(nombre):
    if not mascota_existe(nombre):
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({"mensaje": "Datos inválidos"}), 400

    # Verificar duplicado si el nombre cambia
    nuevo_nombre = datos.get('nombre', nombre)
    if nuevo_nombre != nombre and mascota_existe(nuevo_nombre):
        return jsonify({"mensaje": "Ya existe una mascota con ese nombre"}), 400

    # Actualizar datos de la mascota
    lista_mascotas[nombre].update(datos)

    # Cambiar el nombre en el diccionario si es necesario
    if nuevo_nombre != nombre:
        lista_mascotas[nuevo_nombre] = lista_mascotas.pop(nombre)

    return jsonify(lista_mascotas[nuevo_nombre]), 201

# Método DELETE para eliminar una mascota
@app.route('/mascotas/<string:nombre>', methods=['DELETE'])
def eliminar_mascota(nombre):
    if not mascota_existe(nombre):
        return jsonify({"mensaje": "Mascota no encontrada"}), 404

    del lista_mascotas[nombre]
    return jsonify({"mensaje": f"Mascota {nombre} eliminada correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)
    '''