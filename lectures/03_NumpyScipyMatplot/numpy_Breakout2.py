#!/usr/bin/env python3

import numpy as np

# load all data in .csv file
data = np.loadtxt('data/clusters.csv', delimiter=',')

# select only HaloID, r200crit and m200crit columns
data = data[:, [0, 5, 6]]

# separate HaloID into an integer array
haloid = data[:, 0].astype(np.int)

# separate r200 and m200 into float arrays
data = data[:, 1:]

##### Find Match #####

# find row that matches criterion
select = np.where( (data[:,0]>1) & (data[:,1]<2e4) )

# print HaloID of matches
print("HaloID = {}".format(haloid[select]))


##### Append vdisp #####

# load in vdisp
vdisp = np.loadtxt('data/clusters.csv', usecols=(8,), delimiter=',')

# concatenate
data = np.vstack([ data.T, vdisp ]).T














