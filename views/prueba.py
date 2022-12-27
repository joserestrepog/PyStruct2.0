# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prueba.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class f_Prueba(object):
    def setupUi(self, f_Prueba):
        if not f_Prueba.objectName():
            f_Prueba.setObjectName(u"f_Prueba")
        f_Prueba.resize(400, 319)
        f_Prueba.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.pushButton = QPushButton(f_Prueba)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 210, 93, 28))
        self.pushButton_2 = QPushButton(f_Prueba)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 210, 93, 28))

        self.retranslateUi(f_Prueba)

        QMetaObject.connectSlotsByName(f_Prueba)
    # setupUi

    def retranslateUi(self, f_Prueba):
        f_Prueba.setWindowTitle(QCoreApplication.translate("f_Prueba", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("f_Prueba", u"ACER", None))
        self.pushButton_2.setText(QCoreApplication.translate("f_Prueba", u"FBFB", None))
    # retranslateUi

