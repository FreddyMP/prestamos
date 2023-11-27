from config.config import conec_exit, encriptar

def create_user(correo, nombre, contrasena, rol, creado_por, cliente):
    try:
        cursor = conec_exit(cliente)

        pre_fix = "db_"
        name_db = "USE "+pre_fix + cliente
        cursor['cursor'].execute(name_db)
        password = encriptar(contrasena)
        sql_crear_usuario = f"INSERT INTO usuarios (correo, nombre, contrasena, id_rol, creado_por) VALUES ('{correo}', '{nombre}','{password}',{rol},{creado_por})"
        cursor['cursor'].execute(sql_crear_usuario)

        cursor['connection'].commit()

        return  {"Resultado":password}
        
    except:
        search_error_sql = """SELECT * FROM usuarios"""
        cursor['cursor'].execute(search_error_sql)

        result = cursor['cursor'].fetchall()
        mensaje = ''

        for row in result:
            if row["correo"] == correo:
                mensaje = "Error, ya existe este correo"


        cursor['connection'].rollback()
        return {"resultado":"Error","Mensaje":mensaje}
    
def read_all_users(cliente):
        cursor = conec_exit(cliente)
        pre_fix = "db_"
        name_db = "USE "+pre_fix + cliente
        cursor['cursor'].execute(name_db)

        search_sql = """SELECT * FROM usuarios"""
        cursor['cursor'].execute(search_sql)

        result = cursor['cursor'].fetchall()
        
        return result

def update_user(id_user, correo, nombre, contrasena, rol, cliente):
     
    cursor = conec_exit(cliente)
    pre_fix = "db_"
    name_db = "USE "+pre_fix + cliente
    cursor['cursor'].execute(name_db)

    update_user_sql = f"UPDATE usuarios SET correo ='{correo}', nombre = '{nombre}', contrasena = '{contrasena}', id_rol = {rol} "


    