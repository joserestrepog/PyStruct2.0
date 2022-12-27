#Librerías a utilizar en la clase GraficaLineal
from PySide2.QtWidgets import QWidget
from views.graficaLineal import f_GraficaLineas
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from pylab import *

class GraficaLineal(QWidget, f_GraficaLineas):

    #Creación de variables globales
    data = None

    #Función contructor de la clase
    def __init__(self, dataset, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        #Variables Globales
        global data

        #Asignación de contenido a las variables globales
        data = dataset

        #Conexión entre herramientas de la interfaz y funciones de la clase
        self.setWindowFlag(Qt.Window)
        self.b_Aceptar.clicked.connect(self.graficaLinealSeleccionada)
        self.b_Cancelar.clicked.connect(self.cancelarSeleccion)

    #Función de gráfica de Línea
    def graficaLinealSeleccionada(self):

        #Captura del color seleccionado por el ususario en la UI
        color = self.cb_ColorParticulas.currentText()

        #Verificar dimension de la gráfica (2D)
        if self.rb_2D.isChecked(): 
                       
            #Divison de variables de graficar
            x = data.iloc[:,0]
            y = data.iloc[:,1]
            
            #Generar figura con los atributos correspondientes
            plt.figure()
            plt.plot(x,y, color=color)
            plt.show()      

        #Verificar dimension de la gráfica (3D)
        elif self.rb_3D.isChecked():

            #Divison de variables de graficar
            x = data.iloc[:,0]
            y = data.iloc[:,1]
            
            #Generar figura con los atributos correspondientes
            fig = plt.figure()
            ax  = Axes3D(fig)
            ax.plot(x,x,y, color=color ,linewidth=15)
            plt.show()

    #Función para cancelar proceso
    def cancelarSeleccion(self):
        #Cancelar proceso y cerrar ventana
        self.hide()
