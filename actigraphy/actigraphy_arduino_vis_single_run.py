import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui

""" --------------------------------
actigraphy_arduino_vis_single_runn is a Python file used to visualizing
the OFS and PIR data for just a single data file. Note that this file
has not been updated yet to account for two OFS.
--------------------------------- """

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
d1 = data_trim["PIR1"]
d2 = data_trim["PIR2"]
d3 = data_trim["PIR3"]
d4 = data_trim["PIR4"]

max_motion = max(abs(dx))
print(max_motion)

# plotting
fig = plt.figure()
fig.set_figheight(7)
fig.set_figwidth(6)

gs = fig.add_gridspec(6,1)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[3, 0])
ax5 = fig.add_subplot(gs[4, 0])
ax6 = fig.add_subplot(gs[5, 0])

ax1.plot(dtime, dx, 'blue')
ax1.set_title(r"$v_x(t)$ vs. Time [s]")

ax2.plot(dtime, dy, 'red')
ax2.set_title(r"$v_y(t)$ vs. Time [s]")

ax3.plot(dtime, d1, 'green')
ax3.set_title("PIR1 vs. Time [s]")

ax4.plot(dtime, d2, 'orange')
ax4.set_title("PIR2 vs. Time [s]")

ax5.plot(dtime, d3, 'purple')
ax5.set_title("PIR3 vs. Time [s]")

ax6.plot(dtime, d4, 'black')
ax6.set_title("PIR4 vs. Time [s]")
ax6.set_xlabel("Time [s]")

plt.suptitle(plot_title)
plt.tight_layout()
plt.show()

