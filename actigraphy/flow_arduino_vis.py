import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import data
shake_close = pd.read_csv("shake_close_run.txt")
shake_far = pd.read_csv("shake_far_run.txt")
active_close = pd.read_csv("active_close_run.txt")
active_far = pd.read_csv("active_far_run.txt")
single_close = pd.read_csv("single_close_run.txt")
single_far = pd.read_csv("single_far_run.txt")

## data processing
# trim the data
sc_trim = shake_close[0:100]
sf_trim = shake_far[0:100]
ac_trim = active_close[0:100]
af_trim = active_far[0:100]
sic_trim = single_close[0:100]
sif_trim = single_far[0:100]

x = np.linspace(0, 10, 100)

# plotting
fig, ax = plt.subplots(2, sharex=True, )
fig.suptitle(r'5cm Testing Trials')
fig.set_figheight(7)
fig.set_figwidth(6)

ax[0].plot(x,sic_trim["0.1"], label="Single")
ax[0].plot(x,ac_trim["0.1"], label="Waving")
ax[0].plot(x,sc_trim["0.1"], label="Shaking")
ax[0].set_title(r"$v_x(t)$ vs. Time [s]")
ax[0].legend(loc="upper right")

ax[1].plot(x,sic_trim["0.2"], label="Single")
ax[1].plot(x,ac_trim["0.2"], label="Waving")
ax[1].plot(x,sc_trim["0.2"], label="Shaking")
ax[1].set_title(r"$v_y(t)$ vs. Time [s]")  
ax[1].set_xlabel(r"Time [s]")
ax[1].legend(loc="upper right")
plt.show()

fig1, ax1 = plt.subplots(2, sharex=True, )
fig1.suptitle(r'40cm Testing Trials')
fig1.set_figheight(7)
fig1.set_figwidth(6)

ax1[0].plot(x,sif_trim["0.1"], label="Single")
ax1[0].plot(x,af_trim["0.1"], label="Waving")
ax1[0].plot(x,sf_trim["0.1"], label="Shaking")
ax1[0].set_title(r"$v_x(t)$ vs. Time [s]")
ax1[0].legend(loc="upper right")

ax1[1].plot(x,sif_trim["0.2"], label="Single")
ax1[1].plot(x,af_trim["0.2"], label="Waving")
ax1[1].plot(x,sf_trim["0.2"], label="Shaking")
ax1[1].set_title(r"$v_y(t)$ vs. Time [s]")  
ax1[1].set_xlabel(r"Time [s]")
ax1[1].legend(loc="upper right")
plt.show()