from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import arduino_gui_functions as gui
import cProfile
import io
import pstats

class gui_launch(QtWidgets.QMainWindow, gui.GUI_rt_act):
    def __init__(self):
        super(gui_launch, self).__init__(None)
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.data_interrupt)
        self.timer.start()

app = QApplication(sys.argv)
system = gui_launch()
system.show()
sys.exit(app.exec_())