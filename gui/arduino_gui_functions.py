from   PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from   pyqtgraph import PlotWidget
import numpy as np
from   datetime import datetime
import os
import serial

class codebook():
    def __init__(self):
        return

class GUI_rt_act(object):

    def setupUi(self, rt_act):
        
        rt_act.setObjectName("rt_act")
        rt_act.resize(900, 1150)

        self.centralwidget = QtWidgets.QWidget(rt_act)

        self.plot_xvelocity = PlotWidget(self.centralwidget)
        self.plot_xvelocity.setGeometry(QtCore.QRect(100, 20, 700, 300))
        self.plot_xvelocity.setObjectName("plot_xvelocity")

        self.plot_yvelocity = PlotWidget(self.centralwidget)
        self.plot_yvelocity.setGeometry(QtCore.QRect(100, 370, 700, 300))
        self.plot_yvelocity.setObjectName('plot_yvelocity')

        self.plot_pir = PlotWidget(self.centralwidget)
        self.plot_pir.setGeometry(QtCore.QRect(100, 720, 700, 300))
        self.plot_pir.setObjectName('plot_pir')

        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(200, 1070, 150, 30))
        self.connect_button.setObjectName("connect_button")

        self.data_save_button = QtWidgets.QPushButton(self.centralwidget)
        self.data_save_button.setGeometry(QtCore.QRect(550, 1050, 150, 30))
        self.data_save_button.setObjectName("data_save_button")

        self.field_save = QtWidgets.QLabel(self.centralwidget) 
        self.field_save.setGeometry(QtCore.QRect(500, 1090, 250, 20))
        self.field_save.setObjectName("field_save")
        self.io_save = QtWidgets.QLineEdit(self.centralwidget)
        self.io_save.setGeometry(QtCore.QRect(500, 1090, 250, 20))
        self.io_save.setObjectName("io_save")
        # self.io_save.text()

        rt_act.setCentralWidget(self.centralwidget)

        self.translateUi(rt_act)

        self.connect_button.clicked.connect(rt_act.set_up_communication)
        self.data_save_button.clicked.connect(rt_act.save_data)

        self.initialize_ctrs_and_state()
        
        C = codebook()

    def initialize_ctrs_and_state(self):
        self.data_save_destination      = os.path.join(os.getcwd() , "actigraphy_rt")
        if not os.path.exists(self.data_save_destination):
            os.mkdir(self.data_save_destination)

        self.set_up_xvelocity_plot()
        self.set_up_yvelocity_plot()
        self.set_up_pir_plot()

        self.connect_flag = 0
        self.save_flag = 0
        self.save_ctr = 0
        self.xv_ctr = 0
        self.yv_ctr = 0
        self.pir_ctr = 0
        self.ctr = 0

        self.xv_trigger    = 0
        self.xv_switch     = 0
        self.xv_buffer     = np.zeros(102)
        self.xv_xaxis      = np.linspace(0,len(self.xv_buffer),len(self.xv_buffer))

        self.yv_trigger    = 0
        self.yv_switch     = 0
        self.yv_buffer     = np.zeros(102)
        self.yv_xaxis      = np.linspace(0,len(self.yv_buffer),len(self.yv_buffer))

        self.pir_trigger    = 0
        self.pir_switch     = 0
        self.pir1_buffer    = np.zeros(102)
        self.pir2_buffer    = np.zeros(102)
        self.pir3_buffer    = np.zeros(102)
        self.pir4_buffer    = np.zeros(102)
        self.pir_xaxis      = np.linspace(0,len(self.pir1_buffer),len(self.pir1_buffer))
        return
    
    def set_up_xvelocity_plot(self):# Function for setting up the Graph
        
        self.plot_xvelocity.setXRange(0, 102, padding =0)
        self.plot_xvelocity.setYRange(-100, 100, padding=0)
        styles = {'color':'black', 'font-size':'15px'}
        self.plot_xvelocity.setTitle("OFS X-Direction Velocity", **styles)
        self.plot_xvelocity.setBackground('w')
        self.plot_xvelocity.setLabel('left', 'OFS Motion Vector Output [frames/s]', **styles)
        self.plot_xvelocity.setLabel('bottom', 'Sample Num', **styles)
        self.xpens = pg.mkPen(width=3,color = (0,0,0))
         #[band_520_pen , band_610_pen , band_740_pen , band_nir_pen]

        return
    
    def set_up_yvelocity_plot(self):# Function for setting up the Graph
        
        self.plot_yvelocity.setXRange(0, 102, padding =0)
        self.plot_yvelocity.setYRange(-50, 50, padding=0)
        styles = {'color':'black', 'font-size':'15px'}
        self.plot_yvelocity.setTitle("OFS Y-Direction Velocity", **styles)
        self.plot_yvelocity.setBackground('w')
        self.plot_yvelocity.setLabel('left', 'OFS Motion Vector Output [frames/s]', **styles)
        self.plot_yvelocity.setLabel('bottom', 'Sample Num', **styles)
        self.ypens = pg.mkPen(width=3,color = (0,0,0))
         #[band_520_pen , band_610_pen , band_740_pen , band_nir_pen]

        return 
    
    def set_up_pir_plot(self):# Function for setting up the Graph
        
        self.plot_pir.setXRange(0, 102, padding =0)
        self.plot_pir.setYRange(0, 10, padding=0)
        styles = {'color':'black', 'font-size':'15px'}
        self.plot_pir.setTitle("PIR Sensor Activation", **styles)
        self.plot_pir.setBackground('w')
        # self.plot_pir.setLabel('left', 'Intensity', **styles)
        self.plot_pir.setLabel('bottom', 'Sample Num', **styles)
        self.pir1_pen = pg.mkPen(width=3,color = (28,31,212))
        self.pir2_pen = pg.mkPen(width=3,color = (28,212,58))
        self.pir3_pen = pg.mkPen(width=3,color = (212,28,206))
        self.pir4_pen = pg.mkPen(width=3,color = (212,123,28))

        return 
    
    def translateUi(self, rt_act):# Function connecting UI Button to Callbacks
        _translate = QtCore.QCoreApplication.translate
        rt_act.setWindowTitle(_translate("rt_act", "Actigraphy GUI"))

        self.connect_button.setText(_translate("rt_act", "Connect COM"))
        self.data_save_button.setText(_translate("rt_act", "Save Data"))

    
    def set_up_communication(self , debug = False):
        self.serial_port = 'COM7'
        self.baud_rate = 9600
        self.ser = serial.Serial(self.serial_port, self.baud_rate)
        self.connect_flag = 1
        return

    # need to make this more simpler - so when it calls, just read fro 
    def data_interrupt(self):
        # reads input from serial port, should be in 
        if self.connect_flag:
            line = self.ser.readline()
            decoded_line = str(line, encoding='utf-8')
            print(decoded_line)

            # parse data and store into individual vars
            split_line = decoded_line.split(",")

            xvelocity = int(split_line[0])
            yvelocity = int(split_line[1])
            pir1 = int(split_line[2]) + 1
            pir2 = int(split_line[3]) + 3
            pir3 = int(split_line[4]) + 5
            pir4 = int(split_line[5].strip()) + 7

            # if save_flag is true, save data into txt. file
            
            if self.save_flag % 2:
                if self.save_ctr == 0:
                    output = "Sample,Time,X,Y,PIR1,PIR2,PIR3,PIR4\n"
                    output_file.write(output)
                else:
                    write_to_file_path = f"{self.io_save.text()}.csv"
                    output_file = open(write_to_file_path, "w+")
                    output_file.write(decoded_line)

            #  update x-velocity buffer
            if self.xv_ctr <= 100:
                self.xv_buffer[self.xv_ctr] = xvelocity
                self.xv_ctr += 1
            elif self.xv_ctr == 101:
                self.xv_buffer[0:-1] = self.xv_buffer[1:self.xv_buffer.size]
                self.xv_buffer[-1] = xvelocity
            
            # update x-velocity plot
            if not (self.ctr%1):
                    self.plot_xvelocity.clear()
                    self.plot_xvelocity.plot(self.xv_xaxis, self.xv_buffer,pen=self.xpens)
            
            # update y-velocity buffer
            if self.yv_ctr <= 100:
                self.yv_buffer[self.yv_ctr] = yvelocity
                self.yv_ctr += 1
            elif self.yv_ctr == 101:
                self.yv_buffer[0:-1] = self.yv_buffer[1:self.yv_buffer.size]
                self.yv_buffer[-1] = yvelocity
            
            # update y-velocity plot
            if not (self.ctr%1):
                    self.plot_yvelocity.clear()
                    self.plot_yvelocity.plot(self.yv_xaxis, self.yv_buffer,pen=self.ypens)

            # update pir buffer
            if self.pir_ctr <= 100:
                self.pir1_buffer[self.pir_ctr] = pir1
                self.pir2_buffer[self.pir_ctr] = pir2
                self.pir3_buffer[self.pir_ctr] = pir3
                self.pir4_buffer[self.pir_ctr] = pir4
                self.pir_ctr += 1
            elif self.yv_ctr == 101:
                self.pir1_buffer[0:-1] = self.pir1_buffer[1:self.pir1_buffer.size]
                self.pir2_buffer[0:-1] = self.pir2_buffer[1:self.pir2_buffer.size]
                self.pir3_buffer[0:-1] = self.pir3_buffer[1:self.pir3_buffer.size]
                self.pir4_buffer[0:-1] = self.pir4_buffer[1:self.pir4_buffer.size]

                self.pir1_buffer[-1] = pir1
                self.pir2_buffer[-1] = pir2
                self.pir3_buffer[-1] = pir3
                self.pir4_buffer[-1] = pir4
            
            # update pir plot
            if not (self.ctr%1):
                    self.plot_pir.clear()
                    self.plot_pir.plot(self.pir_xaxis, self.pir1_buffer,pen=self.pir1_pen)
                    self.plot_pir.plot(self.pir_xaxis, self.pir2_buffer,pen=self.pir2_pen)
                    self.plot_pir.plot(self.pir_xaxis, self.pir3_buffer,pen=self.pir3_pen)
                    self.plot_pir.plot(self.pir_xaxis, self.pir4_buffer,pen=self.pir4_pen)
            self.ctr += 1
        return
    
    def save_data(self):
        self.save_flag+=1
        if self.save_flag % 2:
            print("Saving data... ")
        else:
            print("Stopped saving data, setting save counter to 0")
            self.save_ctr = 0
         
