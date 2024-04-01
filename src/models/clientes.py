from config.config import conec_exit, encriptar, db_name
from datetime import datetime

def create_customers(cliente ,nombre, apellido, cedula, identificacion_garante, direccion, ocupacion,ingresos, telefono1, telefono2, correo, lugar_trabajo, creado_por):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        sql_create_cliente = f"""INSERT INTO Clientes 
                                (nombre, apellido, identificacion, identificacion_garante, direccion, ocupacion, ingresos, telefono1, telefono2, correo, lugar_de_trabajo, creado_por)
                                VALUES
                                ('{nombre}','{apellido}','{cedula}','{identificacion_garante}','{direccion}','{ocupacion}','{ingresos}','{telefono1}',
                                '{telefono2}','{correo}','{lugar_trabajo}','{creado_por}') 
                                """
        
        cursor["cursor"].execute(sql_create_cliente)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
        return ValueError
    
def read_all_customers(cliente):
    cursor = conec_exit(cliente)
        
    name_db = db_name(cliente)

    cursor["cursor"].execute(name_db)
    
    sql_all_customers = "select * from Clientes where fecha_eliminacion is null and eliminado_por is null"
    cursor["cursor"].execute(sql_all_customers)

    clientes = cursor["cursor"].fetchall()

    return clientes

def read_find_customers(cliente, filtros):
    try:
        cursor = conec_exit(cliente)
            
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)
        
        sql_all_customers = "select * from Clientes where fecha_eliminacion is null and eliminado_por is null and " + filtros
        cursor["cursor"].execute(sql_all_customers)

        clientes = cursor["cursor"].fetchall()

        return clientes
    except:
        return ({"Error":"No fue posible esta consulta","Resultado":"No hay data"})

def update_customers(cliente, id_cliente, nombre, apellido, cedula, identificacion_garante, direccion, ocupacion, ingresos, telefono1, telefono2, correo, lugar_trabajo, user_log):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        fecha_update = datetime.now()

        sql_update_cliente = f"""UPDATE Clientes SET
                                nombre = '{nombre}' , apellido = '{apellido}', identificacion = '{cedula}', identificacion_garante = '{identificacion_garante}', direccion = '{direccion}',
                                ocupacion = '{ocupacion}', ingresos = '{ingresos}', telefono1 = '{telefono1}', telefono2 = '{telefono2}', correo = '{correo}', lugar_de_trabajo = '{lugar_trabajo}',
                                modificado_por= '{user_log}', fecha_modificacion = '{fecha_update}' WHERE id = '{id_cliente}'
                                """
        
        cursor["cursor"].execute(sql_update_cliente)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
        return ValueError

def delete_customers(cliente, id_cliente, user_log):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        fecha_update = datetime.now()

        sql_update_cliente = f"UPDATE Clientes SET eliminado_por= '{user_log}', fecha_eliminacion = '{fecha_update}' WHERE id = '{id_cliente}'"
        
        cursor["cursor"].execute(sql_update_cliente)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
            return ValueError

