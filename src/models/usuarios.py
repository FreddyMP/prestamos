from config.config import conec_exit

def create_usuarios(correo, nombre, contrasena, rol, creado_por, cliente):
    try:
        cursor = conec_exit(cliente)
        pre_fix = "DB_"
        name_db = pre_fix + cliente
        cursor['cursor'].execute("USE "+name_db)
        sql_crear_usuario = f"INSERT INTO usuarios (correo, nombre, contrasena, id_rol, creado_por) VALUES ('{correo}', '{nombre}','{contrasena}',{rol},{creado_por})"
        cursor['cursor'].execute(sql_crear_usuario)
        return  {"Resultado":"ok","Correo":correo,"Usuario":correo,"Nombre":nombre}
    except:
        search_error_sql = "SELECT * FROM usuarios"
        return {'resultado':0}
    