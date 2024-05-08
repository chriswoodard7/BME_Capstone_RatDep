import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui

num_files = int(easygui.enterbox("Number of actigraphy files to process: "))

file_database = {}
file_keys = []

for file in range(0,num_files):
    # retrive file description
    file_desc = easygui.enterbox("Name of file: ")

    # import data
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    name_split = filename.split("/")

    # wrangle data
    filedata = pd.read_csv(filename)
    data_trim = filedata

    dtime = data_trim["Time"]
    dx = data_trim["X"]
    dy = data_trim["Y"]
    dp1 = data_trim["PIR1"]
    dp2 = data_trim["PIR2"]
    dp3 = data_trim["PIR3"]
    dp4 = data_trim["PIR4"]

    # maximum magnitude
    X_mag = np.abs(dx)
    Xmax = max(X_mag)
    Y_mag = np.abs(dy)
    Ymax = max(Y_mag)

    # non-zero average magnitude
    X_nz = X_mag[X_mag != 0]
    X_avg = np.average(X_nz)
    Y_nz = Y_mag[Y_mag != 0]
    Y_avg = np.average(Y_nz)

    # PIR percent activity
    n = len(dp1)
    up1 = len(dp1[dp1 == 1])
    P1_per = round(up1/n*100)

    up2 = len(dp2[dp2 == 1])
    P2_per = round(up2/n*100)

    up3 = len(dp3[dp3 == 1])
    P3_per = round(up3/n*100)

    up4 = len(dp4[dp4 == 1])
    P4_per = round(up4/n*100)

    # store values into dictionary
    data_val = [Xmax, Ymax, X_avg, Y_avg, P1_per, P2_per, P3_per, P4_per]

    file_keys.append(file_desc)
    file_database[file_desc] = data_val

# extract data
xmax_array = []
ymax_array = []
xavg_array = []
yavg_array = []
p1_per_array = []
p2_per_array = []
p3_per_array = []
p4_per_array = []

for key in file_database:
    xmax_array.append(file_database[key][0])
    ymax_array.append(file_database[key][1])
    xavg_array.append(file_database[key][2])
    yavg_array.append(file_database[key][3])
    p1_per_array.append(file_database[key][4])
    p2_per_array.append(file_database[key][5])
    p3_per_array.append(file_database[key][6])
    p4_per_array.append(file_database[key][7])

# plot maximmum velocities
maximums = {
    'X': xmax_array,
    'Y': ymax_array
}

n=0
fig, ax = plt.subplots(layout='constrained')
for a, m in maximums.items():
    offset = 0.25*n
    rects = ax.bar(np.arange(len(file_keys))+offset, m, 0.25, label=a)
    ax.bar_label(rects, padding=3)
    n += 1

ofs_max_plot_title = easygui.enterbox("OFS max velocity plot title: ")
ax.set_ylabel('OFS output (pixels/frame)')
ax.set_title(ofs_max_plot_title)
ax.set_xticks(np.arange(len(file_keys)), file_keys)
ax.legend()
plt.show()

# plot average velocities
maximums = {
    'X': xavg_array,
    'Y': yavg_array
}

n=0
fig, ax = plt.subplots(layout='constrained')
for a, m in maximums.items():
    offset = 0.25*n
    rects = ax.bar(np.arange(len(file_keys))+offset, m, 0.25, label=a)
    ax.bar_label(rects, padding=3)
    n += 1

ofs_avg_plot_title = easygui.enterbox("OFS avg velocity plot title: ")
ax.set_ylabel('OFS output (pixels/frame)')
ax.set_title(ofs_avg_plot_title)
ax.set_xticks(np.arange(len(file_keys)), file_keys)
ax.legend()
plt.show()

PIR_data = {
    '1': p1_per_array,
    '2': p2_per_array,
    '3': p3_per_array,
    '4': p4_per_array
}

n=0
fig, ax = plt.subplots(layout='constrained')
for a, m in PIR_data.items():
    offset = 0.2*n
    rects = ax.bar(np.arange(len(file_keys))+offset, m, 0.2, label=a)
    ax.bar_label(rects, padding=3)
    n += 1

pir_plot_title = easygui.enterbox("PIR activation plot title: ")
ax.set_ylabel('Time Activated (percent)')
ax.set_title(pir_plot_title)
ax.set_xticks(np.arange(len(file_keys)), file_keys)
ax.legend()
plt.show()