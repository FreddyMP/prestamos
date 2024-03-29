from config.config import conec_exit, encriptar, db_name
from datetime import datetime

def create_user(correo, nombre, contrasena, rol, creado_por, cliente):
    try:
        cursor = conec_exit(cliente)

        name_db = db_name(cliente)

        cursor['cursor'].execute(name_db)
        password = encriptar(contrasena)
        sql_crear_usuario = f"INSERT INTO Usuarios (correo, nombre, contrasena, id_rol, creado_por) VALUES ('{correo}', '{nombre}','{password}',{rol},{creado_por})"
        cursor['cursor'].execute(sql_crear_usuario)

        cursor['connection'].commit()

        return  {"Resultado":password}
        
    except:
        search_error_sql = """SELECT * FROM Usuarios"""
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

        name_db = db_name(cliente)
        cursor['cursor'].execute(name_db)

        search_sql = "SELECT * FROM Usuarios where eliminado_por is null and fecha_eliminacion is null "
        cursor['cursor'].execute(search_sql)

        result = cursor['cursor'].fetchall()
        
        return result

def read_find_users(cliente, filtro):
        try:
            cursor = conec_exit(cliente)
            
            name_db = db_name(cliente)
            cursor['cursor'].execute(name_db)

            search_sql = f"SELECT  *, count(*) AS conteo FROM Usuarios where nombre like '%{filtro}%' and eliminado_por is null and fecha_eliminacion is null"
            cursor['cursor'].execute(search_sql)
            result = cursor['cursor'].fetchall()

            return  result
            
        except ValueError:
            return ValueError
        
def find_user(cliente, id_user):
        try:
            cursor = conec_exit(cliente)
            
            name_db = db_name(cliente)
            cursor['cursor'].execute(name_db)

            search_sql = f"SELECT  * FROM Usuarios where id = {id_user} and eliminado_por is null and fecha_eliminacion is null"
            cursor['cursor'].execute(search_sql)
            result = cursor['cursor'].fetchall()

            return  result
            
        except ValueError:
            return ValueError  
              
def update_user(id_user, user_log, cliente, correo, nombre, contrasena, rol):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)
        cursor['cursor'].execute(name_db)

        fecha_update = datetime.now()
        password = encriptar(contrasena)

        update_user_sql = f"UPDATE Usuarios SET correo ='{correo}', nombre = '{nombre}', contrasena = '{password}', id_rol = {rol}, modificado_por = {user_log}, fecha_modificacion = '{fecha_update}' where id = {id_user} "

        cursor['cursor'].execute(update_user_sql)
        cursor['connection'].commit()

        return {"resultado":"ok"}
    except:
        cursor['connection'].rollback()
        return {"resultado":"Error al actualizar los datos, Posibles razones, el correo ya existe, existen campos con una longitud erronea"}

def delete_user(cliente, id_user, user_log):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor['cursor'].execute(name_db)

        fecha_update = datetime.now()

        delete_user_sql = f"UPDATE Usuarios SET eliminado_por = {user_log}, fecha_eliminacion =  '{fecha_update}' where id = {id_user} "

        cursor['cursor'].execute(delete_user_sql)
        cursor['connection'].commit()

        return {"resultado":"ok"}
    except:
        cursor['connection'].rollback()
        return {"resultado":"Error al actualizar los datos"}
    
def log_in(cliente, usuario, contrasena):
   
    try:
        cursor = conec_exit(cliente)

        name_db = db_name(cliente)
        user = usuario
    
        cursor['cursor'].execute(name_db)

        password =  encriptar(contrasena)

        sql_search_user = f"SELECT count(*) as verificado FROM Usuarios WHERE correo ='{user}' AND contrasena = '{password}' and fecha_eliminacion is null and eliminado_por is null"
        cursor['cursor'].execute(sql_search_user)
        login = cursor['cursor'].fetchone()

        data_log = {}
        
        if login['verificado'] == 1:
            sql_data_log = f"SELECT id_rol, id, nombre FROM Usuarios WHERE correo ='{user}' AND contrasena = '{password}' and fecha_eliminacion is null and eliminado_por is null"
            cursor['cursor'].execute(sql_data_log)
            data_log = cursor['cursor'].fetchone()
            
        return data_log
    except:
        return {"verificado":0}

    
          
     
    