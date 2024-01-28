from config.config import conec_exit, encriptar, db_name
from datetime import datetime

def create_prestamo(cliente, id_cliente, valor_de_prestamo, balance_actual, frecuencia_de_interes, tasa_de_interes, fecha_cambio_tasa_de_interes, tipo_de_amortizacion, tiempo_de_prestamo, aplica_garantia, user_log ):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        #fecha_update = datetime.now()

        sql_add_prestamo = f""" INSERT INTO prestamos (id_cliente, valor_de_prestamo, balance_actual, frecuencia_de_interes, tasa_de_interes,
        fecha_cambio_tasa_de_interes, tipo_de_amortizacion, tiempo_de_prestamo, aplica_garantia, creado_por ) 
        values({id_cliente},{ valor_de_prestamo}, {balance_actual}, {frecuencia_de_interes}, {tasa_de_interes}, '{fecha_cambio_tasa_de_interes}',
        '{tipo_de_amortizacion}', {tiempo_de_prestamo}, {aplica_garantia}, '{user_log}' )"""
        
        cursor["cursor"].execute(sql_add_prestamo)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
            return ValueError
    
def read_all_prestamos(cliente):
    cursor = conec_exit(cliente)
        
    name_db = db_name(cliente)

    cursor["cursor"].execute(name_db)
    
    sql_all_prestamos = "select * from prestamos where fecha_eliminacion is null and eliminado_por is null"
    cursor["cursor"].execute(sql_all_prestamos)

    prestamos = cursor["cursor"].fetchall()

    return prestamos

def read_find_prestamos(cliente, filtros, id = 0):
    cursor = conec_exit(cliente)
        
    name_db = db_name(cliente)

    cursor["cursor"].execute(name_db)

    search_id = ' and 1=1'

    if id != 0 and id != "" and id != '':
         search_id = " and id = " + id
    
    sql_count_prestamos = f"select Distinct count(*) as total from prestamos where id_cliente in (select id from clientes where {filtros} ){search_id}  and fecha_eliminacion is null and eliminado_por is null "
    cursor["cursor"].execute(sql_count_prestamos)
    find_count = cursor["cursor"].fetchall()

    total = find_count[0]
    
    if total["total"] > 0:
        sql_find_prestamos = f"select Distinct * from prestamos where id_cliente in (select id from clientes where {filtros} ){search_id} and fecha_eliminacion is null and eliminado_por is null "
        cursor["cursor"].execute(sql_find_prestamos)
        prestamos_find = cursor["cursor"].fetchall()
        return prestamos_find
    else:
        return {"resultado":"No se encontraron registros"}
    
def update_find_prestamo(cliente, id_prestamo, valor_de_prestamo, balance_actual, frecuencia_de_interes, tasa_de_interes, fecha_cambio_tasa_de_interes, tipo_de_amortizacion, tiempo_de_prestamo, aplica_garantia, user_log ):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        fecha_update = datetime.now()

        sql_update_prestamo = f""" UPDATE prestamos  SET valor_de_prestamo = {valor_de_prestamo}, balance_actual = {balance_actual},  frecuencia_de_interes =  {frecuencia_de_interes},
        tasa_de_interes = {tasa_de_interes}, fecha_cambio_tasa_de_interes = '{fecha_cambio_tasa_de_interes}', tipo_de_amortizacion = '{tipo_de_amortizacion}',
        tiempo_de_prestamo = {tiempo_de_prestamo}, aplica_garantia = {aplica_garantia}, modificado_por= {user_log}, fecha_modificacion = '{fecha_update}' 
        where id = {id_prestamo}"""
        
        cursor["cursor"].execute(sql_update_prestamo)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
        cursor['connection'].rollback()
        return ValueError
    
def prestamo_delete(cliente, id_prestamo, user_log):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        fecha_delete = datetime.now()

        sql_delete_prestamo = f" UPDATE prestamos  SET  eliminado_por= {user_log}, fecha_eliminacion = '{fecha_delete}' where id = {id_prestamo}"
        
        cursor["cursor"].execute(sql_delete_prestamo)
        cursor['connection'].commit()

        return {"resultado":"Ok"}

    except ValueError:
        cursor['connection'].rollback()
        return ValueError     