import mysql.connector

class Conexion():
    #Crear variable global
    licenciaUsada = None

    def __init__(self):
        #Conexión a la base de datos
        self.conexion = mysql.connector.connect(host="bk6kfeniyycp289t75lt-mysql.services.clever-cloud.com",
                                                user="uuzmgrlfqybyuyn8",
                                                passwd="kHNen4hk43sgZA7SmLkr", 
                                                database="bk6kfeniyycp289t75lt")

    #Función para buscar Usuario en la BD
    def buscaUsuario(self,users):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "SELECT idLicencia FROM Usuario WHERE correo = {}".format(users)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se capturan los resultados de la consulta
        correo = cur.fetchall()
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
        #Retorna el o los valores obtenidos en forma de lista
        return correo

    #Función para buscar contraseña, que dependa del correo de usuario en la BD
    def buscaContrasena(self,contrasena,users):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "SELECT * FROM Usuario WHERE correo = {} and contrasena = {}".format(users,contrasena)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se capturan los resultados de la consulta
        contrasena = cur.fetchall()
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
        #Retorna el o los valores obtenidos en forma de lista
        return contrasena

    #Función para buscar en la BD el nombre de usuario actual utilizando el PyStruct
    def nombreUsuarioActual(self):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "SELECT nombre FROM Usuario WHERE idLicencia = {}".format(licenciaUsada)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se capturan los resultados de la consulta
        nombreUsuario = cur.fetchall()
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
        #Retorna el o los valores obtenidos en forma de lista
        return nombreUsuario

    #Función para buscar  Universidades en la BD
    def buscaUniversidades(self):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "SELECT nombre FROM Universidad"
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se capturan los resultados de la consulta
        universidades = cur.fetchall()
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
        #Retorna el o los valores obtenidos en forma de lista
        return universidades

    #Función para validar la licencia ingresada por el usuario
    def validarLicencia(self, licencia):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "SELECT * FROM Licencia WHERE licencia={}".format(licencia)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se capturan los resultados de la consulta
        infoLicencia = cur.fetchall()
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
        #Retorna el o los valores obtenidos en forma de lista
        return infoLicencia

    #Función para registrar a un Usuario en la BD
    def registrarUsuario(self,nombreR,apellidoR,correoR,contrasenaR,idLicenciaR,idUniversidadR):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "INSERT INTO Usuario (nombre, apellido, correo, contrasena, idLicencia, idUniversidad) VALUES (%s, %s, %s, %s, %s, %s)"
        #Como la consulta es un insert se genera el envió de variables por referencia
        val = (nombreR,apellidoR,correoR,contrasenaR,idLicenciaR,idUniversidadR)
        cur.execute(sql, val)
        sql = "UPDATE Licencia SET estado = {} WHERE idLicencia = {}".format(1,idLicenciaR)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()

    #Función para el control del inicio de sesion de una cuenta en la BD
    def registarInicioSesion(self, idLicenciaR):
        #Manejo de la variable global licenciaUsada
        global licenciaUsada
        #Asignción de valor
        licenciaUsada = idLicenciaR
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "UPDATE Licencia SET sesionEstado = {} WHERE idLicencia = {}".format(1,idLicenciaR)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()
    
    #Función para el control de cierre de sesion de una cuenta en la BD
    def registarCerrarSesion(self):
        #Se genera un puntero a la conexión
        cur = self.conexion.cursor()
        #Se construye la consulta o sentencia SQL a realizar
        sql = "UPDATE Licencia SET sesionEstado = {} WHERE idLicencia = {}".format(0,licenciaUsada)
        #Se ejecuta la sentencia SQL
        cur.execute(sql)
        #Se finaliza o cierra la ejecución
        cur.close()
        #Y por ultimo cerramos la conexión a la BD
        self.conexion.commit()