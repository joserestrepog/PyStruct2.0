# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficaDispersion.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class f_GraficaDispersion(object):
    def setupUi(self, f_GraficaDispersion):
        if not f_GraficaDispersion.objectName():
            f_GraficaDispersion.setObjectName(u"f_GraficaDispersion")
        f_GraficaDispersion.resize(782, 560)
        f_GraficaDispersion.setMaximumSize(QSize(782, 560))
        icon = QIcon()
        icon.addFile(u"./assets/iconos/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        f_GraficaDispersion.setWindowIcon(icon)
        f_GraficaDispersion.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.verticalLayout = QVBoxLayout(f_GraficaDispersion)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_GraficaDispersion = QFrame(f_GraficaDispersion)
        self.fr_GraficaDispersion.setObjectName(u"fr_GraficaDispersion")
        self.fr_GraficaDispersion.setMinimumSize(QSize(782, 560))
        self.fr_GraficaDispersion.setMaximumSize(QSize(782, 560))
        self.fr_GraficaDispersion.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"\n"
"")
        self.fr_GraficaDispersion.setFrameShape(QFrame.StyledPanel)
        self.fr_GraficaDispersion.setFrameShadow(QFrame.Raised)
        self.fr_GraficaDispersion.setLineWidth(0)
        self.l_FigLogo = QLabel(self.fr_GraficaDispersion)
        self.l_FigLogo.setObjectName(u"l_FigLogo")
        self.l_FigLogo.setGeometry(QRect(30, 20, 41, 41))
        self.l_FigLogo.setStyleSheet(u"\n"
"\n"
"QLabel{\n"
"	border: 0px;\n"
"}")
        self.l_FigLogo.setPixmap(QPixmap(u"./assets/iconos/Logo.png"))
        self.l_FigLogo.setScaledContents(True)
        self.l_Titulo = QLabel(self.fr_GraficaDispersion)
        self.l_Titulo.setObjectName(u"l_Titulo")
        self.l_Titulo.setGeometry(QRect(70, 20, 211, 41))
        self.l_Titulo.setStyleSheet(u"QLabel{\n"
"	font: 75 12pt \"MS Shell Dig 2\" #0099CC;\n"
"	color: #0099CC;\n"
"	border: 0px;\n"
"}")
        self.fr_TipoGrafica = QFrame(self.fr_GraficaDispersion)
        self.fr_TipoGrafica.setObjectName(u"fr_TipoGrafica")
        self.fr_TipoGrafica.setGeometry(QRect(20, 90, 741, 371))
        self.fr_TipoGrafica.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid #a8a8a8;\n"
