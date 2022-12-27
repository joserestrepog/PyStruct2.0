# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class f_Registrarse(object):
    def setupUi(self, f_Registrarse):
        if not f_Registrarse.objectName():
            f_Registrarse.setObjectName(u"f_Registrarse")
        f_Registrarse.setEnabled(True)
        f_Registrarse.resize(463, 753)
        f_Registrarse.setMinimumSize(QSize(462, 667))
        icon = QIcon()
        icon.addFile(u"./assets/iconos/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        f_Registrarse.setWindowIcon(icon)
        f_Registrarse.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.532, y1:1, x2:0.561975, y2:0, stop:0 rgba(255, 255, 169, 255), stop:0.890547 rgba(0, 180, 215, 255));")
        self.l_FigRegistrarse = QLabel(f_Registrarse)
        self.l_FigRegistrarse.setObjectName(u"l_FigRegistrarse")
        self.l_FigRegistrarse.setGeometry(QRect(140, 20, 191, 181))
        self.l_FigRegistrarse.setStyleSheet(u"background-color: rgb(0);")
        self.l_FigRegistrarse.setPixmap(QPixmap(u"./assets/iconos/inicioSesion.png"))
        self.l_FigRegistrarse.setScaledContents(True)
        self.l_Registrarse = QLabel(f_Registrarse)
        self.l_Registrarse.setObjectName(u"l_Registrarse")
        self.l_Registrarse.setGeometry(QRect(150, 190, 171, 31))
        self.l_Registrarse.setStyleSheet(u"background-color: rgba(0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
" ")
        self.l_Registrarse.setAlignment(Qt.AlignCenter)
        self.nombre = QLineEdit(f_Registrarse)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(90, 250, 291, 31))
        self.nombre.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.nombre.setAlignment(Qt.AlignCenter)
        self.apellidos = QLineEdit(f_Registrarse)
        self.apellidos.setObjectName(u"apellidos")
        self.apellidos.setGeometry(QRect(90, 300, 291, 31))
        self.apellidos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.apellidos.setAlignment(Qt.AlignCenter)
        self.contrasena = QLineEdit(f_Registrarse)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setGeometry(QRect(90, 500, 291, 31))
        self.contrasena.setEchoMode(QLineEdit.Password)
        self.contrasena.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contrasena.setAlignment(Qt.AlignCenter)
        self.confirmarContrasena = QLineEdit(f_Registrarse)
        self.confirmarContrasena.setObjectName(u"confirmarContrasena")
        self.confirmarContrasena.setGeometry(QRect(90, 550, 291, 31))
        self.confirmarContrasena.setEchoMode(QLineEdit.Password)
        self.confirmarContrasena.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.confirmarContrasena.setAlignment(Qt.AlignCenter)
        self.b_Registrarse = QPushButton(f_Registrarse)
        self.b_Registrarse.setObjectName(u"b_Registrarse")
        self.b_Registrarse.setGeometry(QRect(70, 620, 151, 31))
        self.b_Registrarse.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_Registrarse.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(0, 180, 215);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/iconos/registrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_Registrarse.setIcon(icon1)
        self.b_Registrarse.setIconSize(QSize(20, 20))
        self.b_Cancelar = QPushButton(f_Registrarse)
        self.b_Cancelar.setObjectName(u"b_Cancelar")
        self.b_Cancelar.setGeometry(QRect(260, 620, 151, 31))
        self.b_Cancelar.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_Cancelar.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(0, 180, 215);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/iconos/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_Cancelar.setIcon(icon2)
        self.b_Cancelar.setIconSize(QSize(20, 20))
        self.licencia = QLineEdit(f_Registrarse)
        self.licencia.setObjectName(u"licencia")
        self.licencia.setGeometry(QRect(90, 450, 291, 31))
        self.licencia.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.licencia.setAlignment(Qt.AlignCenter)
        self.cb_Universidades = QComboBox(f_Registrarse)
        self.cb_Universidades.addItem("")
        self.cb_Universidades.setObjectName(u"cb_Universidades")
        self.cb_Universidades.setGeometry(QRect(90, 400, 291, 31))
        self.cb_Universidades.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(127, 127, 127);")
        self.l_Cargando = QLabel(f_Registrarse)
        self.l_Cargando.setObjectName(u"l_Cargando")
        self.l_Cargando.setGeometry(QRect(210, 700, 71, 20))
        self.l_Cargando.setStyleSheet(u"background-color: rgb(0);")
        self.progreso = QProgressBar(f_Registrarse)
        self.progreso.setObjectName(u"progreso")
        self.progreso.setGeometry(QRect(70, 684, 341, 16))
        self.progreso.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.437045, x2:0.995, y2:0.477273, stop:0 rgba(255, 255, 169, 255), stop:0.890547 rgba(0, 180, 215, 255));")
        self.progreso.setValue(0)
        self.progreso.setTextVisible(False)
        self.correo = QLineEdit(f_Registrarse)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(90, 350, 291, 31))
        self.correo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.correo.setAlignment(Qt.AlignCenter)

        self.retranslateUi(f_Registrarse)

        QMetaObject.connectSlotsByName(f_Registrarse)
    # setupUi

    def retranslateUi(self, f_Registrarse):
        f_Registrarse.setWindowTitle(QCoreApplication.translate("f_Registrarse", u"Registro Usuario", None))
        self.l_FigRegistrarse.setText("")
        self.l_Registrarse.setText(QCoreApplication.translate("f_Registrarse", u"Registrarse", None))
        self.nombre.setText("")
        self.nombre.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Nombre", None))
        self.apellidos.setText("")
        self.apellidos.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Apellidos", None))
        self.contrasena.setText("")
        self.contrasena.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Contrase\u00f1a", None))
        self.confirmarContrasena.setText("")
        self.confirmarContrasena.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Confirmar contrase\u00f1a", None))
        self.b_Registrarse.setText(QCoreApplication.translate("f_Registrarse", u"Registrarse", None))
        self.b_Cancelar.setText(QCoreApplication.translate("f_Registrarse", u"Cancelar", None))
        self.licencia.setText("")
        self.licencia.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Licencia", None))
        self.cb_Universidades.setItemText(0, QCoreApplication.translate("f_Registrarse", u"Universidad", None))

        self.l_Cargando.setText("")
        self.correo.setText("")
        self.correo.setPlaceholderText(QCoreApplication.translate("f_Registrarse", u"Correo", None))
    # retranslateUi

