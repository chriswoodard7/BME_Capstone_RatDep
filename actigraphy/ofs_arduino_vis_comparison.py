import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui

plot_title = easygui.enterbox("Plot title")

# dialog box to pick actigraphy data file to visualize
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename1 = askopenfilename()
name_split1 = filename1.split("/")
run_name1 = name_split1[-1]

# import data and process
filedata1 = pd.read_csv(filename1)
data_trim1 = filedata1

dtime1 = data_trim1["Time"]
dx1 = data_trim1["X"]
dy1 = data_trim1["Y"]
d11 = data_trim1["PIR1"]
d21 = data_trim1["PIR2"]
d31 = data_trim1["PIR3"]
d41 = data_trim1["PIR4"]

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename2 = askopenfilename()
name_split2 = filename2.split("/")
run_name2 = name_split2[-1]

# import data and process
# shaking
filedata2 = pd.read_csv(filename2)
data_trim2 = filedata2[::3]

dtime2 = data_trim2["Time"]
dx2 = data_trim2["X"]
dy2 = data_trim2["Y"]
d12 = data_trim2["PIR1"]
d22 = data_trim2["PIR2"]
d32 = data_trim2["PIR3"]
d42 = data_trim2["PIR4"]

if len(dx1) > len(dx2):
    dx1 = dx1[0:len(dx2)]
    dy1 = dy1[0:len(dy2)]
    dtime1 = dtime1[0:len(dtime2)]
else:
    dx2 = dx2[0:len(dx1)]
    dy2 = dy2[0:len(dy1)]
    dtime2 = dtime2[0:len(dtime1)]


# plotting
fig = plt.figure()
fig.set_figheight(7)
fig.set_figwidth(10)

# plt.plot(dtime1, dx1)
# plt.plot(dtime1, dx2)
# plt.plot(dtime1, dy1)
# plt.plot(dtime1, dy2)
# plt.xlabel("Time [s]")
# plt.ylabel("Motion [pixel/frame]")
# plt.legend()

gs = fig.add_gridspec(2,1)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])

ax1.plot(dtime1, dx1, 'blue')
ax1.plot(dtime1, dx2, 'turquoise')
ax1.set_title(r"$v_x(t)$ vs. Time [s]")
ax1.legend(["Active", "Shaking"], loc="upper right")

ax2.plot(dtime1, dy1, 'olive')
ax2.plot(dtime1, dy2, 'lime')
ax2.set_title(r"$v_y(t)$ vs. Time [s]")
ax2.legend(["Active", "Shaking"], loc="upper right")

plt.suptitle(f"{plot_title}")
fig.supxlabel("Time [s]")
fig.supylabel("Motion [pixel/frame]")
plt.tight_layout()
plt.show()

