from PySide2.QtWidgets import QMessageBox
from PySide2.QtGui import QIcon

def mensajeError(titulo, texto):
    icon = './assets/iconos/Error.png'
    msg_box = QMessageBox()
    msg_box.setWindowTitle(titulo)
    msg_box.setText(texto)
    msg_box.setIconPixmap(icon)
    icon_logo = './assets/iconos/logo.png'
    q_icon = QIcon(icon_logo)
    msg_box.setWindowIcon(q_icon)
    msg_box.exec_()

def mensajeAlerta(titulo, texto):
    icon = './assets/iconos/Exclamacion.png'
    msg_box = QMessageBox()
    msg_box.setWindowTitle(titulo)
    msg_box.setText(texto)
    msg_box.setIconPixmap(icon)
    icon_logo = './assets/iconos/logo.png'
    q_icon = QIcon(icon_logo)
    msg_box.setWindowIcon(q_icon)
    msg_box.exec_()

def mensajeInfo(titulo, texto):
    icon = './assets/iconos/info.png'
    msg_box = QMessageBox()
    msg_box.setWindowTitle(titulo)
    msg_box.setText(texto)
    msg_box.setIconPixmap(icon)
    icon_logo = './assets/iconos/logo.png'
    q_icon = QIcon(icon_logo)
    msg_box.setWindowIcon(q_icon)
    msg_box.exec_()
