from config.config import conec_exit, encriptar
import random

def list_all(nombre):
    sql='SELECT * FROM ROL'
    cursor = conec_exit(nombre)
    cursor.execute(sql)

    result = cursor.fetchall()

    return result

def create_db(nombre):
    try:
        pre_fix = "DB_"
        name_db = pre_fix + nombre

        sql= "CREATE DATABASE "+name_db
        cursor = conec_exit(name_db)
        cursor['cursor'].execute(sql)
        cursor['cursor'].execute("USE "+name_db)

        #crear tabla para nuestros clientes
        #cursor.execute("CREATE TABLE empresas (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(50) NOT NULL, registrado_Por VARCHAR(50) NOT NULL, fecha_registro DATE NOT NULL, correo VARCHAR(50), telefono1 VARCHAR(50) NOT NULL, telefono2 VARCHAR(50), direccion TEXT NOT NULL, status CHAR(1) DEFAULT '0', fecha_ultimo_pago DATE,  fecha_siguiente_pago DATE, RNC_cedula VARCHAR(50) NOT NULL)")
        cursor['cursor'].execute("CREATE TABLE Roles (id INT AUTO_INCREMENT PRIMARY KEY, descripcion VARCHAR(50) NOT NULL, fecha_creacion DATE DEFAULT CURRENT_TIMESTAMP NOT NULL, creado_por INT(11) NOT NULL, fecha_modificacion DATE, modificado_por INT(11), fecha_eliminacion DATE, eliminado_por INT(11))")
        cursor['cursor'].execute("CREATE TABLE Usuarios (id INT AUTO_INCREMENT PRIMARY KEY, correo VARCHAR(50) NOT NULL UNIQUE, nombre VARCHAR(50) NOT NULL, contrasena VARCHAR(200) NOT NULL, id_rol INT(11) NOT NULL, fecha_creacion DATE DEFAULT CURRENT_TIMESTAMP NOT NULL, creado_por INT(11) NOT NULL, fecha_modificacion DATE, modificado_por INT(11), fecha_eliminacion DATE, eliminado_por INT(11))")
        cursor['cursor'].execute("CREATE TABLE Clientes (id INT AUTO_INCREMENT PRIMARY KEY,nombre VARCHAR(50) NOT NULL, apellido VARCHAR(50) NOT NULL, identificacion VARCHAR(50) NOT NULL, identificacion_garante VARCHAR(50), direccion TEXT NOT NULL, ocupacion VARCHAR(50), ingresos INT(11), telefono1 VARCHAR(15) NOT NULL, telefono2 VARCHAR(15), correo VARCHAR(50), lugar_de_trabajo VARCHAR(15), telefono_trabajo VARCHAR(15), fecha_creacion DATE DEFAULT CURRENT_TIMESTAMP NOT NULL, creado_por INT(11) NOT NULL, fecha_modificacion DATE, modificado_por INT(11), fecha_eliminacion DATE, eliminado_por INT(11))")
        cursor['cursor'].execute("CREATE TABLE Prestamos (id INT AUTO_INCREMENT PRIMARY KEY,id_cliente INT NOT NULL, valor_de_prestamo FLOAT(10) NOT NULL, balance_actual FLOAT(10) NOT NULL, fecha_desembolso DATE NOT NULL, dia_de_pago INT(2) NOT NULL, frecuencia_de_interes VARCHAR(10) NOT NULL, tasa_de_interes FLOAT(2) NOT NULL, fecha_cambio_tasa_de_interes DATE,  tipo_de_amortizacion VARCHAR(50) NOT NULL,  tiempo_de_prestamo INT(11) NOT NULL, aplica_garantia INT(1), fecha_creacion DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,  creado_por INT(11) NOT NULL, fecha_modificacion DATE, modificado_por INT(11), fecha_eliminacion DATE, eliminado_por INT(11))")

        password = encriptar("1234")

        insert_roles = "INSERT INTO Roles (descripcion, creado_por) VALUES ('super_admin', 1)"
        insert_usuarios = f"INSERT INTO Usuarios (correo, nombre, contrasena, id_rol, creado_por) VALUES ('testing@testing.com','Super_admin', '{password}', 1, 1)"
            
        cursor['cursor'].execute(insert_usuarios)
        cursor['cursor'].execute(insert_roles)
        cursor['connection'].commit()
            
        return {'resultado':1}
    except:
        cursor['connection'].rollback()
        return {'resultado':0}
 

    



