from config.config import conec_exit, encriptar
from datetime import datetime
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

        search_sql = "SELECT * FROM usuarios where eliminado_por is null and fecha_eliminacion is null "
        cursor['cursor'].execute(search_sql)

        result = cursor['cursor'].fetchall()
        
        return result

def read_find_users(cliente, filtro):
        try:
            cursor = conec_exit(cliente)
            pre_fix = "db_"
            name_db = "USE "+pre_fix + cliente
            cursor['cursor'].execute(name_db)

            search_sql = f"SELECT * FROM usuarios where nombre like '%{filtro}%' and eliminado_por is null and fecha_eliminacion is null"
            cursor['cursor'].execute(search_sql)

            result = cursor['cursor'].fetchall()
            
            return result
        except:
            return {"Resultado":f"Error buscando '{filtro}'"}
        
def update_user(id_user, user_log, cliente, correo, nombre, contrasena, rol):
    try:
        cursor = conec_exit(cliente)
        pre_fix = "db_"
        name_db = "USE "+pre_fix + cliente
        cursor['cursor'].execute(name_db)

        fecha_update = datetime.now()
        password = encriptar(contrasena)

        update_user_sql = f"UPDATE usuarios SET correo ='{correo}', nombre = '{nombre}', contrasena = '{password}', id_rol = {rol}, modificado_por = {user_log}, fecha_modificacion = '{fecha_update}' where id = {id_user} "

        cursor['cursor'].execute(update_user_sql)
        cursor['connection'].commit()

        return {"resultado":"ok"}
    except:
        cursor['connection'].rollback()
        return {"resultado":"Error al actualizar los datos, Posibles razones, el correo ya existe, existen campos con una longitud erronea"}

def delete_user(cliente, id_user, user_log):
    try:
        cursor = conec_exit(cliente)
        pre_fix = "db_"
        name_db = "USE "+pre_fix + cliente
        cursor['cursor'].execute(name_db)

        fecha_update = datetime.now()

        delete_user_sql = f"UPDATE usuarios SET eliminado_por = {user_log}, fecha_eliminacion =  '{fecha_update}' where id = {id_user} "

        cursor['cursor'].execute(delete_user_sql)
        cursor['connection'].commit()

        return {"resultado":"ok"}
    except:
        cursor['connection'].rollback()
        return {"resultado":"Error al actualizar los datos"}
          
     
    