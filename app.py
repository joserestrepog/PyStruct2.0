#Librerías necesarias para la ejecución de la herramienta
from PySide2.QtWidgets import QApplication
from controllers.inicioSesion import iniciarSesion

if __name__ == '__main__':
    app = QApplication() #Crear instancia de la librería QApplication
    window = iniciarSesion() #Crear instancia de la ventana InicioSesion de PyStruct
    window.show() #Hacer visible la interfaz gráfica de la ventana InicioSesion
    app.exec_() #Poner en ejecución la App