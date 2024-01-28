from python-flask import Flask, request, jsonify
from config.config import exist, conec_exit
from controllers.metodos import search_keys, find,not_empty
from models.empresas import list_all, create_db
from models.clientes import create_customers, read_all_customers, read_find_customers, update_customers, delete_customers
from models.prestamos import create_prestamo, read_all_prestamos, read_find_prestamos, update_find_prestamo
from models.usuarios import create_user, read_all_users, update_user, read_find_users, delete_user, log_in, find_user
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

@app.route("/list_find_usuarios/<cliente>/<filtro>")
def list_find_usuarios(cliente, filtro):
    usuarios =  read_find_users(cliente, filtro)
    return usuarios

@app.route("/find_usuario/<cliente>/<id_user>")
def find_usuarios(cliente, id_user):
    usuarios = find_user(cliente, id_user)
    return usuarios

@app.route("/login/", methods=['POST'])
def login():
    if request.json:
        data = request.get_json()
        campos = ['usuario','cliente','contrasena']
        lista = {}

        search = search_keys(campos, data)

        lista = search[1]

        if search[0] == '0':
            return search[1] 
        else:
            loguear = log_in(lista['cliente'], lista['usuario'], lista['contrasena'])
            return loguear
  
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400

@app.route("/update_usuario", methods=['PUT'])
def update_usuario():
    if request.json:
        data = request.get_json()
        campos = ['id_user','correo','user_log','cliente','nombre','contrasena','rol']
        lista = {}
        
        search = search_keys(campos, data)

        lista = search[1]


        if search[0] == '0':
            return search[1] 
        else:
            update = update_user(lista['id_user'], lista['user_log'], lista['cliente'], lista['correo'], lista['nombre'], lista['contrasena'], lista['rol'])
            return update
       
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
    
@app.route("/delete_usuario", methods=['DELETE'])
def delete_usuario():
    if request.json:
        data = request.get_json()
        campos = ['id_user','user_log','cliente']
        lista = {}

        search = search_keys(campos, data)

        lista = search[1]
        
        if search[0] == '0':
            return search[1] 
        else:
            delete = delete_user(lista['cliente'], lista['id_user'], lista['user_log']) 
            return delete
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
      
@app.route("/add_cliente", methods=['POST'])
def add_cliente():
    if request.json:
        data = request.get_json()
        campos = ['cliente' ,'nombre', 'apellido', 'cedula', 'identificacion_garante', 'direccion', 'ocupacion','ingresos', 'telefono1', 'telefono2', 'correo', 'lugar_trabajo', 'creado_por']
        lista = {}

        search = search_keys(campos, data)

        lista = search[1]
        
        if search[0] == '0':
            return search[1] 
        else:
            create = create_customers(lista['cliente'] ,lista['nombre'], lista['apellido'], lista['cedula'], lista['identificacion_garante'], lista['direccion'], lista['ocupacion'],lista['ingresos'], lista['telefono1'], lista['telefono2'], lista['correo'], lista['lugar_trabajo'], lista['creado_por'])
            return create

    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
         
@app.route("/list_clientes/<cliente>/")
def list_clientes(cliente):
    usuarios =  read_all_customers(cliente)
    return usuarios

@app.route("/find_clientes", methods=["POST"] )
def find_clientes():
    data = request.get_json()
    campos = ['cliente','id','correo', 'nombre','apellido', 'identificacion', 'identificacion_garante']

    cliente = data["cliente"]
    filtros = find(campos, data)
    clientes =  read_find_customers(cliente, filtros)
    return clientes

@app.route("/update_cliente", methods=['PUT'])
def update_cliente():
    if request.json:
        data = request.get_json()
        campos = ['cliente', 'id_cliente', 'nombre', 'apellido', 'cedula', 'identificacion_garante', 'direccion', 'ocupacion', 'ingresos', 'telefono1', 'telefono2', 'correo', 'lugar_trabajo', 'user_log']
        lista = {}
        
        search = search_keys(campos, data)

        lista = search[1]

        if search[0] == '0':
            return search[1] 
        else:
            update = update_customers(lista['cliente'] ,lista['id_cliente'], lista['nombre'], lista['apellido'], lista['cedula'], lista['identificacion_garante'], lista['direccion'], lista['ocupacion'], lista['ingresos'], lista['telefono1'], lista['telefono2'], lista['correo'], lista['lugar_trabajo'], lista['user_log'])
            return update
       
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400          

