from flask import Flask, request, jsonify
from config.config import exist, conec_exit
from models.empresas import list_all, create_db

app = Flask(__name__)

@app.route("/exist/<empresa>/")
def index(empresa):
    Test_conexion = exist(empresa)
    return Test_conexion

@app.route("/list_rol/<nombre>/")
def index2(nombre):
    lista = list_all(nombre)
    return lista

@app.route("/add_empresa", methods=['POST'])
def add_empresa():
    if request.json:
        data = request.get_json()
        if 'nombre' in data:
            nombre = data['nombre']
            create = create_db(nombre)
            return create
        else:
            return jsonify({"error": "Datos JSON incompletos."}), 400
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400

if __name__ == '__main__':
    app.run(port = 3000, debug=True)