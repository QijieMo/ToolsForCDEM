#!/usr/bin/env python2
import numpy as np
from pprint import pprint as pp
import sys

np.set_printoptions(suppress=True)
np.set_printoptions(precision=10)

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: originator.py xyz_name"
    exit(0)
else:
    xyz_name = sys.argv[1]

xyz_file = open(xyz_name,"r").readlines()
at_number = int(xyz_file[0].rstrip(" ").lstrip(" "))
xyz_file = xyz_file[2:]
a = np.zeros(len(xyz_file)*3).reshape(len(xyz_file),3)
atom_names = []

for i in range(len(xyz_file)):
	xyz_file[i] = xyz_file[i].rstrip("\n")
	xyz_file[i] = xyz_file[i].split()
	atom_names.append(xyz_file[i][0])
	a[i][0] = xyz_file[i][1]
	a[i][1] = xyz_file[i][2]
	a[i][2] = xyz_file[i][3]

ref_at = [0.,0.,0.]
ref_at[:] = a[0]

for i in range(len(a)):
	a[i] = a[i] - ref_at

#for i in range(len(a)):
#  print a[i][0],"\t",a[i][1],"\t",a[i][2]

print "Writing new xyz.."
print "New xyz name is:",xyz_name.rstrip(".xyz")+"_originated.xyz"
new_xyz = open(xyz_name.rstrip(".xyz")+"_originated.xyz","w")
new_xyz.write(str(at_number)+"\n\n")
for i in range(len(a)):
	new_xyz.write(atom_names[i]+"\t"+str(round(a[i][0],4))+"\t"+str(round(a[i][1],4))+"\t"+str(round(a[i][2],4))+"\n")

