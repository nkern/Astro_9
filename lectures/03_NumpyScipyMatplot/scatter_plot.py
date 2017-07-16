#!/usr/bin/env python3

# import modules
import numpy as np
import matplotlib.pyplot as plt

# create some fake data
x = np.linspace(0, 2*np.pi, 25)
y1 = np.sin(x)
y2 = np.cos(x)

# make a figure object to hold plots
fig = plt.figure()

# create a single axis object to make a subplot
ax = fig.add_subplot(111)

# plot the three trig functions
ax.scatter(x, y1, c='g')
ax.scatter(x, y2, c='b')

# display plots

