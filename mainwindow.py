from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QMessageBox, QGraphicsScene
from PySide6.QtWidgets import QTableWidgetItem
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, Qt, QPointF
from PySide6.QtGui import QPen, QColor, QTransform
from main_ui import Ui_MainWindow
from random import randint
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from classDir.datafile import *
from classDir.process import *
from classDir.processes import *
import random
import matplotlib.colors as mcolors

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data = DataFile()
        self.processes = Processes()
        
        self.ui.btn_cargar_datos.clicked.connect(self.action_openFile)
        self.ui.btn_ejecutar_algoritmo.clicked.connect(self.action_ejecutarAlgoritmo)
        self.ui.selector_algoritmo.addItem("FIFO")
        self.ui.selector_algoritmo.addItem("SJF")
        self.ui.selector_algoritmo.addItem("Prioridades")
        self.ui.selector_algoritmo.addItem("Round Robin")
    
    @Slot( )
    def action_openFile(self):
        mensaje1 = QMessageBox(self)
        mensaje1.setWindowTitle("Alerta.")
        mensaje1.setText("El archivo no se pudo abrir correctamente")
        mensaje1.setStandardButtons(QMessageBox.Ok)
        mensaje1.setDefaultButton(QMessageBox.Ok)
        mensaje1.setIcon(QMessageBox.Critical)
        
        mensaje2 = QMessageBox(self)
        mensaje2.setWindowTitle("Notificacion.")
        mensaje2.setText("Archivo cargado exitosamente")
        mensaje2.setStandardButtons(QMessageBox.Ok)
        mensaje2.setDefaultButton(QMessageBox.Ok)
        mensaje2.setIcon(QMessageBox.Information)
        
        path = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'TXT (*.txt)'
        )[0]
        
        if self.data.open(path):            
            for line in self.data.dataText:
                parts = line.strip().split(",")
                self.processes.insert(Process(parts[0], parts[1], parts[2], generar_color()))
                
            self.borrarTablaDatos()
            self.mostrarTablaDatos()
                
        else: 
            mensaje1.exec_()
    
    def mostrarTablaDatos(self):
        self.ui.tabla_datos.clear()
        self.ui.tabla_datos.setColumnCount(3)
        headers = ["Proceso", "Tiempo de Proceso", "Prioridad"]
        self.ui.tabla_datos.setHorizontalHeaderLabels(headers)
        
        processesList = self.processes.processes
        fila = 0
        
        for process in processesList:            
            proceso = QTableWidgetItem(str(process.name))
            tiempoProceso = QTableWidgetItem(str(process.duration))
            prioridad = QTableWidgetItem(str(process.priority))
            
            self.ui.tabla_datos.insertRow(fila)
            self.ui.tabla_datos.setItem(fila, 0, proceso)
            self.ui.tabla_datos.setItem(fila, 1, tiempoProceso)
            self.ui.tabla_datos.setItem(fila, 2, prioridad)
            fila += 1
    
    def borrarTablaDatos(self):
        # Borra los datos de la tabla
        self.ui.tabla_datos.clearContents()
        
        # Establece el nuevo número de filas y los encabezados
        self.ui.tabla_datos.setRowCount(0)
        
        self.ui.tabla_datos.setColumnCount(3)
        headers = ["Proceso", "Tiempo de Proceso", "Prioridad"]
        self.ui.tabla_datos.setHorizontalHeaderLabels(headers)
    
    def mostrarTablaResultados(self, nombreAlgoritmo, processesList):        
        if nombreAlgoritmo in ["SJF", "FIFO"]:
            self.ui.tabla_resultado.clear()
            self.ui.tabla_resultado.setColumnCount(4)
            headers = ["Proceso", "Inicio", "Tiempo de Proceso", "Final"]
            self.ui.tabla_resultado.setHorizontalHeaderLabels(headers)
            
            tiempoTotal = 0
            fila = 0
            
            for process in processesList:                
                proceso = QTableWidgetItem(str(process.name))
                inicio = QTableWidgetItem(str(tiempoTotal))
                tiempoProceso = QTableWidgetItem(str(process.duration))
                final = QTableWidgetItem(str(tiempoTotal + int(process.duration)))
                
                self.ui.tabla_resultado.insertRow(fila)
                
                self.ui.tabla_resultado.setItem(fila, 0, proceso)
                self.ui.tabla_resultado.setItem(fila, 1, inicio)
                self.ui.tabla_resultado.setItem(fila, 2, tiempoProceso)
                self.ui.tabla_resultado.setItem(fila, 3, final)
                
                fila += 1
                tiempoTotal += int(process.duration)
                
        if nombreAlgoritmo in ["Prioridades", "Round Robin"]:
            self.ui.tabla_resultado.clear()
            self.ui.tabla_resultado.setColumnCount(5)
            headers = ["Proceso", "Prioridad", "Inicio", "Tiempo de Proceso", "Final"]
            self.ui.tabla_resultado.setHorizontalHeaderLabels(headers)
            
            tiempoTotal = 0
            fila = 0
            
            for process in processesList:                
                proceso = QTableWidgetItem(str(process.name))
                priority = QTableWidgetItem(str(process.priority))
                inicio = QTableWidgetItem(str(tiempoTotal))
                tiempoProceso = QTableWidgetItem(str(process.duration))
                final = QTableWidgetItem(str(tiempoTotal + int(process.duration)))
                
                self.ui.tabla_resultado.insertRow(fila)
                
                self.ui.tabla_resultado.setItem(fila, 0, proceso)
                self.ui.tabla_resultado.setItem(fila, 1, priority)
                self.ui.tabla_resultado.setItem(fila, 2, inicio)
                self.ui.tabla_resultado.setItem(fila, 3, tiempoProceso)
                self.ui.tabla_resultado.setItem(fila, 4, final)
                
                fila += 1
                tiempoTotal += int(process.duration)
            
    def borrarTablaResultados(self):
        # Borra los datos de la tabla
        self.ui.tabla_resultado.clearContents()
    
    @Slot( )
    def action_ejecutarAlgoritmo(self):
        limpiar_layout(self.ui.grafica)
        self.borrarTablaResultados()
        algoritmoSeleccionado = self.ui.selector_algoritmo.currentText()
        
        if(algoritmoSeleccionado == "FIFO"):
            processesList = self.processes.getFIFOalgorithm()
            self.mostrarTablaResultados(algoritmoSeleccionado, processesList)               
            self.grafica1 = GraficarResultado("FIFO - El primero en llegar es el primero en salir", processesList)
            self.ui.grafica.addWidget(self.grafica1)
            
        elif(algoritmoSeleccionado == "SJF"):
            #ordenar la lista utiizando como base la duracion de cada proceso
            processesList = self.processes.getSJFalgorithm()
            self.mostrarTablaResultados(algoritmoSeleccionado, processesList)               
            self.grafica1 = GraficarResultado("SJF - El mas corto primero", processesList)
            self.ui.grafica.addWidget(self.grafica1)
        
        elif(algoritmoSeleccionado == "Prioridades"):
            #ordenar la lista utiizando como base la prioridad de cada proceso
            processesList = self.processes.getPriorityAlgorithm()
            self.mostrarTablaResultados(algoritmoSeleccionado, processesList)               
            self.grafica1 = GraficarResultado("Prioridad - Establecer Prioridades", processesList)
            self.ui.grafica.addWidget(self.grafica1)
        
        elif(algoritmoSeleccionado == "Round Robin"):
            #ordenar la lista utiizando como base la prioridad de cada proceso
            processesList = self.processes.getRoundRobinAlgorithm(3)
            self.mostrarTablaResultados(algoritmoSeleccionado, processesList)               
            self.grafica1 = GraficarResultado("Round Robin", processesList)
            self.ui.grafica.addWidget(self.grafica1)

