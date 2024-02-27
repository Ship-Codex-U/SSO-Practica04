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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1031, 547)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 260, 531, 231))
        self.grafica = QVBoxLayout(self.verticalLayoutWidget)
        self.grafica.setObjectName(u"grafica")
        self.grafica.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 230, 239, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(10, 0))
        self.tabla_resultado = QTableWidget(self.centralwidget)
        self.tabla_resultado.setObjectName(u"tabla_resultado")
        self.tabla_resultado.setGeometry(QRect(470, 30, 531, 191))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabla_resultado.sizePolicy().hasHeightForWidth())
        self.tabla_resultado.setSizePolicy(sizePolicy1)
        self.tabla_resultado.setMinimumSize(QSize(0, 100))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(470, 0, 239, 21))
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(10, 0))
        self.btn_cargar_datos = QPushButton(self.centralwidget)
        self.btn_cargar_datos.setObjectName(u"btn_cargar_datos")
        self.btn_cargar_datos.setGeometry(QRect(30, 0, 121, 24))
        self.tabla_datos = QTableWidget(self.centralwidget)
        self.tabla_datos.setObjectName(u"tabla_datos")
        self.tabla_datos.setGeometry(QRect(30, 30, 421, 191))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 240, 125, 21))
        self.selector_algoritmo = QComboBox(self.centralwidget)
        self.selector_algoritmo.setObjectName(u"selector_algoritmo")
        self.selector_algoritmo.setGeometry(QRect(170, 240, 151, 22))
        self.btn_ejecutar_algoritmo = QPushButton(self.centralwidget)
        self.btn_ejecutar_algoritmo.setObjectName(u"btn_ejecutar_algoritmo")
        self.btn_ejecutar_algoritmo.setGeometry(QRect(30, 290, 181, 24))
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
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Grafica", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.btn_cargar_datos.setText(QCoreApplication.translate("MainWindow", u"Cargar Datos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecciona algoritmo:", None))
        self.btn_ejecutar_algoritmo.setText(QCoreApplication.translate("MainWindow", u"Ejecutar Algoritmo", None))
    # retranslateUi

