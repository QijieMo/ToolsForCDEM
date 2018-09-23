#!/usr/bin/env python2
from pprint import pprint as pp
import sys

def weights(at_name):
    if at_name=="H": return 1.008
    if at_name=="He": return 4.003
    if at_name=="Li": return 6.941
    if at_name=="Be": return 9.012
    if at_name=="B": return 10.811
    if at_name=="C": return 12.011
    if at_name=="N": return 14.007
    if at_name=="O": return 15.999
    if at_name=="F": return 18.998
    if at_name=="Ne": return 20.180
    if at_name=="Na": return 22.990
    if at_name=="Mg": return 24.305
    if at_name=="Al": return 26.982
    if at_name=="Si": return 28.086
    if at_name=="P": return 30.974
    if at_name=="S": return 32.065
    if at_name=="Cl": return 35.453
    if at_name=="Ar": return 39.948
    if at_name=="K": return 39.098
    if at_name=="Ca": return 40.078
    if at_name=="Sc": return 44.956
    if at_name=="Ti": return 47.867
    if at_name=="V": return 50.942
    if at_name=="Cr": return 51.996
    if at_name=="Mn": return 54.938
    if at_name=="Fe": return 55.845
    if at_name=="Co": return 58.933
    if at_name=="Ni": return 58.693
    if at_name=="Cu": return 63.546
    if at_name=="Zn": return 65.390
    if at_name=="Ga": return 69.723
    if at_name=="Ge": return 72.640
    if at_name=="81": return 74.922
    if at_name=="Se": return 78.960
    if at_name=="Br": return 79.904
    if at_name=="Kr": return 83.800
    if at_name=="Rb": return 85.468
    if at_name=="Sr": return 87.620
    if at_name=="Y": return 88.906
    if at_name=="Zr": return 91.224
    if at_name=="Nb": return 92.906
    if at_name=="Mo": return 95.940
    if at_name=="Tc": return 98.000
    if at_name=="Ru": return 101.070
    if at_name=="Rh": return 102.906
    if at_name=="Pd": return 106.420
    if at_name=="Ag": return 107.868
    if at_name=="Cd": return 112.411
    if at_name=="In": return 114.818
    if at_name=="Sn": return 118.710
    if at_name=="Sb": return 121.760
    if at_name=="Te": return 127.600
    if at_name=="I": return 126.905
    if at_name=="Xe": return 131.293
    if at_name=="Cs": return 132.906
    if at_name=="Ba": return 137.327
    if at_name=="La": return 138.906
    if at_name=="Ce": return 140.116
    if at_name=="Pr": return 140.908
    if at_name=="Nd": return 144.240
    if at_name=="Pm": return 145.000
    if at_name=="Sm": return 150.360
    if at_name=="Eu": return 151.964
    if at_name=="Gd": return 157.250
    if at_name=="Tb": return 158.925
    if at_name=="Dy": return 162.500
    if at_name=="Ho": return 164.930
    if at_name=="Er": return 167.259
    if at_name=="Tm": return 168.934
    if at_name=="Yb": return 173.040
    if at_name=="Lu": return 174.967
    if at_name=="Hf": return 178.490
    if at_name=="Ta": return 180.948
    if at_name=="W": return 183.840
    if at_name=="Re": return 186.207
    if at_name=="Os": return 190.230
    if at_name=="Ir": return 192.217
    if at_name=="Pt": return 195.078
    if at_name=="Au": return 196.967
    if at_name=="Hg": return 200.590
    if at_name=="Tl": return 204.383
    if at_name=="Pb": return 207.200
    if at_name=="Bi": return 208.980
    if at_name=="Po": return 209.000
    if at_name=="At": return 210.000
    if at_name=="Rn": return 222.000
    if at_name=="Fr": return 223.000
    if at_name=="Ra": return 226.000
    if at_name=="Ac": return 227.000
    if at_name=="Th": return 232.038
    if at_name=="Pa": return 231.036
    if at_name=="U": return 238.029
    if at_name=="Np": return 237.000
    if at_name=="Pu": return 244.000
    if at_name=="Am": return 243.000
    if at_name=="Cm": return 247.000
    if at_name=="Bk": return 247.000
    if at_name=="Cf": return 251.000
    if at_name=="Es": return 252.000
    if at_name=="Fm": return 257.000
    if at_name=="Md": return 258.000
    if at_name=="No": return 259.000
    if at_name=="Lr": return 262.000
    if at_name=="Rf": return 261.000
    if at_name=="Db": return 262.000
    if at_name=="Sg": return 266.000
    if at_name=="Bh": return 264.000
    if at_name=="Hs": return 277.000
    if at_name=="Mt": return 268.000 

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: center_masser.py xyz_name"
    exit(0)
else:
    xyz_name = sys.argv[1]

xyz_file = open(xyz_name,"r").readlines()
at_number = int(xyz_file[0].rstrip(" ").lstrip(" "))
xyz_file = xyz_file[2:]
print "Found "+str(at_number)+" atoms\nNow calculating center of mass..."
at_list = []
x_vals = []
y_vals = []
z_vals = []
for i in range(at_number):
	at_list.append(xyz_file[i].split()[0])
	x_vals.append(xyz_file[i].split()[1])
	y_vals.append(xyz_file[i].split()[2])
	z_vals.append(xyz_file[i].split()[3])
print "Parsing part finished"
print "Now constructing atom weights array"
at_weights = []
for i in range(at_number):
	at_weights.append(weights(at_list[i]))
	print at_list[i],"==>",weights(at_list[i])
print "Everything is ready, finding CMS"
sum_of_masses = sum(at_weights)
print "Total mass ==>",sum_of_masses
x_center = 0.
y_center = 0.
z_center = 0.
for i in range(at_number):
	x_center += float(x_vals[i]) * at_weights[i]
	y_center += float(y_vals[i]) * at_weights[i]
	z_center += float(z_vals[i]) * at_weights[i]
x_center = x_center/sum_of_masses
y_center = y_center/sum_of_masses
z_center = z_center/sum_of_masses
print "Center of xyz ==>",x_center,y_center,z_center
print "Now moving CMS to origin"
new_xyzName = xyz_name.split(".")[0]+"_cmsOriginated.xyz"
print "File name is:", new_xyzName
new_xyz = open(new_xyzName,"w")
new_xyz.write(str(at_number)+"\n\n")
for i in range(at_number):
	new_x = str(float(x_vals[i]) - x_center)
	new_y = str(float(y_vals[i]) - y_center)
	new_z = str(float(z_vals[i]) - z_center)
	new_xyz.write(at_list[i]+"\t"+new_x+"\t"+new_y+"\t"+new_z+"\n")
print "All finished."