from PySide2.QtWidgets import QTableWidget
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


def funcionTabla(self):
    
    a = QTableWidget()
    brush = QBrush(QColor(0, 0, 0, 255))
    brush.setStyle(Qt.NoBrush)
    __qtablewidgetitem27 = QTableWidgetItem()
    __qtablewidgetitem27.setForeground(brush);
    a.setItem(0, 0, __qtablewidgetitem27)
    a.setStyleSheet(u"background-color: rgb(213, 213, 213);\n"
    "selection-background-color: rgb(67, 179, 231);")
    a.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    a.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
    a.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
    a.setAutoScrollMargin(16)
    a.setDragDropMode(QAbstractItemView.NoDragDrop)
    a.setAlternatingRowColors(True)
    a.setSelectionMode(QAbstractItemView.ExtendedSelection)
    a.setSelectionBehavior(QAbstractItemView.SelectItems)
    a.setShowGrid(True)
    a.setGridStyle(Qt.DashLine)
    a.setRowCount(100000)
    a.setColumnCount(50)

    nombreColumnas = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",)

    a.setHorizontalHeaderLabels(nombreColumnas)
    
    a.cellChanged

    return a