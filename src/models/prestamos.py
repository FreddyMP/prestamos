from config.config import conec_exit, encriptar, db_name
from datetime import datetime

def create_prestamo(cliente, id_cliente, valor_de_prestamo, balance_actual, fecha_desembolso, dia_de_pago, frecuencia_de_interes, tasa_de_interes, fecha_cambio_tasa_de_interes, tipo_de_amortizacion, tiempo_de_prestamo, aplica_garantia, user_log ):
    try:
        cursor = conec_exit(cliente)
        
        name_db = db_name(cliente)

        cursor["cursor"].execute(name_db)

        #fecha_update = datetime.now()

        sql_add_prestamo = f""" INSERT INTO prestamos (id_cliente, valor_de_prestamo, balance_actual, fecha_desembolso, dia_de_pago, frecuencia_de_interes, tasa_de_interes,
        fecha_cambio_tasa_de_interes, tipo_de_amortizacion, tiempo_de_prestamo, aplica_garantia, creado_por ) 
        values({id_cliente},{ valor_de_prestamo}, {balance_actual}, '{fecha_desembolso}', {dia_de_pago}, {frecuencia_de_interes}, {tasa_de_interes}, '{fecha_cambio_tasa_de_interes}',
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

def read_find_prestamos(cliente, filtros):
    cursor = conec_exit(cliente)
        
    name_db = db_name(cliente)

    cursor["cursor"].execute(name_db)
    
    sql_find_prestamos = f"select id_cliente from prestamos where id_cliente in (select id from clientes where {filtros} ) and fecha_eliminacion is null and eliminado_por is null "
    cursor["cursor"].execute(sql_find_prestamos)

    prestamos_find = cursor["cursor"].fetchall()
    
    return prestamos_find["id_cliente"]