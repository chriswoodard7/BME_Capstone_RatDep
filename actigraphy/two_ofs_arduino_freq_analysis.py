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
dx1 = data_trim["X1"]
dy1 = data_trim["Y1"]
dx2 = data_trim["X2"]
dy2 = data_trim["Y2"]
d1 = data_trim["PIR1"]
d2 = data_trim["PIR2"]
d3 = data_trim["PIR3"]
d4 = data_trim["PIR4"]

f1, Pxx1 = sig.periodogram(dx1, fs=33)
f2, Pxx2 = sig.periodogram(dx2, fs=33)

fig, axs = plt.subplots(2, 1, figsize=(10, 7))
axs[0].plot(f1, Pxx1, color="deepskyblue")
axs[1].plot(f2, Pxx2, color="limegreen")
fig.legend(["OFS1 X", "OFS2 X"])
fig.suptitle(plot_title)
fig.supxlabel("Frequency [Hz]")
fig.supylabel(r"Power spectral density $[V^2/Hz]$")
plt.tight_layout()
plt.show()