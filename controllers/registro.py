from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.registro import f_Registrarse
from mensajes import mensajes
from db import conexionDB
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator
import time

class Registrarse(QWidget, f_Registrarse):

    #Función contructor de la clase
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        #Crear validadores para los campos especificados
        validator = QRegExpValidator(QRegExp(r'[a-z, A-Z]+'))
        validator2 = QRegExpValidator(QRegExp(r'[A-Z]+'))
        self.nombre.setValidator(validator)
        self.apellidos.setValidator(validator)
        self.licencia.setValidator(validator2) 

        #Conexión de herramientas de la interfaz con las funciones de la clase
        self.agregarUniversidades()
        self.b_Cancelar.clicked.connect(self.cancelarRegistro)               
        self.b_Registrarse.clicked.connect(self.registrar)   
   
    #Función para agregar universidades al combobox del formulario en la UI
    def agregarUniversidades(self):
        #Se realiza una conexión a la BD
        self.datos = conexionDB.Conexion()
        #Se hace el llamada a la función buscaUniversidades para su respectiva consulta a la BD
        universidades = self.datos.buscaUniversidades() 
        #Se toma el tamaño de la lista de universidades   
        conta = len(universidades)
        #Se le agregan estilos al combobox
        self.cb_Universidades.setEditable(True)
        self.cb_Universidades.lineEdit().setReadOnly(True)
        self.cb_Universidades.lineEdit().setAlignment(Qt.AlignCenter)
        #Se le manda la información al combobox
        for i in range(0,conta):
            self.cb_Universidades.addItem(*universidades[i], Qt.AlignCenter, Qt.TextAlignmentRole)

    #Función para cancelar el registro de Usuario
    def cancelarRegistro(self):
        #Cancelar registro y cerrar ventana Registro Usuario
        self.hide()

    #Funcioón para registrar un usuario
    def registrar(self):
        #Se crea la conexión a la BD
        self.datos = conexionDB.Conexion()
        #Se capturan los datos ingresados por el usuario
        nombre = self.nombre.text()
        apellido = self.apellidos.text()
        correo = self.correo.text()
        licencia = self.licencia.text()
        contrasena = self.contrasena.text()
        confContrasena = self.confirmarContrasena.text()
        universidad = self.cb_Universidades.currentText()

        #Se valida que haya seleccionado una universidad
        if(universidad != 'Universidad'):
            #Se valida que ningún campos se encuentra vacío
            if nombre != '' and apellido != '' and correo != '' and licencia != '' and contrasena != '' and confContrasena != '':
                #Se valida que el correo contenga el simbolo @
                arroba = False
                for i in correo:
                    if i == '@':
                        arroba = True
                        break
                
                #condición para cuando el correo tiene @
                if arroba == True:
                    #Se valida que las contraseñas ingresadas concuenrden
                    if contrasena==confContrasena: 
                        #Se verifica que la licencia ingresada se encuentre activa en la BD                   
                        licencia = str("'" + licencia + "'")
                        #Se llama a la función validarLicencia
                        infoLicencia = self.datos.validarLicencia(licencia)
                        lista = []

                        for i in infoLicencia[0]:
                            lista.append(i)
                        #Condición para cuando la licencia este activa
                        if lista[2] == 0:               
                            idU = int (self.cb_Universidades.currentIndex())
                            idL = int (lista[0])
                            #Se llama la función de registrarUsuario para la consulta INSERT a la BD
                            self.datos.registrarUsuario(nombre.capitalize(),apellido.capitalize(),correo.lower(),contrasena.lower(),idL,idU)
                            #Se genera el progreso en la barra de progreso
                            for i in range(0,99):
                                time.sleep(0.02)
                                self.progreso.setValue(i)
                                self.l_Cargando.setText('Cargando...')
                            #Se cierra la ventana Registro de Usuario
                            self.hide()
                            #Se presenta mensaje informativo del registro exitoso
                            mensajes.mensajeInfo('Registro', 'Usuario registrado exitosamente')
                        else:
                            #Mensaje de error cuando la licencia ingresada ya pertenece a otro usuario
                            mensajes.mensajeError('Error', 'La licencia ingresada existe para otro usuario\n'
                                                'valide e intente de nuevo')
                    else:
                        #Mensaje de error para el momento en que las contraseñas ingresadas no coincidan
                        mensajes.mensajeError('Error', 'Las contraseñas ingresadas deben coincidir')
                else:
                    #Mensaje de error si el correo no cotiene el simbolo @
                    mensajes.mensajeError('Error', 'El campo correo debe contener un @')
            else:
                #Mensaje de error, por si algún campo se encuentra vacío
                mensajes.mensajeError('Error','Ningun campo puede estar vacío')
        else:
            #Mensaje de error, por si el usuario no seleccionó universidad
            mensajes.mensajeError('Error','Debe seleccionar una Universidad')
