# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'licencia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import iconos_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(514, 243)
        Form.setMinimumSize(QSize(514, 243))
        Form.setMaximumSize(QSize(514, 243))
        icon = QIcon()
        icon.addFile(u":/iconos/Logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 11, 492, 221))
        self.frame.setMinimumSize(QSize(492, 221))
        self.frame.setStyleSheet(u"background-color: rgb(229, 229, 229);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(159, 70, 211, 21))
        self.label_6.setMinimumSize(QSize(211, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 70, 62, 21))
        self.label_3.setMinimumSize(QSize(62, 21))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 100, 65, 21))
        self.label_4.setMinimumSize(QSize(65, 21))
        self.label_4.setFont(font)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(162, 100, 134, 21))
        self.label_7.setMinimumSize(QSize(134, 21))
        self.label_7.setFont(font)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(90, 130, 86, 21))
        self.label_5.setMinimumSize(QSize(86, 21))
        self.label_5.setFont(font)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(184, 121, 86, 21))
        self.label_8.setMinimumSize(QSize(86, 21))
        self.label_8.setFont(font)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(281, 181, 93, 28))
        self.pushButton.setMinimumSize(QSize(93, 28))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(381, 181, 93, 28))
        self.pushButton_2.setMinimumSize(QSize(93, 28))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 61, 51))
        self.label.setMinimumSize(QSize(61, 51))
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u"../assets/iconos/LicenciaMensaje.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 20, 234, 31))
        self.label_2.setMinimumSize(QSize(234, 24))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PyStruct", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        Form.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_6.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Licencia:", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Fecha final:", None))
        self.label_8.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Renovar", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Estado de Licenciamiento:", None))
    # retranslateUi

