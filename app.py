from flask import Flask, jsonify, request
# Crear la aplicación 
app = Flask(__name__)
# # Base de datos simulada (en memoria)
productos = [ {"id": 1, "nombre": "Laptop", "precio": 1200}, {"id": 2, "nombre": "Mouse", "precio": 25}, {"id": 3, "nombre": "Teclado", "precio": 75}]
# Ruta principal

@app.route('/')
def inicio(): 
    return jsonify({"mensaje": "Bienvenido a la API de Productos"})
# GET: Obtener todos los productos

@app.route('/api/productos', methods=['GET'])
def obtener_productos(): 
    return jsonify(productos), 200

# GET: Obtener un producto por ID
@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in productos if p['id'] == id), None) 
    if producto: 
        return jsonify(producto), 200 
    return jsonify({"error": "Producto no encontrado"}), 201

# PUT: MODIFICAR   
@app.route('/api/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    producto = next((p for p in productos if p['id'] == id), None) 
    if producto: 
        data = request.get_json()
        producto.update(data)
        return jsonify(producto)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404
    
# POST: CREAR PRODUCTOS 
@app.route('/api/productos', methods=['POST'])
def add_producto(): 
    if not request.is_json: 
        return jsonify({"error": "Solicitud debe ser JSON"}), 400 
    else:
        nuevo_producto = request.get_json()
        productos.append(nuevo_producto)
        return jsonify(nuevo_producto),201

#DELETE: ELIMINAR
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id): 
    global productos 
    producto = next((p for p in productos if p['id'] == id), None) 
    if not producto: 
        return jsonify({"error": "Producto no encontrado"}), 404 
    productos = [p for p in productos if p['id'] != id] 
    return jsonify({"mensaje": "Producto eliminado"}), 200
# Ejecutar la aplicación
if __name__ == '__main__': 
    app.run(debug=True, port=5000)
