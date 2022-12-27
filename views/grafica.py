# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grafica.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class f_Grafica(object):
    def setupUi(self, f_Grafica):
        if not f_Grafica.objectName():
            f_Grafica.setObjectName(u"f_Grafica")
        f_Grafica.resize(1086, 831)
        f_Grafica.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.gridLayout = QGridLayout(f_Grafica)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fr_Grafica = QFrame(f_Grafica)
        self.fr_Grafica.setObjectName(u"fr_Grafica")
        self.fr_Grafica.setMinimumSize(QSize(1085, 831))
        self.fr_Grafica.setMaximumSize(QSize(1085, 831))
        self.fr_Grafica.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.fr_Grafica.setFrameShape(QFrame.StyledPanel)
        self.fr_Grafica.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.fr_Grafica, 0, 0, 1, 1)


        self.retranslateUi(f_Grafica)

        QMetaObject.connectSlotsByName(f_Grafica)
    # setupUi

    def retranslateUi(self, f_Grafica):
        f_Grafica.setWindowTitle(QCoreApplication.translate("f_Grafica", u"Grafica", None))
    # retranslateUi

