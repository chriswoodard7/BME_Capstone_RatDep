import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import easygui

# plot_title = easygui.enterbox("Plot title")

# # dialog box to pick actigraphy data file to visualize
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename()
# name_split = filename.split("/")
# run_name = name_split[-1]

# # import data and process
# filedata = pd.read_csv(filename)
# data_trim = filedata

# dtime = data_trim["Time"]
# dx = data_trim["X"]
# dy = data_trim["Y"]
# dp1 = data_trim["PIR1"]
# dp2 = data_trim["PIR2"]
# dp3 = data_trim["PIR3"]
# dp4 = data_trim["PIR4"]

# # plotting
# fig = plt.figure()
# fig.set_figheight(7)
# fig.set_figwidth(10)

# plt.plot(dtime1, dx1)
# plt.plot(dtime1, dx2)
# plt.plot(dtime1, dy1)
# plt.plot(dtime1, dy2)
# plt.xlabel("Time [s]")
# plt.ylabel("Motion [pixel/frame]")
# plt.legend()

# plt.plot(dtime, dx)

# gs = fig.add_gridspec(2,1)
# ax1 = fig.add_subplot(gs[0, 0])
# ax2 = fig.add_subplot(gs[1, 0])

# ax1.plot(dtime1, dx1, 'blue')
# ax1.plot(dtime1, dx2, 'turquoise')
# ax1.set_title(r"$v_x(t)$ vs. Time [s]")
# ax1.legend(["Active", "Shaking"], loc="upper right")

# ax2.plot(dtime1, dy1, 'olive')
# ax2.plot(dtime1, dy2, 'lime')
# ax2.set_title(r"$v_y(t)$ vs. Time [s]")
# ax2.legend(["Active", "Shaking"], loc="upper right")

# plt.suptitle(f"{plot_title}")
# fig.supxlabel("Time [s]")
# fig.supylabel("Motion [pixel/frame]")
# plt.tight_layout()
# plt.show()

num_files = int(easygui.enterbox("Number of actigraphy files to process: "))

file_databasex = {}
file_databasey = {}
file_keys = []
time_array = []
ticks = []
tick = 0

for file in range(0,num_files):
    # retrive file description
    tick+=1
    file_desc = easygui.enterbox("Name of file: ")

    # import data
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()
    name_split = filename.split("/")

    # wrangle data
    filedata = pd.read_csv(filename)
    data_trim = filedata[0:581]

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
    new_keyx = file_desc + "_x"
    new_keyy = file_desc + "_y"
    file_databasex[new_keyx] = dx
    file_databasey[new_keyy] = dy
    time_array = dtime
    ticks.append(tick)

###############################
# PLOT X-DIRECTION VELOCITIES #
###############################
    
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

tick_new = 0
for key in file_databasex:
    tick_new+=1
    # Generate the random data for the y=k 'layer'.
    # xs = np.arange(20)
    # ys = np.random.rand(20)

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    # cs = [c] * len(xs)
    # cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.plot(time_array, file_databasex[key], zs=tick_new, zdir='y', alpha=0.8)

ax.set_xlabel('Time')
ax.set_ylabel('Run #')
ax.set_zlabel('OFS X-Direction Velocity [frames/s]')

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(ticks)

plot_title = easygui.enterbox("Plot title: ")
ax.set_title(plot_title)

plt.show()

###############################
# PLOT Y-DIRECTION VELOCITIES #
###############################

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

tick_new = 0
for key in file_databasey:
    tick_new+=1
    # Generate the random data for the y=k 'layer'.
    # xs = np.arange(20)
    # ys = np.random.rand(20)

    # You can provide either a single color or an array with the same length as
    # xs and ys. To demonstrate this, we color the first bar of each set cyan.
    # cs = [c] * len(xs)
    # cs[0] = 'c'

    # Plot the bar graph given by xs and ys on the plane y=k with 80% opacity.
    ax.plot(time_array, file_databasey[key], zs=tick_new, zdir='y', alpha=0.8)

ax.set_xlabel('Time')
ax.set_ylabel('Run #')
ax.set_zlabel('OFS Y-Direction Velocity [frames/s]')

# On the y-axis let's only label the discrete values that we have data for.
ax.set_yticks(ticks)

plot_title = easygui.enterbox("Plot title: ")
ax.set_title(plot_title)

plt.show()