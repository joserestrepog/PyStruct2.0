# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicioSesion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class f_InicioSesion(object):
    def setupUi(self, f_InicioSesion):
        if not f_InicioSesion.objectName():
            f_InicioSesion.setObjectName(u"f_InicioSesion")
        f_InicioSesion.resize(503, 637)
        f_InicioSesion.setMinimumSize(QSize(503, 637))
        f_InicioSesion.setMaximumSize(QSize(503, 637))
        icon = QIcon()
        icon.addFile(u"./assets/iconos/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        f_InicioSesion.setWindowIcon(icon)
        f_InicioSesion.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.532, y1:1, x2:0.561975, y2:0, stop:0 rgba(255, 255, 169, 255), stop:0.890547 rgba(0, 180, 215, 255));")
        self.l_FigUsuario = QLabel(f_InicioSesion)
        self.l_FigUsuario.setObjectName(u"l_FigUsuario")
        self.l_FigUsuario.setGeometry(QRect(160, 50, 181, 161))
        self.l_FigUsuario.setStyleSheet(u"/*image: url(:/iconos/inicioSesion2.png);*/\n"
"background-color: rgb(0);")
        self.l_FigUsuario.setPixmap(QPixmap(u"./assets/iconos/inicioSesion2.png"))
        self.l_FigUsuario.setScaledContents(False)
        self.l_Usuario = QLabel(f_InicioSesion)
        self.l_Usuario.setObjectName(u"l_Usuario")
        self.l_Usuario.setGeometry(QRect(170, 220, 171, 31))
        self.l_Usuario.setStyleSheet(u"background-color: rgba(0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
" ")
        self.l_Usuario.setAlignment(Qt.AlignCenter)
        self.l_Contrasena = QLabel(f_InicioSesion)
        self.l_Contrasena.setObjectName(u"l_Contrasena")
        self.l_Contrasena.setGeometry(QRect(170, 320, 171, 31))
        self.l_Contrasena.setStyleSheet(u"background-color: rgba(0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
" ")
        self.l_Contrasena.setAlignment(Qt.AlignCenter)
        self.correo = QLineEdit(f_InicioSesion)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(110, 260, 291, 31))
        self.correo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.correo.setAlignment(Qt.AlignCenter)
        self.contrasena = QLineEdit(f_InicioSesion)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setGeometry(QRect(110, 360, 291, 31))
        self.contrasena.setEchoMode(QLineEdit.Password)        
        self.contrasena.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.contrasena.setAlignment(Qt.AlignCenter)
        self.b_IniciarSesion = QPushButton(f_InicioSesion)
        self.b_IniciarSesion.setObjectName(u"b_IniciarSesion")
        self.b_IniciarSesion.setGeometry(QRect(170, 430, 171, 31))
        self.b_IniciarSesion.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_IniciarSesion.setStyleSheet(u"QPushButton{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(0, 180, 215);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/iconos/inicioSesion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_IniciarSesion.setIcon(icon1)
        self.b_IniciarSesion.setIconSize(QSize(20, 20))
        self.b_Registrar = QPushButton(f_InicioSesion)
        self.b_Registrar.setObjectName(u"b_Registrar")
        self.b_Registrar.setGeometry(QRect(180, 500, 151, 31))
        self.b_Registrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_Registrar.setStyleSheet(u"QPushButton{	\n"
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
        icon2.addFile(u"./assets/iconos/registrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_Registrar.setIcon(icon2)
        self.b_Registrar.setIconSize(QSize(20, 20))
        self.progreso = QProgressBar(f_InicioSesion)
        self.progreso.setObjectName(u"progreso")
        self.progreso.setGeometry(QRect(60, 560, 391, 16))
        self.progreso.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.437045, x2:0.995, y2:0.477273, stop:0 rgba(255, 255, 169, 255), stop:0.890547 rgba(0, 180, 215, 255));")
        self.progreso.setValue(0)
        self.progreso.setTextVisible(False)
        self.l_Cargando = QLabel(f_InicioSesion)
        self.l_Cargando.setObjectName(u"l_Cargando")
        self.l_Cargando.setGeometry(QRect(220, 580, 71, 16))
        self.l_Cargando.setStyleSheet(u"background-color: rgb(0);")

        self.retranslateUi(f_InicioSesion)

        QMetaObject.connectSlotsByName(f_InicioSesion)
    # setupUi

    def retranslateUi(self, f_InicioSesion):
        f_InicioSesion.setWindowTitle(QCoreApplication.translate("f_InicioSesion", u"Inicio de Sesi\u00f3n - PyStruct", None))
        self.l_FigUsuario.setText("")
        self.l_Usuario.setText(QCoreApplication.translate("f_InicioSesion", u"Usuario", None))
        self.l_Contrasena.setText(QCoreApplication.translate("f_InicioSesion", u"Contrase\u00f1a", None))
        self.correo.setText("")
        self.correo.setPlaceholderText(QCoreApplication.translate("f_InicioSesion", u"Ingrese su correo", None))
        self.contrasena.setText("")
        self.contrasena.setPlaceholderText(QCoreApplication.translate("f_InicioSesion", u"Ingrese su contrase\u00f1a", None))
        self.b_IniciarSesion.setText(QCoreApplication.translate("f_InicioSesion", u"Iniciar Sesi\u00f3n", None))
        self.b_Registrar.setText(QCoreApplication.translate("f_InicioSesion", u"Registrarse", None))
        self.l_Cargando.setText("")
    # retranslateUi

