import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui

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

max_motion = max(abs(dx1))
print("Max OFS1 X:")
print(max_motion)
print("Max OFS2 X:")
print(max(abs(dx2)))

# plotting
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True)
fig.set_figheight(7)
fig.set_figwidth(10)

ax1.plot(dtime, dx1, color="darkblue")
ax1.plot(dtime, dy1, color="deepskyblue")
ax1.legend(["X (OFS #1)","Y (OFS #1)"])
ax2.plot(dtime, dx2, color="limegreen")
ax2.plot(dtime, dy2, color="green")
ax2.legend(["X (OFS #2)", "Y (OFS #2)"])
fig.supylabel("OFS Motion Vector Output [frames/s]")
fig.supxlabel("Time")
fig.suptitle(plot_title)
plt.show()