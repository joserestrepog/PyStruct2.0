# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predictor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class f_Predictor(object):
    def setupUi(self, f_Predictor):
        if not f_Predictor.objectName():
            f_Predictor.setObjectName(u"f_Predictor")
        f_Predictor.resize(582, 678)
        f_Predictor.setMinimumSize(QSize(582, 678))
        f_Predictor.setMaximumSize(QSize(582, 678))
        f_Predictor.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border: 2px solid #0099CC;")
        self.b_Cancelar = QPushButton(f_Predictor)
        self.b_Cancelar.setObjectName(u"b_Cancelar")
        self.b_Cancelar.setGeometry(QRect(330, 610, 141, 31))
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
        icon = QIcon()
        icon.addFile(u"../assets/iconos/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_Cancelar.setIcon(icon)
        self.b_Cancelar.setIconSize(QSize(20, 20))
        self.ancho = QLineEdit(f_Predictor)
        self.ancho.setObjectName(u"ancho")
        self.ancho.setGeometry(QRect(270, 309, 261, 31))
        self.ancho.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ancho.setAlignment(Qt.AlignCenter)
        self.text_Descripcion = QTextBrowser(f_Predictor)
        self.text_Descripcion.setObjectName(u"text_Descripcion")
        self.text_Descripcion.setGeometry(QRect(260, 39, 271, 181))
        self.text_Descripcion.setStyleSheet(u"QTextBrowser{\n"
"	border: 0px;\n"
"	text-align: justify;\n"
"}")
        self.l_Temperatura = QLabel(f_Predictor)
        self.l_Temperatura.setObjectName(u"l_Temperatura")
        self.l_Temperatura.setGeometry(QRect(50, 369, 201, 31))
        self.l_Temperatura.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
" ")
        self.l_Temperatura.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.l_CantParticulas = QLabel(f_Predictor)
        self.l_CantParticulas.setObjectName(u"l_CantParticulas")
        self.l_CantParticulas.setGeometry(QRect(50, 429, 181, 31))
        self.l_CantParticulas.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
