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
# data_trim = filedata[0:500]
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
fig.set_figwidth(10)

plt.plot(dtime, dx, color="red")
plt.plot(dtime, dy, color="pink")
plt.ylabel("OFS Motion Vector Output [pixels/frame]")
plt.xlabel("Time")
plt.title(plot_title)
plt.legend(["X","Y"])
plt.show()