#!/usr/bin/env python2
import sys
import numpy as np

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: get_volume.py cell_file"
    exit(0)
else:
    cell_file = sys.argv[1]

cell_file_raw = open(cell_file,"r")
cell_file_raw_data = cell_file_raw.readlines()
cell_array = []
for line in cell_file_raw_data:
	line = line.split()
	line[0] = float(line[0])
	line[1] = float(line[1])
	line[2] = float(line[2])
	cell_array.append(line)
cell_file_raw.close()
volume = np.fabs(np.dot(np.cross(cell_array[0],cell_array[1]),cell_array[2]))
print volume
