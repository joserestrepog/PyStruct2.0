#Librerías necesarias para las funciones de la clase Main
from PySide2.QtWidgets import QColorDialog, QMainWindow, QFileDialog, QTabWidget, QFormLayout, QRadioButton, QTableWidget, QTableWidgetItem, QTreeView, QFileSystemModel, QVBoxLayout, QWidget
from PySide2.QtCore import QModelIndex, Qt
from PySide2.QtGui import QColor , QFont, QPalette
from views.main import f_PyStruct
from Tabla import funcionTablaMain
from db import conexionDB
from controllers.graficaDispersion import GraficaDispersion
from controllers.graficaLineal import GraficaLineal
from controllers.predictor import PredecirEstructura
from mensajes import mensajes
from os import startfile
from PySide2.QtWidgets import QApplication
import sys
import os
import pandas as pd
import numpy as np


class Main(QMainWindow, f_PyStruct):

    #Creación de variables globales
    a = None
    camposSeleccionados = None; rangoSeleccionado = None
    contaPestanas = None; contaNewPestanas = None

    #Función constructor de la clase
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)      

        #Manejo de variables globales
        global rangoSeleccionado
        global contaPestanas
        global contaNewPestanas

        contaPestanas = 1
        contaNewPestanas = 1
        rangoSeleccionado = 0   

        #Conexion entre el menu de la UI y las funciones de la clase Main
        self.abrir.triggered.connect(self.abrirArchivo)
        self.guardarComo.triggered.connect(self.guardarArchivo)
        self.nuevo.triggered.connect(self.agregarPestana)
        self.pegar.triggered.connect(self.pegarSeleccion)
        self.copiar.triggered.connect(self.copiarSeleccion)
        self.cortar.triggered.connect(self.cortarSeleccion)
        self.cerrar.triggered.connect(self.closeEvent)
        self.cerrarSesion.triggered.connect(self.cerrarSesiones)
        self.documentacion.triggered.connect(self.documentacionApp)
        self.estadoLicencia.triggered.connect(self.cuenta)

        #Conexión entre botones y funciones
        self.b_Importar.clicked.connect(self.abrirArchivo)    
        self.b_Exportar.clicked.connect(self.guardarArchivo)
        self.b_graficar.clicked.connect(self.graficarSeleccion)
        self.b_Predictor.clicked.connect(self.modeloPredictor)        
        self.b_Copiar.clicked.connect(self.copiarSeleccion)
        self.b_Pegar.clicked.connect(self.pegarSeleccion)
        self.b_Cortar.clicked.connect(self.cortarSeleccion)
        self.b_Centrado.clicked.connect(self.estiloCentrar)
        self.b_Derecha.clicked.connect(self.estiloDerecha)
        self.b_Izquierda.clicked.connect(self.estiloIzquierda)
        self.b_Negrilla.clicked.connect(self.estiloNegrilla)
        self.b_Cursiva.clicked.connect(self.estiloCursiva)
        self.b_Subrayado.clicked.connect(self.estiloSubrayar)
        self.b_PaletaColores.clicked.connect(self.estiloPaletaColor)
        self.b_Qnegrilla.clicked.connect(self.quitarEstiloNegrilla)
        self.b_Qcursiva.clicked.connect(self.quitarEstiloCursiva)
        self.b_Qsubrayado.clicked.connect(self.quitarEstiloSubrayar)

        #Conexión entre combobox y funciones
        self.cb_TipoGrafica.setEditable(True)
        self.cb_TipoGrafica.lineEdit().setReadOnly(True)
        self.cb_TipoGrafica.lineEdit().setAlignment(Qt.AlignCenter)        
        self.cb_TipoLetra.activated.connect(self.estiloTipoFuente)
        self.cb_TamanoLetra.activated.connect(self.estiloTamano)

        #Conexión entre espacios de trabajos y funciones
        self.tree.doubleClicked.connect(self.tree_cilcked)
        self.treePred.doubleClicked.connect(self.abrirPrediccion)
        self.tw_Pestanas.tabCloseRequested.connect(self.cerrarPestanas)
        self.arbolDeArchivos()
        self.actualizarPredicciones()
        
    #Función para crear y visualizar el arbol de archivos
    def arbolDeArchivos(self):
        dir_path = 'Este equipo' #Abrir directorio raíz del proyecto
        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        #Generar vista de archivos y carpetas en forma de arbol.        
        self.tree.setModel(self.model)
        #Indicar el directorio de inicio al arbol
        self.tree.setRootIndex(self.model.index(dir_path))

        #Mostrar ventana con el arbol de archivos
        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)
    
    #Función para actualizar el archivo de predicción 
    def actualizarPredicciones(self):
        dir_path = os.getcwd() #codigo para abrir directorio raíz del proyecto
        dir_path = dir_path + '/prediccionML'
        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)

        #Generar el arbol que contiene el archivo predicción
        self.treePred.setModel(self.model)
        self.treePred.setRootIndex(self.model.index(dir_path))
        self.treePred.setColumnWidth(200,400)
        self.treePred.setAlternatingRowColors(True)

        #Mostrar ventana con el archivo predicción
        layout = QVBoxLayout()
        layout.addWidget(self.treePred)
        self.setLayout(layout)

    #Función para importar un archivo al sistema
    def abrirArchivo(self):
        #Manejo de variables globales
        global contaNewPestanas
        global contaPestanas

        #Validación del total de pestañas en la vista principal
        if contaPestanas < 10:
            
            #Abrir modulo de importar o cargar archivo, con formatos (.csv, .xlsx, .dat)
            archivo = QFileDialog.getOpenFileName(self, 'Importar Archivo','C:/', 
                    "Arcivos Excel (*.csv);;Arcivos Excel (*.xlsx);;Archivos SDMSC (*.dat)")

            #Verificar que tipo de archivo intenta importar el usuario, en caso de ser .csv entra
            if archivo[1] == "Arcivos Excel (*.csv)":
                #Crear una nueva pestaña
                self.agregarPestana()
                #Leer el archivo importado
                dataset = pd.read_csv(archivo[0])
                
                #Capturar la cantidad de filas y columnas
                filas = dataset.shape[0]
                columnas = dataset.shape[1]         
                
                #Ciclo for para cargar los datos del archivo a una matriz o tabla
                for i in range(filas):
                    for j in range(columnas):
                        dato = dataset.iloc[i,j]
                        dato2 = QTableWidgetItem(str(dato))
                        globals()["tabla_New_Tab_"+str(contaNewPestanas)].setItem(i, j, dato2)
            
            #Verificar tipo de archivo, en caso de no ser .csv pero si .xlsx
            elif archivo[1] == 'Arcivos Excel (*.xlsx)':
                #Crear una nueva pestaña
                self.agregarPestana()
                #Leer el archivo importado
                dataset = pd.read_excel(archivo[0], sheet_name=0)
                
                #Capturar la cantidad de filas y columnas
                filas = dataset.shape[0]
                columnas = dataset.shape[1]
                
                #Ciclo for para cargar los datos del archivo a una matriz o tabla
                for i in range(filas):
                    for j in range(columnas):
                        dato = dataset.iloc[i,j]
                        dato2 = QTableWidgetItem(str(dato))
                        globals()["tabla_New_Tab_"+str(contaNewPestanas)].setItem(i, j, dato2)
            #Verificar tipo de archivo, en caso de ser .dat
            elif archivo[1] == 'Archivos SDMSC (*.dat)':
                #Crear una nueva pestaña
                self.agregarPestana()
                #Leer el archivo importado
                dataset = np.genfromtxt(archivo[0])         

                #Capturar la cantidad de filas y columnas
                filas = dataset.shape[0]
                columnas = dataset.shape[1]          
                
                #Ciclo for para cargar los datos del archivo a una matriz o tabla
                for i in range(filas):
                    for j in range(columnas):
                        dato = dataset[i,j]
                        dato2 = QTableWidgetItem(str(dato))
                        globals()["tabla_New_Tab_"+str(contaNewPestanas)].setItem(i, j, dato2)
        
        else:
            #Mensaje de alerta en caso de no poder importar el archivo por exceder el límite de pestañas que es = 10
            mensajes.mensajeAlerta('Alerta', 'La importación no se puede llevar a cabo porque excedió\n'
                                    'el limite de 10 pestañas')

    #Función para exportar archivos del sistema                
    def guardarArchivo(self):
        #Manejo de variables globales
        global rangoSeleccionado
        global contaPestanas

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Virificar que si existan pestañas visibles para el usuario
        if contaPestanas > 0:

            #Verificar la pestaña que desean exportar 
            if nomPestana != 'PyStruct':
                
                #Abrir modulo para exportar archivos, y capturar la ruta y tipo del archivo
                archivo = QFileDialog.getSaveFileName(self, 'Exportar Archivo','C:/',"Arcivos Excel (*.csv);;Arcivos Excel (*.xlsx);;Arcivos SDMSC (*.dat)")
                
                #Validar tipo de archivo que desea guardar el usuario (.dat)
                if archivo[1] == 'Arcivos SDMSC (*.dat)':
                    #Crear un archivo y abrirlo
                    dat = open(archivo[0], "w")
                    #Ciclo for para sobre escribir el archivo y almacenar cada uno de los datos de la matriz
                    for row in range(globals()["tabla_"+str(nomPestana)].rowCount()):
                        for column in range(globals()["tabla_"+str(nomPestana)].columnCount()):
                            #Validar que en la celda exista un valor distinto a null o vacíos
                            if globals()["tabla_"+str(nomPestana)].item(row, column) is not None:
                                #Capturar un valor de la tabla o matriz
                                valor = float (globals()["tabla_"+str(nomPestana)].item(row, column).text())
                                #Formato de guardado
                                #Si el número o dato es menor que 0 se agrega un tabular y posteriormente el dato
                                if valor < 0:           
                                    dat.write('\t')
                                    dat.write(globals()["tabla_"+str(nomPestana)].item(row, column).text())
                                #En caso de ser mayor o igual a 0, agregar un tabular, un espacio y luego el valor a guardar
                                else:
                                    dat.write('\t ')
                                    dat.write(globals()["tabla_"+str(nomPestana)].item(row, column).text())
                        #Escribir un salto de linea en el archivo
                        dat.write('\n')
                    #Cerrar el archivo exportado
                    dat.close()
                #En caso de que el tipo de archivo a exportar sea .csv o .xlsx
                else:
                    #Se crean listas para el intercambio de la información
                    lista = []
                    lista2 = []
                    dataset = pd.DataFrame()
                    
                    #El ciclo for es para capturar cada valor de las celdas de la tabla
                    for row in range(globals()["tabla_"+str(nomPestana)].rowCount()):
                        for column in range(globals()["tabla_"+str(nomPestana)].columnCount()):
                            #Validar que en la celda exista un valor distinto a null o vacíos                
                            if globals()["tabla_"+str(nomPestana)].item(row, column) is not None:
                                lista.append((globals()["tabla_"+str(nomPestana)].item(row, column).text()))
                        lista2.append(lista)
                        lista = []
                    dataset = pd.DataFrame(lista2)

                    #Exportar arhivo sea .csv o .xlsx
                    if archivo[1] == 'Arcivos Excel (*.csv)':
                        dataset.to_csv(archivo[0], index=False)
                    else:
                        dataset.to_excel(archivo[0], index=False)
            else:
                #Mensaje de error por exportar la pestaña PyStruct del sistema
                mensajes.mensajeError('Error de Exportación', 'La pestaña PyStruct no puede ser exportada')
        else:
            #Mensaje de error por no existir pestañas para exportar
            mensajes.mensajeError('Error Exportación', 'No hay ninguna pestaña para exportar')

    #Función para graficar un rango seleccionado por el ususario
    def graficarSeleccion(self):
        #Manejo de variables globales
        global rangoSeleccionado 

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar de que pestaña desean exportar
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0
            seleccionTipoGrafica = ""

            #Crear listas para intercambio de datos
            lista = []
            lista2 = []
            dataset = pd.DataFrame()
           
            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow()

                #Validar si el contenido seleccionado es completamente de numeros reales
                validarContenido = True
                for i in range(minrow,maxrow+1): 
                    for j in range(mincol,maxcol+1):                   
                        if  globals()["tabla_"+str(nomPestana)].item(i, j) == None :
                            validarContenido = False
                            break
                    else:
                        validarContenido = True
                                                   
                #Verficar si el usuario seleccionó mas de una columna para gráficar
                if (maxcol-mincol)>0:

                        #Capturar el tipo de gráfica del combobox
                        seleccionTipoGrafica = self.cb_TipoGrafica.currentText()

                        #Validar si el usuario si escogió un tipo de gráfica
                        if seleccionTipoGrafica != 'Tipo':
                            
                            #Verificar contenido real
                            if validarContenido == True:
                                
                                #Condicional para cuando el tipo de gráfica es Dispersión
                                if seleccionTipoGrafica == 'Dispersión':
                                    #Consultar si es 2D o 3D
                                    rescol = (maxcol-mincol)+1
                                    #Condicional para dispersión 3D
                                    if rescol == 3:
                                        #Ciclo for para capturar el rango seleccionado por el usuario
                                        for i in range(minrow,maxrow+1):
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol).text()))
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol+1).text()))
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i,maxcol).text()))
                                            lista2.append(lista)
                                            lista = []
                                        #Crear dataframe con los datos capturados
                                        dataset = pd.DataFrame(lista2)
                                        #Crear instancia del módulo GraficaDispersion e inicializarlo
                                        window = GraficaDispersion(dataset, rescol, self)
                                        window.show() 
                                    #Condicional para dispersión 2D
                                    elif rescol == 2:
                                        #Ciclo for para capturar el rango seleccionado por el usuario
                                        for i in range(minrow,maxrow+1):
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol).text()))
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol+1).text()))
                                            lista2.append(lista)
                                            lista = []
                                        #Crear dataframe con los datos capturados  
                                        dataset = pd.DataFrame(lista2)
                                        #Crear instancia del módulo GraficaDispersion e inicializarlo
                                        window = GraficaDispersion(dataset, rescol, self)
                                        window.show()
                                    
                                    else:
                                        #Mensaje de error para cuando no se selecciona la cantidad de columnas para este tipo de gráfica
                                        mensajes.mensajeError('Error de Parámetros','Debe seleccionar entre 2 y 3 columnas para este tipo de gráfica')
                                #Condicional para cuando el tipo de gráfica es Lineal
                                else:
                                    #Consultar si es 2D o 3D
                                    rescol = (maxcol-mincol)+1
                                    #Condicional para lineal 2D
                                    if rescol == 2:
                                        #Ciclo for para capturar el rango seleccionado por el usuario
                                        for i in range(minrow,maxrow+1):
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol).text()))
                                            lista.append( float (globals()["tabla_"+str(nomPestana)].item(i, mincol+1).text()))
                                            lista2.append(lista)
                                            lista = []
                                        #Crear dataframe con los datos capturados
                                        dataset = pd.DataFrame(lista2)
                                        #Crear instancia del módulo GraficaLineal e inicializarlo
                                        window = GraficaLineal(dataset, self)
                                        window.show()
                                    else:
                                        #Mensaje de alerta para cuando no se selecciona exactamente dos columnas para este tipo de gráfica
                                        mensajes.mensajeError('Error de Parámetros','Debe seleccionar exactamente dos columnas para este tipo de gráfica')
                            else:
                                #Mensaje de error por si la selección tiene valores nulos o vacíos
                                mensajes.mensajeError('Error de Contenido', 'Toda la selección debe tener numeros reales')
                        else:
                            #Mensaje de alerta por si el usuario no selecciona tipo de gráfica
                            mensajes.mensajeAlerta('Alerta','Debe seleccionar un tipo de gráfica')   
                else:
                    #Mensaje de alerta por si el usuario selecciona solo una columna
                    mensajes.mensajeAlerta('Alerta','Seleccione mas de una columna')
            else:
                #Mensaje de error por si no se cuentan con datos seleccionados
                mensajes.mensajeError('Error de Datos','No se cuenta con datos seleccionados para graficar') 
        else:
            #Mensajes de error en el caso de que quieran gráficar PyStruct
            mensajes.mensajeError('Error de Datos', 'La pestaña PyStruct no puede ser graficada, debido a su contenido') 

    #Función para instanciar y ejecutar módulo predictor
    def modeloPredictor(self):
        #Crear la instancia e inicializarla
        window = PredecirEstructura(self)
        window.show()

    #Función para abrir los archivos de árbol de archivos con el programa predeterminado en el PC ejecutor
    def tree_cilcked(self, QModelidx):
        #Abrir archivos con el programa predeterminado, al darle doble clic
        startfile(self.model.filePath(QModelidx))

    #Función para abrir el archivo predicción
    def abrirPrediccion(self):
        #Manejo de variables
        global contaPestanas
        global contaNewPestanas

        dir_path = os.getcwd() #codigo para abrir directorio raíz del proyecto
        dir_path = dir_path + '/prediccionML/prediccion.csv'
        
        #Leer el archivo .csv en la dirección indicada
        dataset = pd.read_csv(dir_path)

        #Validar si hay espacio para la creación de una nueva pestaña
        if contaPestanas < 10:
            #Llamar función para crear nueva pestaña
            self.agregarPestana()

            #Capturar cantidad de filas y columnas del archivo
            filas = dataset.shape[0]
            columnas = dataset.shape[1]
            
            #Ciclo for para leer datos del dataframe y enviarlos a la tabla o matriz
            for i in range(filas):
                for j in range(columnas):
                    dato = dataset.iloc[i,j]
                    globals()["tabla_New_Tab_"+str(contaNewPestanas)].setItem(i, j, QTableWidgetItem(str(dato)))
        else:
            #Mensaje de alerta en el momento en que se exceda el limite de pestañas que es = a 10
            mensajes.mensajeAlerta('Alerta', 'No se puede cargar la matriz porque excedió\n'
                                    'el limite de 10 pestañas')       

    #Funcion para agregar una nueva pestaña      
    def agregarPestana(self):
        #Manejo de variables globales
        global contaPestanas
        global contaNewPestanas

        #Validar si hay disponibilidad de agregar una nueva pestaña
        if contaPestanas < 10:
            
            #Contadores de cantidad de pestañas y nombre de pestaña
            contaPestanas = contaPestanas + 1
            contaNewPestanas = contaNewPestanas + 1

            #Crear la pestaña a traves del llamado de la función en contexto
            globals()["tabla_New_Tab_"+str(contaNewPestanas)] = funcionTablaMain.funcionTabla(self)

            #Crear un widget de contenido
            globals()["tab_"+str(contaNewPestanas)] = QWidget()

            #Crear un espacio de trabajo
            layout = QFormLayout()

            #Concatenar estructura
            layout.addWidget(globals()["tabla_New_Tab_"+str(contaNewPestanas)])
            globals()["tab_"+str(contaNewPestanas)].setLayout(layout)
            nombrePes = "New_Tab_"+str(contaNewPestanas)
            #Adicionar pestañas a la vista del usuario 
            self.tw_Pestanas.addTab(globals()["tab_"+str(contaNewPestanas)],nombrePes)
            self.tw_Pestanas.setCurrentIndex(contaPestanas - 1) #HACER FOCUS EN LA NUEVA PESTAÑA
        else:
            #Mensaje de alerta, cuando no se permiten crear mas pestañas
            mensajes.mensajeAlerta('Alerta', 'Solo se permiten 10 pestañas')

    #Función para cerrar las pestañas del espacio de trabajo     
    def cerrarPestanas(self, index):
        #Manejo de variables globales
        global contaPestanas

        #Capturar el nombre de la pestaña en la que se posiciona el usuario
        nomPestana = self.tw_Pestanas.tabText(index)

        #Condicional para ver que pestaña desean eliminar (Si es PyStruct o cualquier otra)
        if nomPestana != 'PyStruct':
            globals()["tabla_"+str(nomPestana)].clearContents()
            
            #Eliminar pestaña
            self.tw_Pestanas.removeTab(index)
        else:
            #Eliminar pestaña
            self.tw_Pestanas.removeTab(index)
        
        #Disminuir en 1 el conta de pestañas
        contaPestanas = contaPestanas - 1 

    #Funcion para copiar cierta cantidad de datos
    def copiarSeleccion(self):
        #Manejo de variables globales
        global rangoSeleccionado 

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar de que pestaña desean exportar
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()
            
            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Crear listas para intercambio de datos
            lista = []
            lista2 = []
            dataset = pd.DataFrame()           

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != 0:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow()

                #Ciclo for para capturar el rango seleccionado por el usuario
                for i in range(minrow,maxrow+1): 
                    for j in range(mincol,maxcol+1):                   
                        if  globals()["tabla_"+str(nomPestana)].item(i, j) != None :
                            lista.append(float (globals()["tabla_"+str(nomPestana)].item(i, j).text()))                            
                        else:
                            lista.append(' ')
                    lista2.append(lista)
                    lista = []
                #Crear dataframe con los datos capturados             
                dataset = pd.DataFrame(lista2)
                #Enviar dataset al clipboard
                dataset.to_clipboard(index=False)

            else:
                #Mensaje de error, al no encontrarse datos seleccionados
                mensajes.mensajeError('Error de Datos','No se cuenta con datos seleccionados para copiar') 
        else:
            #Mensaje de error, al intentar copiar la pestaña PyStuct
            mensajes.mensajeError('Error de Parámetros', 'La pestaña PyStruct no puede ser copiada, debido a su contenido')  

    #Funcion para pegar elementos copiados previamente
    def pegarSeleccion(self):

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)
        
        #Crear dataframe
        dataset = pd.DataFrame()

        #Pegar elementos del clipboard al dataset
        dataset = pd.read_clipboard()
        
        #Obtener filas y columas del dataset
        filas = dataset.shape[0]
        columnas = dataset.shape[1]

        if nomPestana != 'PyStruct':

            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()
            #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
            if rangoSeleccionado != []:
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow()
                #Establecer un minimo de columna de respaldo
                mincolRespaldo = mincol
                
                #Ciclo for para pegar elementos a la tabla 
                for i in range(filas):
                    for j in range(columnas):
                        dato = dataset.iloc[i,j]
                        globals()["tabla_"+str(nomPestana)].setItem(minrow, mincol, QTableWidgetItem(str(dato)))
                        mincol = mincol + 1
                    minrow = minrow + 1
                    mincol = mincolRespaldo

            else:
                #Mensaje de error, para el momento en que el usuario no indique posicion inicial de elementos en la tabla
                mensajes.mensajeError('Error', 'Debe indicar la posición inicial para pegar el contenido')
        else:
            #Mensaje de error, para el momento en que quieran pegar en PyStruct
            mensajes.mensajeError('Error de Parámetros', 'En la pestaña PyStruct no se puede pegar contenido')

    #Función para cortar datos seleccionados
    def cortarSeleccion(self):
        #Manejo de variables globales
        global rangoSeleccionado 

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar de que pestaña desean exportar
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()
            
            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0
            
            #Crear listas para intercambio de datos
            lista = []
            lista2 = []
            dataset = pd.DataFrame()           

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != 0:
                
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow()

                #Ciclo for para capturar el rango seleccionado por el usuario
                for i in range(minrow,maxrow+1): 
                    for j in range(mincol,maxcol+1):                   
                        if  globals()["tabla_"+str(nomPestana)].item(i, j) != None :
                            lista.append(float (globals()["tabla_"+str(nomPestana)].item(i, j).text()))                            
                        else:
                            lista.append(' ')
                    lista2.append(lista)
                    lista = [] 
                #Crear dataframe con los datos capturados             
                dataset = pd.DataFrame(lista2)
                dataset.to_clipboard(index=False)

                #Enviar espacios en blanco a campos cortados
                for i in range(minrow,maxrow+1): 
                    for j in range(mincol,maxcol+1):
                        globals()["tabla_"+str(nomPestana)].item(i, j).setText('')

            else:
                #Mensaje de error, para cuando no se tengan datos seeccionados
                mensajes.mensajeError('Error de Datos','No se cuenta con datos seleccionados para ejecutar cortar') 
        else:
            #Mensaje de error, para el momento en que quieran cortar PyStruct
            mensajes.mensajeError('Error de Parámetros', 'La pestaña PyStruct no puede ser cortada, debido a su contenido') 

    #Función para abrir documentación de PyStruct
    def documentacionApp(self, QModelidx):
        #Abrir documentación de PyStruct, con el programa predeterminado en el PC ejecutor
        os.startfile(".\\Documentacion\\Solicitud Academica original 4253_1.pdf")

    #Función para consultar la cuenta iniciada y version de PyStruct
    def cuenta(self):
        #Crear una conexión a la BD
        self.datos = conexionDB.Conexion()

        #Llamar la funcion para consultar el usuario actual
        nombreUsuario = self.datos.nombreUsuarioActual()
        #Cicl for para interpretar el resultado de consulta
        for i in nombreUsuario:
            nombreUsuario = i
        #Mensaje informativo visualizado para el usuario.
        mensajes.mensajeInfo('Información de Cuenta', 'Hola ' + str(*nombreUsuario) + ' has iniciado sesión \n'+
                              'en PyStruct en su versión 1.0')

    #Función para darle alineación centrada a los datos
    def estiloCentrar(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        globals()["tabla_"+str(nomPestana)].item(i,j).setTextAlignment(Qt.AlignCenter)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para darle alineación a la derecha a los datos
    def estiloDerecha(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        globals()["tabla_"+str(nomPestana)].item(i, j).setTextAlignment(Qt.AlignRight)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para darle alineación a la izquierda a los datos
    def estiloIzquierda(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        globals()["tabla_"+str(nomPestana)].item(i, j).setTextAlignment(Qt.AlignLeft)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para poner datos en negrilla
    def estiloNegrilla(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setBold(True)        
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para quitarle a los datos la negrilla
    def quitarEstiloNegrilla(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setBold(False)        
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para poner cursiva los datos
    def estiloCursiva(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setItalic(True)        
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')
    
    #Función para quitarle lo cursiva a los datos
    def quitarEstiloCursiva(self):
        global rangoSeleccionado

        indice = self.tw_Pestanas.currentIndex()

        nomPestana = self.tw_Pestanas.tabText(indice)

        if nomPestana != 'PyStruct':
            
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0
           
            if rangoSeleccionado != []:

                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setItalic(False)        
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para subrayar los datos
    def estiloSubrayar(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setUnderline(True)  
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')
        
    #Función para quitar subrayado a los datos
    def quitarEstiloSubrayar(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()
                        font.setItalic(False)        
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')
 
    #Función para dar color a los datos
    def estiloPaletaColor(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                
                #Seleccionar un color
                color = QColorDialog.getColor()

                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        globals()["tabla_"+str(nomPestana)].item(i, j).setForeground(QColor(color.name()))
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para dar tipo de fuente a los datos
    def estiloTipoFuente(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Capturar el tipo de fuente seleccionado por el usuario
        fuente = self.cb_TipoLetra.currentText()

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()                        
                        font.setFamily(fuente)                         
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos') 

    #Función para dar tamaño a los datos
    def estiloTamano(self):
        #Manejo de variables globales
        global rangoSeleccionado

        #Capturar el indice de la pestaña donde el usuario se encuentra posicionado
        indice = self.tw_Pestanas.currentIndex()

        #Capturar el nombre de la pestaña perteneciente a un indice especificado
        nomPestana = self.tw_Pestanas.tabText(indice)

        #Capturar el tamaño para los datos
        tamano = int (self.cb_TamanoLetra.currentText())

        #Verificar en que pestaña se encueentra el usuario
        if nomPestana != 'PyStruct':
            #Capturar el rango de celdas seleccionadas por el usuario
            rangoSeleccionado = globals()["tabla_"+str(nomPestana)].selectedRanges()

            #Crear variables para mínimos y máximos del rango seleccionado
            minrow = 0; maxrow = 0; mincol = 0; maxcol = 0

            #Validar si el usuario si ha seleccionado datos de la matriz
            if rangoSeleccionado != []:
                #Ciclo for para conseguir los mínimos y máximos del rango seleccionado
                for ir in rangoSeleccionado:
                    mincol = ir.leftColumn()
                    maxcol = ir.rightColumn()
                    minrow = ir.topRow()
                    maxrow = ir.bottomRow() 
                
                #Ciclo for para dar estilo al rango seleccionado por el usuario
                for i in range(minrow,maxrow+1):
                    for j in range(mincol,maxcol+1):
                        font = globals()["tabla_"+str(nomPestana)].item(i, j).font()                        
                        font.setPointSize(tamano)                         
                        globals()["tabla_"+str(nomPestana)].item(i, j).setFont(font)
            else:
                #Mensaje de error, en caso de no seleccionar celdas
                mensajes.mensajeError('Error de estilos','No se cuenta con datos seleccionados para aplicar el estilo') 
        else:
            #Mensaje de error, en el caso de querer dar estilo a la pestaña PyStruct
            mensajes.mensajeError('Error de estilos', 'A la pestaña PyStruct no se le puede aplicar estilos')

    #Función para capturar evento close de la ventana principal
    def closeEvent(self, QCloseEvent):
        #Cerrar toda la herramienta
        sys.exit()

    #Función para cerrar sesiones de usuario
    def cerrarSesiones(self):
        #Crear conexión a BD
        self.datos = conexionDB.Conexion()
        #Llamar funcion para cerrar sesion
        self.datos.registarCerrarSesion()
        #Cerrar solo la ventana principal
        self.hide()