class GraficarResultado(FigureCanvas):
    def __init__(self, nombreAlgoritmo, listaProcesos, figure=None):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(8, 3), facecolor='white')
        super().__init__(self.fig)
        
        # Obtener el nombre de los procesos
        nombresProcesos = [proceso.name for proceso in listaProcesos]

        # Posición de inicio de la primera barra
        start_pos = 0

        for i, proceso in enumerate(listaProcesos):
            # Ajustar la posición de inicio de la barra actual
            self.ax.barh(proceso.name, int(proceso.duration), left=start_pos, color=proceso.color, height=0.6)
            # Calcular la posición de inicio de la siguiente barra
            start_pos += int(proceso.duration)
            self.ax.text(start_pos, i, str(proceso.duration), ha='left', va='center')

        self.ax.set_yticks(range(len(listaProcesos)))
        self.ax.set_yticklabels(nombresProcesos)
        self.ax.invert_yaxis()  
        self.ax.set_title(nombreAlgoritmo)
        
def generar_color():
    colores_disponibles = [
    'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black',
    'purple', 'orange', 'lime', 'pink', 'teal', 'lavender', 'brown',
    'beige', 'maroon', 'mediumspringgreen', 'olive', 'coral', 'navy', 'grey',
    'darkgreen', 'salmon', 'gold', 'skyblue', 'tan', 'orchid', 'sienna', 'slateblue'
]
    return random.choice(colores_disponibles)

def limpiar_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

