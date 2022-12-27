#Librerias a Utilizar en la clase GraficaDispersion
from PySide2.QtWidgets import QWidget
from views.graficaDispersion import f_GraficaDispersion
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from mensajes import mensajes

class GraficaDispersion(QWidget, f_GraficaDispersion):

    #Creación de variables globales
    data = None
    restaCol = None

    #Función contructor de la clase
    def __init__(self, dataset, rescol, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        #Variables Globales
        global restaCol
        global data

        #Asignación de contenido a las variables globales
        data = dataset
        restaCol = rescol
        
        #Conexión entre herramientas de la interfaz y funciones de la clase
        self.setWindowFlag(Qt.Window)
        self.b_Aceptar.clicked.connect(self.graficaDispersionSeleccionada)
        self.b_Cancelar.clicked.connect(self.cancelarSeleccion)

    #Función de gráfica de Dispersión
    def graficaDispersionSeleccionada(self):

        #Captura del color seleccionado por el ususario en la UI
        color = self.cb_ColorParticulas.currentText()
        #Captura del tamaño seleccionado por el ususario en la UI
        tamano = int (self.cb_TamanoParticulas.currentText())

        #Validación de la selección del combobox (2D)
        if self.rb_2D.isChecked():
            seleccion = 2
            #Verificar dimension de la gráfica (2D)
            if seleccion == restaCol:
                #Divison de variables de graficar
                x = data.iloc[:,0]
                y = data.iloc[:,1]
                
                #Generar figura con los atributos correspondientes
                plt.figure()
                plt.scatter(x,y, c=color, s=tamano)
                plt.show()
            else:
                #Mensaje de error en caso de que no corresponda el tipo de gráfica y matriz seleccionada
                mensajes.mensajeError('Error de Dimensión','La matriz de datos no corresponde al numero de columnas del grafico 2D')
        #Validación de la selección del combobox (3D)
        elif self.rb_3D.isChecked():
            seleccion = 3
            #Verificar dimension de la gráfica (3D)
            if seleccion == restaCol:
                #Divison de variables de graficar
                x = data.iloc[:,0]
                y = data.iloc[:,1]
                z = data.iloc[:,2]

                #Generar figura con los atributos correspondientes
                fig = plt.figure()
                ax = fig.add_subplot(111,projection='3d')
                ax.scatter3D(x,y,z, c=color, s=tamano)
                plt.show()

            else:
                #Mensaje de error en caso de que no corresponda el tipo de gráfica y matriz seleccionada
                mensajes.mensajeError('Error de Dimensión','La matriz de datos no corresponde al numero de columnas del grafico 3D')
        else:
            #Mensaje de alerta en caso de no seleccionar dimensión de la gráfica
            mensajes.mensajeAlerta('Alerta','Por Favor Seleccione dimension a graficar')
    
    #Función para cancelar proceso
    def cancelarSeleccion(self):
        #Cancelar proceso y cerrar ventana
        self.hide()