from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import MainWindow
import sys

#Aplicacion de Qt
app = QApplication()

window = MainWindow()

#Se hace visible la ventana
window.show()

#Qt loop
sys.exit(app.exec_())