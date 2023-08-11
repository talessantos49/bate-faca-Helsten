import datetime
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QLCDNumber
#from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter
import datetime as dt

from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import matplotlib.pyplot as plt
import numpy as np
import time
import serial
import random
from random import randint

from ui_bateFaca import Ui_MainWindow as ui

data = dt.date.today()
hora = datetime.datetime.now()
qtCreatorFile = "bate-faca.ui"  # Esse e o arquivo .ui gerado pelo QtDesigner
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
ser = serial.Serial('/dev/ttyACM0', 9600)  # abre porta serial COM6


#class Canvas_grafica(FigureCanvas):
#    def __init__(self, parent=None):
#        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
#                                         sharey=True, facecolor='white')
#        super().__init__(self.fig)

#        nombres = ['15', '25', '30', '35', '40']
#        colores = ['red', 'red', 'red', 'red', 'red']
#        tamano = [10, 15, 20, 25, 30]

#        self.ax.bar(nombres, tamano, color=colores)
#        self.fig.suptitle('Grafica de Barras', size=9)
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.top = 30
        self.left = 10
        self.width = 1350
        self.height = 750
        self.date_time()
        self.InitUi()
        self.InitWindow()
        self.timer = QtCore.QTimer()
#        self.grafico = Canvas_grafica()
        # self.timer.timeout.connect(self.date_time)  # progress function

        #self.create_linechart()
        self.timer.timeout.connect(self.CallTwo)  # progress function
        self.timer.start(60)

    def InitUi(self):
        self.lcd = QLCDNumber()
        self.lcd.display(60)
#        random = randint(1, 200)

        while ser.inWaiting() == 0:
                pass
        lista = str(ser.readline())
        try:
                lista = lista.split("x")
                dados = float(lista[1])
                dados2 = (float(lista[2]) * -1)
                # leitura.append(random.randint(-5,10))  #teste com numeros aleatorios
                self.lcdNumber.display(dados)
                self.lcdNumber_2.display(dados2)
        except:
                lista = str(ser.readline())

        #self.lcdNumber.display(random)
        #self.lcdNumber_2.display(random)

    def InitWindow(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def CallTwo(self):
        self.date_time()
        self.InitUi()
        #self.graficos_up()

    #### Aqui comecam os codigos que manipulam os widgets

    def graficos_up(self):
        self.grafico_uno.addWidget(self.grafico)
        
    def date_time(self):
        organize = str(data).split("-")
        actual_date = str(organize[2] + "/" + organize[1] + "/" + organize[0])
        self.date_line.setText(str(actual_date))
        hours = dt.datetime.now().strftime("%H:%M:%S")
        self.hour_line.setText(str(hours))

    def graphics(self):

        chart_view = QChartView(self.create_line_chart())
        self.ui.gridLayout.addWidget(chart_view, 1, 1)
        self.charts.append(chart_view)

        leitura = []
        fig, ax = plt.subplots()
        ser = serial.Serial('/dev/ttyACM0', 9600)  # abre porta serial COM6

        x = []
        y1 = []
        y2 = []
        contador = 0
        eixo_x = 50
        while True:
            while ser.inWaiting() == 0:
                pass
            lista = str(ser.readline())
            try:
                lista = lista.split("x")
                print(lista)
                dados = float(lista[1])
                dados2 = (float(lista[2]) * -1)
                # dados = int(ser.readline()[:-1]) #firmware deve ter um delay de pelo menos 100ms entre cada envio
                # print (dados)
                ax.clear()
                ax.set_xlim([0, eixo_x])  # faixa do eixo horizontal
                ax.set_ylim([-5, 5])  # faixa do eixo vertical
                # leitura.append(random.randint(-5,10))  #teste com numeros aleatorios
                leitura.append(dados)
                y2.append(dados2)
                y1.append(0)
                plt.plot(y1, color="k")
                plt.plot(y2, color="r")
                plt.plot(leitura, color="b")
                # ax.plot(leitura, color="blue")
                # plt.pause(.000001)
                contador = contador + 1
                if contador > eixo_x:
                    leitura.pop(0)
                    y1.pop(0)
                    y2.pop(0)
            except:
                lista = str(ser.readline())

        ser.close()

 

#### Aqui terminam os codigos que manipulam os widgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
