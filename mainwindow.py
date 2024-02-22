from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Qt, QPointF
from PySide6.QtGui import QPen, QColor, QTransform
from main_ui import Ui_MainWindow
from random import randint
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.grafica1 = Grafica02()
        
        self.ui.grafica.addWidget(self.grafica1)
        

class Canvas_grafica(FigureCanvas):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5,5), sharey=True, facecolor= 'white')
        super().__init__(self.fig)
        nombres = ['15', '25', '30','35', '40']
        colores = ['red', 'red', 'red', 'red','red']
        tamaño = [10, 15, 20, 25, 30]
        
        self.ax.bar(nombres, tamaño, color = colores)
        self.fig.suptitle( 'Grafica de Barras')

class GraficaDeEscalera(FigureCanvas):
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(8,3), facecolor='white')
        super().__init__(self.fig)
        nombres = ['15', '25', '30', '35', '40']
        colores = ['red', 'green', 'blue', 'orange', 'purple']
        tamaño = [10, 15, 20, 25, 30]

        for i in range(len(nombres)):
            self.ax.barh(i, tamaño[i], color=colores[i], height=0.6)
            self.ax.text(tamaño[i], i, str(tamaño[i]), ha='left', va='center')

        self.ax.set_yticks(range(len(nombres)))
        self.ax.set_yticklabels(nombres)
        self.ax.invert_yaxis()  # Invertir el eje y para que la primera categoría esté en la parte superior
        self.ax.set_title('Gráfica de Barras Horizontal en forma de Escalera')
        
class Grafica02(FigureCanvas):
    def __init__(self, figure=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(8,3), facecolor='white')
        super().__init__(self.fig)
        nombres = ['15', '25', '30', '35', '40']
        colores = ['red', 'green', 'blue', 'orange', 'purple']
        tamaño = [10, 15, 20, 25, 30]

        # Posición de inicio de la primera barra
        start_pos = 0

        for i in range(len(nombres)):
            # Ajustar la posición de inicio de la barra actual
            self.ax.barh(i, tamaño[i], left=start_pos, color=colores[i], height=0.6)
            # Calcular la posición de inicio de la siguiente barra
            start_pos += tamaño[i]
            self.ax.text(start_pos, i, str(tamaño[i]), ha='left', va='center')

        self.ax.set_yticks(range(len(nombres)))
        self.ax.set_yticklabels(nombres)
        self.ax.invert_yaxis()  
        self.ax.set_title('Gráfica de Barras Horizontal en forma de Escalera')

