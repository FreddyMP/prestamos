import pymysql
import hashlib

def exist(nombre):
    db = pymysql.connect(host= 'localhost', port= 3306, user= 'fpereyra', password='15951236487')
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
    
def encriptar(texto_plano):
    # Crear un objeto hash SHA-256
    sha256 = hashlib.sha256()

    # Convertir el texto a bytes (ya que el hash se calcula en bytes)
    texto_bytes = texto_plano.encode('utf-8')

    # Actualizar el objeto hash con los bytes del texto
    sha256.update(texto_bytes)

    # Obtener el hash en formato hexadecimal
    hash_resultado = sha256.hexdigest()

    return hash_resultado   

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

def db_name(cliente):
    pre_fix = "db_"
    name = "USE "+pre_fix + cliente
    return name

   

   
