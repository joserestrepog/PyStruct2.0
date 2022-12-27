from PySide2.QtWidgets import QWidget, QFileDialog
from views.predictor import f_Predictor
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator
import joblib
import sklearn 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mensajes import mensajes
import os


class PredecirEstructura(QWidget, f_Predictor):

    #Función contructor de la clase
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        
        #Crear validador de solo numeros para los campos especificados
        validator = QRegExpValidator(QRegExp(r'[0-9]+')) 
        self.ancho.setValidator(validator)
        self.cantParticulas.setValidator(validator)
        self.temperatura.setValidator(validator)

        #Conexión de herramientas de la interfaz con las funciones de la clase
        self.b_Cancelar.clicked.connect(self.cancelarPrediccion)
        self.b_Predecir.clicked.connect(self.hacerPrediccion)
        self.cb_Material.setEditable(True)
        self.cb_Material.lineEdit().setReadOnly(True)
        self.cb_Material.lineEdit().setAlignment(Qt.AlignCenter)

    #Función para hacer la predicción
    def hacerPrediccion(self):        

        #Validar elección de material a predecir
        if self.cb_Material.currentText() != 'Seleccione el Material':
            #Verificar si los campos están vacíos
            if self.ancho.text() != '' and self.cantParticulas.text() != '' and self.temperatura.text() != '':
                #Capturar los datos siempre y cuando sean mayores a cero
                if int (self.ancho.text()) > 0 and int (self.cantParticulas.text()) > 0 and int (self.temperatura.text()) > 0:
                   
                    if self.cb_Material.currentText() == 'Hierro':
                   
                        #Cargar el modelo de predicción de ML
                        #regressor = joblib.load('./modeloML/modelo_entrenado.pkl')
                        regressor = joblib.load('./modeloML/modelo_entrenado.pkl')
                        #Capturar color seleccionado por el usuario para la gráfica de la predicción
                        color = self.cb_ColorParticulas.currentText()
                        #Capturar tamaño para las particulas de la gráfica
                        tamano = int (self.cb_TamanoParticulas.currentText())

                        #Capturar datos ingresados por el Usuario
                        anchocaja = int (self.ancho.text())
                        cantParticulas = int (self.cantParticulas.text())
                        Temperatura = int (self.temperatura.text())
                        NParticula = 0
                        
                        #Crear dataframe para guardar matriz de datos
                        y_pred2 = pd.DataFrame()
                        #Crear dos listas para interacambiar los datos que se predicen
                        lista = []
                        lista2 = []
                        
                        #Ciclo for para obtener cada registro de la predicción
                        for i in range(0,cantParticulas):
                            y_pred = regressor.predict([[anchocaja,cantParticulas,Temperatura,i]])
                            lista.append( float (y_pred[0,0]));lista.append( float (y_pred[0,1]));lista.append(float (y_pred[0,2]))
                            lista2.append(lista)
                            lista = []

                        #Crear copia de los datos para graficar y crear archivo de datos 
                        data = pd.DataFrame(lista2)

                        #Separación de columnas para graficar
                        x = data.iloc[:,0]
                        y = data.iloc[:,1]
                        z = data.iloc[:,2]

                        #Generar la figura de dispersión
                        fig = plt.figure()
                        ax = fig.add_subplot(111,projection='3d')
                        ax.scatter3D(x,y,z, c=color, s=tamano)
                        plt.show()
                        
                        #Guardar prediccion en carpeta prediccionML
                        dir_path = os.getcwd() #codigo para abrir directorio raíz del proyecto
                        dir_path = dir_path + '/prediccionML/prediccion.csv'
                        data.to_csv(dir_path, header=False, index=False)

                    

                    if self.cb_Material.currentText() == 'Níquel':
                                                 #Cargar el modelo de predicción de ML
                        regressor = joblib.load('./modeloML/modelo_entrenadoNiquel.pkl')
                        #Capturar color seleccionado por el usuario para la gráfica de la predicción
                        color = self.cb_ColorParticulas.currentText()
                        #Capturar tamaño para las particulas de la gráfica
                        tamano = int (self.cb_TamanoParticulas.currentText())

                        #Capturar datos ingresados por el Usuario
                        anchocaja = int (self.ancho.text())
                        cantParticulas = int (self.cantParticulas.text())
                        Temperatura = int (self.temperatura.text())
                        NParticula = 0
                        
                        #Crear dataframe para guardar matriz de datos
                        y_pred2 = pd.DataFrame()
                        #Crear dos listas para interacambiar los datos que se predicen
                        lista = []
                        lista2 = []
                        
                        #Ciclo for para obtener cada registro de la predicción
                        for i in range(0,cantParticulas):
                            y_pred = regressor.predict([[i,anchocaja,cantParticulas,Temperatura]])
                            lista.append( float (y_pred[0,0]));lista.append( float (y_pred[0,1]));lista.append(float (y_pred[0,2]))
                            lista2.append(lista)
                            lista = []

                        #Crear copia de los datos para graficar y crear archivo de datos 
                        data = pd.DataFrame(lista2)

                        #Separación de columnas para graficar
                        x = data.iloc[:,0]
                        y = data.iloc[:,1]
                        z = data.iloc[:,2]

                        #Generar la figura de dispersión
                        fig = plt.figure()
                        ax = fig.add_subplot(111,projection='3d')
                        ax.scatter3D(x,y,z, c=color, s=tamano)
                        plt.show()
                        
                        #Guardar prediccion en carpeta prediccionML
                        dir_path = os.getcwd() #codigo para abrir directorio raíz del proyecto
                        dir_path = dir_path + '/prediccionML/prediccion.csv'
                        data.to_csv(dir_path, header=False, index=False)


                else:
                    #Mensaje de alerta en caso de que almenos 1 campo sea menos o igual a 0
                    mensajes.mensajeAlerta('Alerta', 'Todos los campos deben ser mayor a cero')
            else:
                #Mensaje de error en caso de que algún campo esté vacío
                mensajes.mensajeError('Error', 'Ningún campo puede estar vacío')
        else:
            #Mensaje de error en caso de no haber seleccionado material a predecir
            mensajes.mensajeError('Error Predicción','Debe seleccionar el material a predecir')

    #Función cancelar proceso
    def cancelarPrediccion(self): 
        #Cancelar proceso y cerrar ventana       
        self.hide()