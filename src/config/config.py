import pymysql

def exist(nombre):
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='')

    cursor =  db.cursor(pymysql.cursors.DictCursor)

    existencia_db = f"SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{nombre}'"

    
    try:
        cursor.execute(existencia_db)

        resultado_existencia = cursor.fetchone()
    
        # El indice 1 es el flag si existe la db
        if resultado_existencia:
            si_existe = {'db_name' : resultado_existencia["SCHEMA_NAME"],
                         'exist': 1}
            return si_existe
        else:
            no_existe = {'exist': 0}
            return no_existe
        
    except:
        return {'fail': "error en la consulta"}

def conec_exit(nombre):
    dba = exist(nombre)
    existe = {'exist': dba['exist']}
    if existe == 1:
        db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '', db = nombre)
        cursor =  db.cursor(pymysql.cursors.DictCursor)
        return {'cursor':cursor, 'connection': db}  
    else:
        db = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', password = '')
        cursor =  db.cursor(pymysql.cursors.DictCursor)
        return {'cursor':cursor, 'connection': db} 



   

   
