#!/usr/bin/env python3

####################################
### Reproduce two-subplot figure ###
####################################

## Import Modules ##
import matplotlib.pyplot as plt
import numpy as np

# time array
time1 = np.linspace(0, 5, 51)
time2 = np.linspace(0, 2, 51)

# y functions
y1 = np.cos(2 * np.pi * time1) * np.exp(-time1)
y2 = np.cos(2 * np.pi * time2) 

## Generate Plots ##

# make figure
fig = plt.figure(figsize=(8, 6))

# make first subplot
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# put data on ax1
ax1.plot(time1, y1, marker='o', linestyle='-', markersize=9, color='steelblue')

# label ax1
ax1.set_ylabel('Dampled oscillation')

# put data on ax2
ax2.plot(time2, y2, marker='.', markersize=9, linestyle='-', color='steelblue')

# label ax2
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Undamped')

# set title
ax1.set_title('A tale of two subplots')

# display
plt.show()