@app.route("/delete_cliente", methods=['DELETE'])
def delete_cliente():
    if request.json:
        data = request.get_json()
        campos = ['id_cliente','user_log','cliente']
        lista = {}

        search = search_keys(campos, data)

        lista = search[1]
        
        if search[0] == '0':
            return search[1] 
        else:
            delete = delete_customers(lista['cliente'], lista['id_cliente'], lista['user_log']) 
            return delete
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
             
@app.route("/add_prestamo", methods=['POST'])
def add_prestamo():
    if request.json:
        data = request.get_json()
        campos = ['cliente', 'id_cliente','user_log', 'valor_de_prestamo', 'balance_actual', 'fecha_desembolso', 'dia_de_pago', 'frecuencia_de_interes', 'tasa_de_interes', 'fecha_cambio_tasa_de_interes', 'tipo_de_amortizacion', 'tiempo_de_prestamo', 'aplica_garantia']
        lista = {}

        search = search_keys(campos, data)

        lista = search[1]
        if search[0] == '0':
            return search[1] 
        else:
            add = create_prestamo(lista['cliente'], lista['id_cliente'],  lista['valor_de_prestamo'], lista['balance_actual'], lista['fecha_desembolso'], lista['dia_de_pago'] , lista['frecuencia_de_interes'], lista['tasa_de_interes'], lista['fecha_cambio_tasa_de_interes'], lista['tipo_de_amortizacion'] , lista['tiempo_de_prestamo'], lista['aplica_garantia'], lista['user_log']) 
            return add
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
             
@app.route("/list_prestamos/<cliente>/")
def list_prestamos(cliente):
    prestamos =  read_all_prestamos(cliente)
    return prestamos

@app.route("/find_prestamos", methods=["POST"] )
def find_prestamos():
    data = request.get_json()
    campos = ['cliente','identificacion', 'nombre','apellido']

    cliente = data["cliente"]
    id = data["id"]
    filtros = find(campos, data)
    prestamos_find =  read_find_prestamos(cliente, filtros, id)
    return prestamos_find

@app.route("/update_prestamo", methods=['PUT'])
def update_prestamo():
    if request.json:
        data = request.get_json()
        campos = ['cliente', 'user_log', 'valor_de_prestamo', 'balance_actual', 'frecuencia_de_interes', 'tasa_de_interes', 'fecha_cambio_tasa_de_interes', 'tipo_de_amortizacion', 'tiempo_de_prestamo', 'aplica_garantia']
        campos_not_null =  ['cliente', 'user_log', 'valor_de_prestamo', 'balance_actual', 'frecuencia_de_interes', 'tasa_de_interes', 'tipo_de_amortizacion', 'tiempo_de_prestamo', 'aplica_garantia']
        lista = {}

        no_nulos = not_empty(campos_not_null, data )

        search = search_keys(campos, data)

        lista = search[1]
        id_prestamo = data['id_prestamo']
        if search[0] == '0':
            return search[1] 
        else:
            if no_nulos[0] == "1":
                prestamo_update = update_find_prestamo(lista['cliente'], id_prestamo, lista['valor_de_prestamo'], lista['balance_actual'],  lista['frecuencia_de_interes'], lista['tasa_de_interes'], lista['fecha_cambio_tasa_de_interes'], lista['tipo_de_amortizacion'] , lista['tiempo_de_prestamo'], lista['aplica_garantia'], lista['user_log']) 
                return prestamo_update
            else:
                return no_nulos[1]
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400
    
@app.route("/delete_prestamo", methods=['DELETE'])
def delete_prestamo():
    if request.json:
        data = request.get_json()
        campos = ['id_prestamo','user_log','cliente']
        campos_not_null = ['id_prestamo','user_log','cliente']
        lista = {}

        no_nulos = not_empty(campos_not_null, data )
        search = search_keys(campos, data)

        lista = search[1]
        
        if search[0] == '0':
            return search[1] 
        else:
            if no_nulos[0] == "1":
                delete = delete_customers(lista['cliente'], lista['id_cliente'], lista['user_log']) 
                return delete
            else:
                return no_nulos[1]
        
    else:
        return jsonify({"error": "Solicitud no contiene datos JSON."}), 400



if __name__ == '__main__':
    app.run(port = 3000, debug=True)