"}")
        self.fr_TipoGrafica.setFrameShape(QFrame.StyledPanel)
        self.fr_TipoGrafica.setFrameShadow(QFrame.Raised)
        self.L_Fig3D = QLabel(self.fr_TipoGrafica)
        self.L_Fig3D.setObjectName(u"L_Fig3D")
        self.L_Fig3D.setGeometry(QRect(400, 110, 301, 211))
        self.L_Fig3D.setStyleSheet(u"QLabel{	\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.L_Fig3D.setPixmap(QPixmap(u"./assets/iconos/gDispersion3D.png"))
        self.L_Fig3D.setScaledContents(True)
        self.l_Fig2D = QLabel(self.fr_TipoGrafica)
        self.l_Fig2D.setObjectName(u"l_Fig2D")
        self.l_Fig2D.setGeometry(QRect(40, 110, 301, 211))
        self.l_Fig2D.setStyleSheet(u"QLabel{\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.l_Fig2D.setPixmap(QPixmap(u"./assets/iconos/gDispesion2D.png"))
        self.l_Fig2D.setScaledContents(True)
        self.l_TipoGrafica = QLabel(self.fr_TipoGrafica)
        self.l_TipoGrafica.setObjectName(u"l_TipoGrafica")
        self.l_TipoGrafica.setGeometry(QRect(290, 10, 151, 31))
        self.l_TipoGrafica.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(225, 225, 225);\n"
"	font: 75 13pt \"MS Shell Dig 2\" #0099CC;\n"
"	color: #000000;\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.l_TipoGrafica.setAlignment(Qt.AlignCenter)
        self.rb_2D = QRadioButton(self.fr_TipoGrafica)
        self.rb_2D.setObjectName(u"rb_2D")
        self.rb_2D.setGeometry(QRect(150, 70, 71, 31))
        self.rb_2D.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"MS Shell Dig 2\";\n"
"	color: #000000;\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.rb_3D = QRadioButton(self.fr_TipoGrafica)
        self.rb_3D.setObjectName(u"rb_3D")
        self.rb_3D.setGeometry(QRect(520, 70, 71, 31))
        self.rb_3D.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"MS Shell Dig 2\";\n"
"	color: #000000;\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.b_Aceptar = QPushButton(self.fr_GraficaDispersion)
        self.b_Aceptar.setObjectName(u"b_Aceptar")
        self.b_Aceptar.setGeometry(QRect(540, 490, 101, 41))
        font = QFont()
        font.setPointSize(10)
        self.b_Aceptar.setFont(font)
        self.b_Cancelar = QPushButton(self.fr_GraficaDispersion)
        self.b_Cancelar.setObjectName(u"b_Cancelar")
        self.b_Cancelar.setGeometry(QRect(650, 490, 101, 41))
        self.b_Cancelar.setFont(font)
        self.cb_ColorParticulas = QComboBox(self.fr_GraficaDispersion)
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.setObjectName(u"cb_ColorParticulas")
        self.cb_ColorParticulas.setGeometry(QRect(80, 510, 91, 22))
        self.cb_TamanoParticulas = QComboBox(self.fr_GraficaDispersion)
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.addItem("")
        self.cb_TamanoParticulas.setObjectName(u"cb_TamanoParticulas")
        self.cb_TamanoParticulas.setGeometry(QRect(330, 510, 51, 22))
        self.l_color = QLabel(self.fr_GraficaDispersion)
        self.l_color.setObjectName(u"l_color")
        self.l_color.setGeometry(QRect(30, 510, 51, 21))
        self.l_color.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")
        self.l_tamParticulas = QLabel(self.fr_GraficaDispersion)
        self.l_tamParticulas.setObjectName(u"l_tamParticulas")
        self.l_tamParticulas.setGeometry(QRect(190, 510, 141, 21))
        self.l_tamParticulas.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")
        self.frame = QFrame(self.fr_GraficaDispersion)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 480, 381, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.fr_GraficaDispersion)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 470, 121, 21))
        self.label.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")
        self.frame.raise_()
        self.l_FigLogo.raise_()
        self.l_Titulo.raise_()
        self.fr_TipoGrafica.raise_()
        self.b_Aceptar.raise_()
        self.b_Cancelar.raise_()
        self.cb_ColorParticulas.raise_()
        self.cb_TamanoParticulas.raise_()
        self.l_color.raise_()
        self.l_tamParticulas.raise_()
        self.label.raise_()

        self.verticalLayout.addWidget(self.fr_GraficaDispersion)


        self.retranslateUi(f_GraficaDispersion)

        QMetaObject.connectSlotsByName(f_GraficaDispersion)
    # setupUi

    def retranslateUi(self, f_GraficaDispersion):
        f_GraficaDispersion.setWindowTitle(QCoreApplication.translate("f_GraficaDispersion", u"Gr\u00e1ficos", None))
        self.l_FigLogo.setText("")
        self.l_Titulo.setText(QCoreApplication.translate("f_GraficaDispersion", u"Gr\u00e1ficas de Dispersi\u00f3n", None))
        self.L_Fig3D.setText("")
        self.l_Fig2D.setText("")
        self.l_TipoGrafica.setText(QCoreApplication.translate("f_GraficaDispersion", u"Dispersi\u00f3n", None))
        self.rb_2D.setText(QCoreApplication.translate("f_GraficaDispersion", u"2D", None))
        self.rb_3D.setText(QCoreApplication.translate("f_GraficaDispersion", u"3D", None))
        self.b_Aceptar.setText(QCoreApplication.translate("f_GraficaDispersion", u"Aceptar", None))
        self.b_Cancelar.setText(QCoreApplication.translate("f_GraficaDispersion", u"Cancelar", None))
        self.cb_ColorParticulas.setItemText(0, QCoreApplication.translate("f_GraficaDispersion", u"Black", None))
        self.cb_ColorParticulas.setItemText(1, QCoreApplication.translate("f_GraficaDispersion", u"Blue", None))
        self.cb_ColorParticulas.setItemText(2, QCoreApplication.translate("f_GraficaDispersion", u"Green", None))
        self.cb_ColorParticulas.setItemText(3, QCoreApplication.translate("f_GraficaDispersion", u"Magenta", None))
        self.cb_ColorParticulas.setItemText(4, QCoreApplication.translate("f_GraficaDispersion", u"Orange", None))
        self.cb_ColorParticulas.setItemText(5, QCoreApplication.translate("f_GraficaDispersion", u"Pink", None))
        self.cb_ColorParticulas.setItemText(6, QCoreApplication.translate("f_GraficaDispersion", u"Red", None))
        self.cb_ColorParticulas.setItemText(7, QCoreApplication.translate("f_GraficaDispersion", u"Yellow", None))

        self.cb_TamanoParticulas.setItemText(0, QCoreApplication.translate("f_GraficaDispersion", u"2", None))
        self.cb_TamanoParticulas.setItemText(1, QCoreApplication.translate("f_GraficaDispersion", u"3", None))
        self.cb_TamanoParticulas.setItemText(2, QCoreApplication.translate("f_GraficaDispersion", u"5", None))
        self.cb_TamanoParticulas.setItemText(3, QCoreApplication.translate("f_GraficaDispersion", u"8", None))
        self.cb_TamanoParticulas.setItemText(4, QCoreApplication.translate("f_GraficaDispersion", u"10", None))
        self.cb_TamanoParticulas.setItemText(5, QCoreApplication.translate("f_GraficaDispersion", u"12", None))
        self.cb_TamanoParticulas.setItemText(6, QCoreApplication.translate("f_GraficaDispersion", u"14", None))
        self.cb_TamanoParticulas.setItemText(7, QCoreApplication.translate("f_GraficaDispersion", u"16", None))
        self.cb_TamanoParticulas.setItemText(8, QCoreApplication.translate("f_GraficaDispersion", u"18", None))
        self.cb_TamanoParticulas.setItemText(9, QCoreApplication.translate("f_GraficaDispersion", u"20", None))
        self.cb_TamanoParticulas.setItemText(10, QCoreApplication.translate("f_GraficaDispersion", u"24", None))

        self.l_color.setText(QCoreApplication.translate("f_GraficaDispersion", u"Color:", None))
        self.l_tamParticulas.setText(QCoreApplication.translate("f_GraficaDispersion", u"Tama\u00f1o Particula:", None))
        self.label.setText(QCoreApplication.translate("f_GraficaDispersion", u"Estilo de gr\u00e1fica", None))
    # retranslateUi

