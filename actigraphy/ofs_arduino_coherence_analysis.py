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
filename1 = askopenfilename()
name_split = filename1.split("/")
run_name = name_split[-1]

# import data and process
# import first dataset
filedata1 = pd.read_csv(filename1)
data_trim1 = filedata1[0:1200]

dtime1 = data_trim1["Time"]
dx1 = data_trim1["X"]
dy1 = data_trim1["Y"]
# dp11 = data_trim1["PIR1"]
# dp21 = data_trim1["PIR2"]
# dp3 = data_trim1["PIR3"]
# dp4 = data_trim1["PIR4"]

# import second dataset
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename2 = askopenfilename()
name_split = filename2.split("/")
run_name = name_split[-1]

filedata2 = pd.read_csv(filename2)
data_trim2 = filedata2[0:1200]

dtime1 = data_trim2["Time"]
dx2 = data_trim2["X"]
dy2 = data_trim2["Y"]

# f, Pxx = sig.periodogram(dx, fs=100)

# plt.plot(f, Pxx, color="darkgreen")
# plt.title(plot_title)
# plt.xlabel("Frequency [Hz]")
# plt.ylabel(r"Power spectral density $[V^2/Hz]$")
# plt.tight_layout()
# plt.show()

plt.cohere(dx1, dx2, Fs=10)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Coherence")
plt.title(plot_title, fontweight='bold')
plt.show()