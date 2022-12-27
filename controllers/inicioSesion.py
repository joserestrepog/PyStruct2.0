#Librerías a utilizar en la clase iniciarSesion
from db import conexionDB
import time
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtGui import QCloseEvent
from views.inicioSesion import f_InicioSesion
from mensajes import mensajes
from controllers.registro import Registrarse
from controllers.main import Main
import sys   

 
class iniciarSesion(QWidget, f_InicioSesion):

    #Función contructor de la clase 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Conexión de herramientas de la interfaz y funciones de la clase
        self.datos = conexionDB.Conexion()
        self.b_IniciarSesion.clicked.connect(self.iniciarSesion)
        self.b_Registrar.clicked.connect(self.registrar)   

    #Función iniciarSesion
    def iniciarSesion(self):        
        
        #Captura de datos ingresados por el usuario
        usuario = self.correo.text()
        contrasena = self.contrasena.text()

        #Validar que ningún campo esté vacío
        if usuario != '' and contrasena != '':

            #Arreglar datos para mandar a consulta de base de datos
            usuario = str("'" + usuario + "'")
            contrasena = str("'" + contrasena + "'")

            #Crear instancias con la conexión a la BD
            dato1 = self.datos.buscaUsuario(usuario)
            dato2 = self.datos.buscaContrasena(contrasena, usuario)
            
            #Verificar que los datos ingresados sean correctos
            if dato1 != [] and dato2 != []:
                #Generar progreso en la barra de progreso
                self.l_Cargando.setText('Cargando...')
                for i in range(0,99):
                    time.sleep(0.02)
                    self.progreso.setValue(i)                
                
                #Minimizar el inicio de sesión e instanciar y mostrar ventana principal PyStruct
                self.showMinimized() 
                window = Main(self)
                window.show()
                #Vaciar los campos de inicio de sesión
                self.correo.setText('')
                self.contrasena.setText('')
                self.progreso.setValue(0)
                self.l_Cargando.setText('')

                #Modificar y registrar inicio de sesión exitoso en la BD
                for i in dato1:
                    data = i
                self.datos.registarInicioSesion(int (*data))
            else:
                #Mensaje de error en caso de que los datos ingresados sean incorrectos
                mensajes.mensajeError('Error de Inicio','El usuario y/o contraseña ingresados son inconrrectos')
                self.correo.setText('')
                self.contrasena.setText('')                                
        else:
            #Mensaje de error en caso de que al menos 1 campo este vaío
            mensajes.mensajeError('Error de Datos','Ningún campo puede estar vacío')
    
    #Funcion para registrar Usuario nuevo
    def registrar(self):
        #Generar progreso en la barra de progreso
        self.l_Cargando.setText('Cargando...')
        for i in range(0,99):
            time.sleep(0.02)
            self.progreso.setValue(i)
        
        #Crear instancia y hacer visible la ventana Registro de Usuario
        window = Registrarse(self)
        window.show()
        #Vaciar los campos de inicio de sesión
        self.progreso.setValue(0)
        self.l_Cargando.setText('')
     
                

