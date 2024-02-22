# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 471)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vista_grafica = QFrame(self.centralwidget)
        self.vista_grafica.setObjectName(u"vista_grafica")
        self.vista_grafica.setGeometry(QRect(250, 30, 691, 351))
        self.vista_grafica.setFrameShape(QFrame.StyledPanel)
        self.vista_grafica.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.vista_grafica)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 641, 301))
        self.grafica = QVBoxLayout(self.verticalLayoutWidget)
        self.grafica.setObjectName(u"grafica")
        self.grafica.setContentsMargins(0, 0, 0, 0)
        self.btn_cargar_datos = QPushButton(self.centralwidget)
        self.btn_cargar_datos.setObjectName(u"btn_cargar_datos")
        self.btn_cargar_datos.setGeometry(QRect(40, 30, 101, 21))
        self.tabla_datos = QTableWidget(self.centralwidget)
        self.tabla_datos.setObjectName(u"tabla_datos")
        self.tabla_datos.setGeometry(QRect(40, 80, 161, 151))
        self.selector_algoritmo = QComboBox(self.centralwidget)
        self.selector_algoritmo.setObjectName(u"selector_algoritmo")
        self.selector_algoritmo.setGeometry(QRect(50, 300, 141, 31))
        self.btn_ejecutar_algoritmo = QPushButton(self.centralwidget)
        self.btn_ejecutar_algoritmo.setObjectName(u"btn_ejecutar_algoritmo")
        self.btn_ejecutar_algoritmo.setGeometry(QRect(60, 350, 121, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1031, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_cargar_datos.setText(QCoreApplication.translate("MainWindow", u"Cargar datos", None))
        self.btn_ejecutar_algoritmo.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Algoritmo", None))
    # retranslateUi