" ")
        self.l_CantParticulas.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cantParticulas = QLineEdit(f_Predictor)
        self.cantParticulas.setObjectName(u"cantParticulas")
        self.cantParticulas.setGeometry(QRect(270, 429, 261, 31))
        self.cantParticulas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.cantParticulas.setAlignment(Qt.AlignCenter)
        self.b_Predecir = QPushButton(f_Predictor)
        self.b_Predecir.setObjectName(u"b_Predecir")
        self.b_Predecir.setGeometry(QRect(330, 530, 141, 31))
        self.b_Predecir.setCursor(QCursor(Qt.PointingHandCursor))
        self.b_Predecir.setStyleSheet(u"QPushButton{	\n"
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
        icon1.addFile(u"../assets/iconos/registrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.b_Predecir.setIcon(icon1)
        self.b_Predecir.setIconSize(QSize(20, 20))
        self.l_Figura = QLabel(f_Predictor)
        self.l_Figura.setObjectName(u"l_Figura")
        self.l_Figura.setGeometry(QRect(70, 29, 171, 151))
        self.l_Figura.setStyleSheet(u"border: 0px;")
        self.l_Figura.setPixmap(QPixmap(u"../assets/iconos/ventanaPredictor.png"))
        self.l_Figura.setScaledContents(True)
        self.l_AnchoCaja = QLabel(f_Predictor)
        self.l_AnchoCaja.setObjectName(u"l_AnchoCaja")
        self.l_AnchoCaja.setGeometry(QRect(50, 309, 191, 31))
        self.l_AnchoCaja.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
" ")
        self.l_AnchoCaja.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.temperatura = QLineEdit(f_Predictor)
        self.temperatura.setObjectName(u"temperatura")
        self.temperatura.setGeometry(QRect(270, 369, 261, 31))
        self.temperatura.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.temperatura.setAlignment(Qt.AlignCenter)
        self.l_Material = QLabel(f_Predictor)
        self.l_Material.setObjectName(u"l_Material")
        self.l_Material.setGeometry(QRect(50, 249, 141, 31))
        self.l_Material.setStyleSheet(u"background-color: rgba(0, 0, 0, 0%);\n"
"font: 75 11pt \"MS Shell Dlg 2\";\n"
"border: 0px;\n"
" ")
        self.l_Material.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cb_Material = QComboBox(f_Predictor)
        self.cb_Material.addItem("")
        self.cb_Material.addItem("")
        self.cb_Material.addItem("")
        self.cb_Material.setObjectName(u"cb_Material")
        self.cb_Material.setGeometry(QRect(270, 250, 261, 31))
        self.frame = QFrame(f_Predictor)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 510, 221, 131))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.l_color = QLabel(self.frame)
        self.l_color.setObjectName(u"l_color")
        self.l_color.setGeometry(QRect(40, 30, 41, 21))
        self.l_color.setStyleSheet(u"border: 0px;\n"
"font: 75 9pt \"MS Shell Dig 2\" #0099CC;")
        self.l_tamParticulas = QLabel(self.frame)
        self.l_tamParticulas.setObjectName(u"l_tamParticulas")
        self.l_tamParticulas.setGeometry(QRect(40, 70, 61, 21))
        self.l_tamParticulas.setStyleSheet(u"border: 0px;\n"
"font: 75 9pt \"MS Shell Dig 2\" #0099CC;")
        self.cb_TamanoParticulas = QComboBox(self.frame)
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
        self.cb_TamanoParticulas.setGeometry(QRect(110, 80, 71, 22))
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
        self.cb_ColorParticulas.setGeometry(QRect(110, 30, 71, 22))
        self.l_tamParticulas_2 = QLabel(self.frame)
        self.l_tamParticulas_2.setObjectName(u"l_tamParticulas_2")
        self.l_tamParticulas_2.setGeometry(QRect(40, 90, 61, 21))
        self.l_tamParticulas_2.setStyleSheet(u"border: 0px;\n"
"font: 75 9pt \"MS Shell Dig 2\" #0099CC;")
        self.l_color_2 = QLabel(f_Predictor)
        self.l_color_2.setObjectName(u"l_color_2")
        self.l_color_2.setGeometry(QRect(70, 500, 161, 21))
        self.l_color_2.setStyleSheet(u"border: 0px;\n"
"font: 75 10pt \"MS Shell Dig 2\" #0099CC;")
        self.l_Temperatura.raise_()
        self.b_Cancelar.raise_()
        self.ancho.raise_()
        self.text_Descripcion.raise_()
        self.l_CantParticulas.raise_()
        self.cantParticulas.raise_()
        self.b_Predecir.raise_()
        self.l_Figura.raise_()
        self.l_AnchoCaja.raise_()
        self.temperatura.raise_()
        self.l_Material.raise_()
        self.cb_Material.raise_()
        self.frame.raise_()
        self.l_color_2.raise_()

        self.retranslateUi(f_Predictor)

        QMetaObject.connectSlotsByName(f_Predictor)
    # setupUi

    def retranslateUi(self, f_Predictor):
        f_Predictor.setWindowTitle(QCoreApplication.translate("f_Predictor", u"Predictor", None))
        self.b_Cancelar.setText(QCoreApplication.translate("f_Predictor", u"Cancelar", None))
        self.ancho.setText("")
        self.ancho.setPlaceholderText(QCoreApplication.translate("f_Predictor", u"Ingrese el ancho", None))
        self.text_Descripcion.setHtml(QCoreApplication.translate("f_Predictor", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 3'; font-size:10pt;\">Actualmente la versi\u00f3n 2.0 de PyStruct cuenta con la predicci\u00f3n de la estructura cristalina del Hierro y del N\u00edquel. Adem\u00e1s, para hacer la predicci\u00f3n se hace uso de </span><span style=\" font-family:'MS Shell Dlg 3'; font-size:10pt; font-style:italic;\">&quot;Arboles de Regresi\u00f3n&quot;</span><span style=\" font-family:'MS Shell Dlg 3'; font-size:10pt;\"> como modelo de machine learning.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; ma"
                        "rgin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 3'; font-size:10pt;\"><br /></p></body></html>", None))
        self.l_Temperatura.setText(QCoreApplication.translate("f_Predictor", u"Temperatura Final en K:", None))
        self.l_CantParticulas.setText(QCoreApplication.translate("f_Predictor", u"N\u00famero de Particulas:", None))
        self.cantParticulas.setText("")
        self.cantParticulas.setPlaceholderText(QCoreApplication.translate("f_Predictor", u"Ingrese Nro de particulas", None))
        self.b_Predecir.setText(QCoreApplication.translate("f_Predictor", u"Predecir", None))
        self.l_Figura.setText("")
        self.l_AnchoCaja.setText(QCoreApplication.translate("f_Predictor", u"Ancho de Caja en UPR:", None))
        self.temperatura.setText("")
        self.temperatura.setPlaceholderText(QCoreApplication.translate("f_Predictor", u"Ingrese temperatura", None))
        self.l_Material.setText(QCoreApplication.translate("f_Predictor", u"Material", None))
        self.cb_Material.setItemText(0, QCoreApplication.translate("f_Predictor", u"Seleccione el Material", None))
        self.cb_Material.setItemText(1, QCoreApplication.translate("f_Predictor", u"N\u00edquel", None))
        self.cb_Material.setItemText(2, QCoreApplication.translate("f_Predictor", u"Hierro", None))

        self.l_color.setText(QCoreApplication.translate("f_Predictor", u"Color:", None))
        self.l_tamParticulas.setText(QCoreApplication.translate("f_Predictor", u"Tama\u00f1o", None))
        self.cb_TamanoParticulas.setItemText(0, QCoreApplication.translate("f_Predictor", u"2", None))
        self.cb_TamanoParticulas.setItemText(1, QCoreApplication.translate("f_Predictor", u"3", None))
        self.cb_TamanoParticulas.setItemText(2, QCoreApplication.translate("f_Predictor", u"5", None))
        self.cb_TamanoParticulas.setItemText(3, QCoreApplication.translate("f_Predictor", u"8", None))
        self.cb_TamanoParticulas.setItemText(4, QCoreApplication.translate("f_Predictor", u"10", None))
        self.cb_TamanoParticulas.setItemText(5, QCoreApplication.translate("f_Predictor", u"12", None))
        self.cb_TamanoParticulas.setItemText(6, QCoreApplication.translate("f_Predictor", u"14", None))
        self.cb_TamanoParticulas.setItemText(7, QCoreApplication.translate("f_Predictor", u"16", None))
        self.cb_TamanoParticulas.setItemText(8, QCoreApplication.translate("f_Predictor", u"18", None))
        self.cb_TamanoParticulas.setItemText(9, QCoreApplication.translate("f_Predictor", u"20", None))
        self.cb_TamanoParticulas.setItemText(10, QCoreApplication.translate("f_Predictor", u"24", None))

        self.cb_ColorParticulas.setItemText(0, QCoreApplication.translate("f_Predictor", u"Black", None))
        self.cb_ColorParticulas.setItemText(1, QCoreApplication.translate("f_Predictor", u"Blue", None))
        self.cb_ColorParticulas.setItemText(2, QCoreApplication.translate("f_Predictor", u"Green", None))
        self.cb_ColorParticulas.setItemText(3, QCoreApplication.translate("f_Predictor", u"Magenta", None))
        self.cb_ColorParticulas.setItemText(4, QCoreApplication.translate("f_Predictor", u"Orange", None))
        self.cb_ColorParticulas.setItemText(5, QCoreApplication.translate("f_Predictor", u"Pink", None))
        self.cb_ColorParticulas.setItemText(6, QCoreApplication.translate("f_Predictor", u"Red", None))
        self.cb_ColorParticulas.setItemText(7, QCoreApplication.translate("f_Predictor", u"Yellow", None))

        self.l_tamParticulas_2.setText(QCoreApplication.translate("f_Predictor", u"Particula:", None))
        self.l_color_2.setText(QCoreApplication.translate("f_Predictor", u"Detalles de la Grafica", None))
    # retranslateUi

