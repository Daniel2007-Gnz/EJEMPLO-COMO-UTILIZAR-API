from flask import Flask, jsonify, render_template, abort
import copy

app = Flask(__name__)

CARROS_INICIALES = [
    {"id": 1, "marca": "Toyota", "modelo": "Corolla", "anio": 2020, "kilometraje": 45000, "transmision": "Automática", "color": "Gris", "precio": 14500},
    {"id": 2, "marca": "Mazda", "modelo": "3", "anio": 2019, "kilometraje": 62000, "transmision": "Manual", "color": "Rojo", "precio": 11800},
    {"id": 3, "marca": "Honda", "modelo": "Civic", "anio": 2021, "kilometraje": 30000, "transmision": "Automática", "color": "Negro", "precio": 17200}
]

carros = copy.deepcopy(CARROS_INICIALES)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/api/carros', methods=['GET'])
def obtener_carros():
    return jsonify(carros), 200

@app.route('/api/carros/<int:carro_id>/comprar', methods=['POST'])
def comprar_carro(carro_id):
    global carros
    carro = next((c for c in carros if c["id"] == carro_id), None)

    if carro is None:
        abort(404, description="Carro no encontrado")

    carros = [c for c in carros if c["id"] != carro_id]
    return jsonify({"mensaje": "Compra exitosa", "carro": carro}), 200

@app.route('/api/carros/reiniciar', methods=['POST'])
def reiniciar_inventario():
    global carros
    carros = copy.deepcopy(CARROS_INICIALES)
    return jsonify(carros), 200

if __name__ == '__main__':
    app.run(debug=True)