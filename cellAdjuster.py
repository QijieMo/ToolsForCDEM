#!/usr/bin/env python2
import os
import sys
from math import sqrt
import numpy as np
from pprint import pprint as pp
#Taking arguments with error control
if len(sys.argv)<3 or len(sys.argv)>3:
    print "Arguments are wrong.\n" \
          "Correct usage: cellAdjuster.py xyz_file space_ang\n" \
          "space_ang is how much space you need for corner atoms from the cell walls"
    exit(0)
else:
    XyzFileName = sys.argv[1]
    space_ang = float(sys.argv[2])

XyzData = open(XyzFileName,'r').readlines()
XyzAtnum = int(XyzData[0].rstrip(" ").lstrip(" "))
XyzCommentLine = XyzData[1]
XyzData = XyzData[2:]

x_vals = []
y_vals = []
z_vals = []
at_names = []

print "Found",XyzAtnum,"atoms"

for i in range(len(XyzData)):
	XyzData[i] = XyzData[i].rstrip("\n").split()
	at_names.append(XyzData[i][0])
	x_vals.append(float(XyzData[i][1]))
	y_vals.append(float(XyzData[i][2]))
	z_vals.append(float(XyzData[i][3]))

print "Now moving atoms in xyz to not have negative numbers.."
print "Minimum values are: (x,y,z)",min(x_vals),min(y_vals),min(z_vals)
x_min = min(x_vals)
y_min = min(y_vals)
z_min = min(z_vals)
for i in range(len(x_vals)):
	x_vals[i] -= x_min - space_ang/2. 
	y_vals[i] -= y_min - space_ang/2. 
	z_vals[i] -= z_min - space_ang/2.
print "Adjusted coordinates are:"
for i in range(len(x_vals)):
	print at_names[i],x_vals[i],y_vals[i],z_vals[i]
print "Writing to xyz.."
print "Xyz name is: "+ XyzFileName.rstrip(".xyz")+"_originated.xyz"
new_name = XyzFileName.rstrip(".xyz")+"_originated.xyz"
new_file = open(new_name,"w")
new_file.write(str(XyzAtnum)+"\n\n")
for i in range(len(x_vals)):
	new_file.write(at_names[i]+"\t"+str(x_vals[i])+"\t"+str(y_vals[i])+"\t"+str(z_vals[i])+"\n")
print "Adjusting cell.."
cell = [0.]*9
cell = np.array(cell).reshape(3,3)
x_max = max(x_vals)
y_max = max(y_vals)
z_max = max(z_vals)
cell[0][0] = x_max + space_ang/2.
cell[1][1] = y_max + space_ang/2.
cell[2][2] = z_max + space_ang/2.
print "Cell_file name is: cell_file"
print "Assumed cell is: (max_(x,y,z) + space_ang/2.)"
pp(cell)
cell_ad = open("cell_file","w")
for i in range(3):
	cell_ad.write(str(cell[i][0])+"\t"+str(cell[i][1])+"\t"+str(cell[i][2])+"\n")
print "You can visualize the result with the command below:"
print "xyz_visualizer.py "+new_name+" cell_file"