from config.config import conec_exit

def create_rol(nombre_db, descripcion, creado_por):
    cursor = conec_exit(nombre_db)
    sql = f"INSERT into {nombre_db}.roles(description, creado_por) values ('{descripcion}', '{creado_por}')"

    cursor.excute(sql)

    return 'hecho'