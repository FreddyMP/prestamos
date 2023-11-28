from flask import Flask, request, jsonify
from config.config import exist, conec_exit
from models.empresas import list_all, create_db
from models.usuarios import create_user, read_all_users, update_user, read_find_users
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
        if 'name' in data:
            name = data['name']
            create = create_db(name)
            return create
        else:
            return jsonify({"error": "Datos JSON incompletos."}), 400
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
    
@app.route("/add_usuario", methods=['POST'])
def add_usuario():
    if request.json:
        data = request.get_json()
        if 'correo' in data and 'nombre' in data and 'contrasena' in data and 'creado_por' in data and 'rol' in data and 'cliente' in data:
            correo = data['correo']
            nombre = data['nombre']
            contrasena = data['contrasena']
            creado_por = data['creado_por']
            rol = data['rol']
            cliente = data['cliente']
            create = create_user(correo, nombre, contrasena, creado_por, rol, cliente)
            return create
        else:
            return jsonify({"error": "Datos JSON incompletos."}), 400
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
    
@app.route("/list_usuarios/<cliente>/")
def list_usuarios(cliente):
    usuarios =  read_all_users(cliente)
    return usuarios

@app.route("/find_usuarios/<cliente>/<filtro>")
def find_usuarios(cliente, filtro):
    usuarios =  read_find_users(cliente, filtro)
    return usuarios


@app.route("/update_usuario", methods=['PUT'])
def update_usuario():
    if request.json:
        data = request.get_json()
        campos = ['id_user','correo','user_log','cliente','nombre','contrasena','rol']
        lista = {}
        resultado = ''

        contador = 0
        while contador < 7:
            if campos[contador] in data:
                lista[campos[contador]] = data[campos[contador]]
            else:
                resultado = {"resultado":f"No se encontro el campo '{campos[contador]}' en el json"}
            contador = contador + 1

        if resultado =='':
            update = update_user(lista['id_user'], lista['user_log'], lista['cliente'], lista['correo'], lista['nombre'], lista['contrasena'], lista['rol'])
            return update
        else:
            return resultado
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
      

if __name__ == '__main__':
    app.run(port = 3000, debug=True)