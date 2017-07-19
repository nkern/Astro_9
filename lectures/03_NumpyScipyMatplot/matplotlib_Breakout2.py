#!/usr/bin/env python3

##############################################
## Analyze data from Horsehead Nebula Image ##
##############################################

## Import Modules ##
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl

## Load Data ##
with open('data/horsehead.pkl', 'rb') as f:
	input = pkl.Unpickler(f)
	data = input.load()

## Rotate Data ##
data = np.rot90(data)

## Visualize 2D Array Data ##
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.imshow(data)
plt.show()

## Make Histogram of Pixel Values ##
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(data.ravel(), bins=100, alpha=0.85)
plt.show()

## Interesting Populations at pixel values of
## 4000 - 8000
## 10000 - 16000
## 19000 - 23000

## Make four plots with different clim ##
fig = plt.figure(figsize=(8,8))
fig.subplots_adjust(wspace=0.3, hspace=0.3)

# ax1
ax1 = fig.add_subplot(2, 2, 1)
cax1 = ax1.imshow(data, clim=(4000,8000))
fig.colorbar(cax1)

# ax2
ax2 = fig.add_subplot(2, 2, 2)
cax2 = ax2.imshow(data, clim=(10000,16000))
fig.colorbar(cax2)

# ax3
ax3 = fig.add_subplot(2, 2, 3)
cax3 = ax3.imshow(data, clim=(19000,23000))
fig.colorbar(cax3)

# ax4
ax4 = fig.add_subplot(2, 2, 4)
ax4.hist(data.ravel(), bins=100, alpha=0.85)
ax4.set_ylim(-200, 8000)
ax4.fill_between([4000, 8000], 0, 8000, facecolor='black', alpha=0.5)
ax4.fill_between([10000, 16000], 0, 8000, facecolor='black', alpha=0.5)
ax4.fill_between([19000, 23000], 0, 8000, facecolor='black', alpha=0.5)
ax4.set_xlabel('pixel value')

# display
plt.show()

