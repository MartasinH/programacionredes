import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

mascotas = {
    "1":"firulais el guero",
}
mascotas ['2']= "El feo"
mascotas ['3']= "El Firus"
@app.route('/', methods=['GET'])
def hola():
    return jsonify({'mensaje': 'Hola'})

@app.route('/mascotas', methods=['GET'])
def list_mascotas():
    return jsonify(mascotas), 200
@app.route('/mascotas', methods=['POST'])
def add_mascotas():
    datos = requests.get_json()
    mascotas[datos['clave']]=datos['nombre']
    return jsonify({'mensaje': 'Agregado'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)