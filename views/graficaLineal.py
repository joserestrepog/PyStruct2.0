# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'graficaLineal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class f_GraficaLineas(object):
    def setupUi(self, f_GraficaLineas):
        if not f_GraficaLineas.objectName():
            f_GraficaLineas.setObjectName(u"f_GraficaLineas")
        f_GraficaLineas.resize(782, 560)
        f_GraficaLineas.setMaximumSize(QSize(782, 560))
        icon = QIcon()
        icon.addFile(u"./assets/iconos/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        f_GraficaLineas.setWindowIcon(icon)
        f_GraficaLineas.setStyleSheet(u"QFrame{\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.verticalLayout = QVBoxLayout(f_GraficaLineas)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_GraficaLineas = QFrame(f_GraficaLineas)
        self.fr_GraficaLineas.setObjectName(u"fr_GraficaLineas")
        self.fr_GraficaLineas.setMinimumSize(QSize(782, 560))
        self.fr_GraficaLineas.setMaximumSize(QSize(782, 560))
        self.fr_GraficaLineas.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"\n"
"")
        self.fr_GraficaLineas.setFrameShape(QFrame.StyledPanel)
        self.fr_GraficaLineas.setFrameShadow(QFrame.Raised)
        self.fr_GraficaLineas.setLineWidth(0)
        self.l_FigLogo = QLabel(self.fr_GraficaLineas)
        self.l_FigLogo.setObjectName(u"l_FigLogo")
        self.l_FigLogo.setGeometry(QRect(30, 20, 41, 41))
        self.l_FigLogo.setStyleSheet(u"QLabel{\n"
"	border: 0px;\n"
"}")
        self.l_FigLogo.setPixmap(QPixmap(u"./assets/iconos/Logo.png"))
        self.l_FigLogo.setScaledContents(True)
        self.l_Titulo = QLabel(self.fr_GraficaLineas)
        self.l_Titulo.setObjectName(u"l_Titulo")
        self.l_Titulo.setGeometry(QRect(70, 20, 171, 41))
        self.l_Titulo.setStyleSheet(u"QLabel{\n"
"	font: 75 12pt \"MS Shell Dig 2\" #0099CC;\n"
"	color: #0099CC;\n"
"	border: 0px;\n"
"}")
        self.fr_TipoGrafica = QFrame(self.fr_GraficaLineas)
        self.fr_TipoGrafica.setObjectName(u"fr_TipoGrafica")
        self.fr_TipoGrafica.setGeometry(QRect(20, 90, 741, 371))
        self.fr_TipoGrafica.setStyleSheet(u"QFrame{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 2px solid #a8a8a8;\n"
"}")
        self.fr_TipoGrafica.setFrameShape(QFrame.StyledPanel)
        self.fr_TipoGrafica.setFrameShadow(QFrame.Raised)
        self.l_Fig3D = QLabel(self.fr_TipoGrafica)
        self.l_Fig3D.setObjectName(u"l_Fig3D")
        self.l_Fig3D.setGeometry(QRect(400, 110, 301, 211))
        self.l_Fig3D.setStyleSheet(u"QLabel{	\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.l_Fig3D.setPixmap(QPixmap(u"./assets/iconos/gLineal3D.png"))
        self.l_Fig3D.setScaledContents(True)
        self.l_Fig2D = QLabel(self.fr_TipoGrafica)
        self.l_Fig2D.setObjectName(u"l_Fig2D")
        self.l_Fig2D.setGeometry(QRect(40, 110, 301, 211))
        self.l_Fig2D.setStyleSheet(u"QLabel{\n"
"	border: 2px solid #0099CC;\n"
"}")
        self.l_Fig2D.setPixmap(QPixmap(u"./assets/iconos/gLineal2D.png"))
        self.l_Fig2D.setScaledContents(True)
        self.l_TipoGrafica = QLabel(self.fr_TipoGrafica)
        self.l_TipoGrafica.setObjectName(u"l_TipoGrafica")
        self.l_TipoGrafica.setGeometry(QRect(300, 10, 141, 31))
        self.l_TipoGrafica.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(225, 225, 225);\n"
"	font: 75 14pt \"MS Shell Dig 2\" #0099CC;\n"
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
        self.b_Aceptar = QPushButton(self.fr_GraficaLineas)
        self.b_Aceptar.setObjectName(u"b_Aceptar")
        self.b_Aceptar.setGeometry(QRect(540, 490, 101, 41))
        font = QFont()
        font.setPointSize(10)
        self.b_Aceptar.setFont(font)
        self.b_Cancelar = QPushButton(self.fr_GraficaLineas)
        self.b_Cancelar.setObjectName(u"b_Cancelar")
        self.b_Cancelar.setGeometry(QRect(650, 490, 101, 41))
        self.b_Cancelar.setFont(font)
        self.frame = QFrame(self.fr_GraficaLineas)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 480, 381, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.cb_ColorParticulas = QComboBox(self.frame)
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.addItem("")
        self.cb_ColorParticulas.setObjectName(u"cb_ColorParticulas")
        self.cb_ColorParticulas.setGeometry(QRect(70, 30, 91, 22))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 51, 16))
        self.label.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")
        self.label_2 = QLabel(self.fr_GraficaLineas)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 470, 121, 21))
        self.label_2.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")

        self.verticalLayout.addWidget(self.fr_GraficaLineas)


        self.retranslateUi(f_GraficaLineas)

        QMetaObject.connectSlotsByName(f_GraficaLineas)
    # setupUi

    def retranslateUi(self, f_GraficaLineas):
        f_GraficaLineas.setWindowTitle(QCoreApplication.translate("f_GraficaLineas", u"Gr\u00e1ficos", None))
        self.l_FigLogo.setText("")
        self.l_Titulo.setText(QCoreApplication.translate("f_GraficaLineas", u"Gr\u00e1ficas de L\u00edneas", None))
        self.l_Fig3D.setText("")
        self.l_Fig2D.setText("")
        self.l_TipoGrafica.setText(QCoreApplication.translate("f_GraficaLineas", u"L\u00edneas", None))
        self.rb_2D.setText(QCoreApplication.translate("f_GraficaLineas", u"2D", None))
        self.rb_3D.setText(QCoreApplication.translate("f_GraficaLineas", u"3D", None))
        self.b_Aceptar.setText(QCoreApplication.translate("f_GraficaLineas", u"Aceptar", None))
        self.b_Cancelar.setText(QCoreApplication.translate("f_GraficaLineas", u"Cancelar", None))
        self.cb_ColorParticulas.setItemText(0, QCoreApplication.translate("f_GraficaLineas", u"Black", None))
        self.cb_ColorParticulas.setItemText(1, QCoreApplication.translate("f_GraficaLineas", u"Blue", None))
        self.cb_ColorParticulas.setItemText(2, QCoreApplication.translate("f_GraficaLineas", u"Green", None))
        self.cb_ColorParticulas.setItemText(3, QCoreApplication.translate("f_GraficaLineas", u"Magenta", None))
        self.cb_ColorParticulas.setItemText(4, QCoreApplication.translate("f_GraficaLineas", u"Orange", None))
        self.cb_ColorParticulas.setItemText(5, QCoreApplication.translate("f_GraficaLineas", u"Pink", None))
        self.cb_ColorParticulas.setItemText(6, QCoreApplication.translate("f_GraficaLineas", u"Red", None))
        self.cb_ColorParticulas.setItemText(7, QCoreApplication.translate("f_GraficaLineas", u"Yellow", None))

        self.label.setText(QCoreApplication.translate("f_GraficaLineas", u"Color:", None))
        self.label_2.setText(QCoreApplication.translate("f_GraficaLineas", u"Estilo de gr\u00e1fica", None))
    # retranslateUi

