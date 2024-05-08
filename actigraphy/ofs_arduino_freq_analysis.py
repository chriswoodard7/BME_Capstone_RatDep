import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui
import scipy.signal as sig

plot_title = easygui.enterbox("Plot title")

# dialog box to pick actigraphy data file to visualize
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()
name_split = filename.split("/")
run_name = name_split[-1]

# import data and process
filedata = pd.read_csv(filename)
data_trim = filedata

dtime = data_trim["Time"]
dx = data_trim["X"]
dy = data_trim["Y"]
dp1 = data_trim["PIR1"]
dp2 = data_trim["PIR2"]
dp3 = data_trim["PIR3"]
dp4 = data_trim["PIR4"]

f, Pxx = sig.periodogram(dx, fs=10)

plt.plot(f, Pxx, color="green")
plt.title(plot_title)
plt.xlabel("Frequency [Hz]")
plt.ylabel(r"Power spectral density $[V^2/Hz]$")
plt.tight_layout()
plt.show()