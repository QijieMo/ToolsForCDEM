#!/usr/bin/env python2
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
#Taking arguments with error control
if len(sys.argv)<3 or len(sys.argv)>3:
    print "Arguments are wrong.\n" \
          "Correct usage: xyz_visualizer.py xyz_file cell_file"
    exit(0)
else:
    XyzFileName = sys.argv[1]
    cell_file = sys.argv[2]

def at_color(at_name):
	if at_name=='H':
		return '#FFFFFF'
	if at_name=='He':
		return '#D9FFFF'
	if at_name=='Li':
		return '#CC80FF'
	if at_name=='Be':
		return '#C2FF00'
	if at_name=='B':
		return '#FFB5B5'
	if at_name=='C':
		return '#909090'
	if at_name=='N':
		return '#3050F8'
	if at_name=='O':
		return '#FF0D0D'
	if at_name=='F':
		return '#90E050'
	if at_name=='Ne':
		return '#B3E3F5'
	if at_name=='Na':
		return '#AB5CF2'
	if at_name=='Mg':
		return '#8AFF00'
	if at_name=='Al':
		return '#BFA6A6'
	if at_name=='Si':
		return '#F0C8A0'
	if at_name=='P':
		return '#FF8000'
	if at_name=='S':
		return '#FFFF30'
	if at_name=='Cl':
		return '#1FF01F'
	if at_name=='Ar':
		return '#80D1E3'
	if at_name=='K':
		return '#8F40D4'
	if at_name=='Ca':
		return '#3DFF00'
	if at_name=='Sc':
		return '#E6E6E6'
	if at_name=='Ti':
		return '#BFC2C7'
	if at_name=='V':
		return '#A6A6AB'
	if at_name=='Cr':
		return '#8A99C7'
	if at_name=='Mn':
		return '#9C7AC7'
	if at_name=='Fe':
		return '#E06633'
	if at_name=='Co':
		return '#F090A0'
	if at_name=='Ni':
		return '#50D050'
	if at_name=='Cu':
		return '#C88033'
	if at_name=='Zn':
		return '#7D80B0'
	if at_name=='Ga':
		return '#C28F8F'
	if at_name=='Ge':
		return '#668F8F'
	if at_name=='As':
		return '#BD80E3'
	if at_name=='Se':
		return '#FFA100'
	if at_name=='Br':
		return '#A62929'
	if at_name=='Kr':
		return '#5CB8D1'
	if at_name=='Rb':
		return '#702EB0'
	if at_name=='Sr':
		return '#00FF00'
	if at_name=='Y':
		return '#94FFFF'
	if at_name=='Zr':
		return '#94E0E0'
	if at_name=='Nb':
		return '#73C2C9'
	if at_name=='Mo':
		return '#54B5B5'
	if at_name=='Tc':
		return '#3B9E9E'
	if at_name=='Ru':
		return '#248F8F'
	if at_name=='Rh':
		return '#0A7D8C'
	if at_name=='Pd':
		return '#006985'
	if at_name=='Ag':
		return '#C0C0C0'
	if at_name=='Cd':
		return '#FFD98F'
	if at_name=='In':
		return '#A67573'
	if at_name=='Sn':
		return '#668080'
	if at_name=='Sb':
		return '#9E63B5'
	if at_name=='Te':
		return '#D47A00'
	if at_name=='I':
		return '#940094'
	if at_name=='Xe':
		return '#429EB0'
	if at_name=='Cs':
		return '#57178F'
	if at_name=='Ba':
		return '#00C900'
	if at_name=='La':
		return '#70D4FF'
	if at_name=='Ce':
		return '#FFFFC7'
	if at_name=='Pr':
		return '#D9FFC7'
	if at_name=='Nd':
		return '#C7FFC7'
	if at_name=='Pm':
		return '#A3FFC7'
	if at_name=='Sm':
		return '#8FFFC7'
	if at_name=='Eu':
		return '#61FFC7'
	if at_name=='Gd':
		return '#45FFC7'
	if at_name=='Tb':
		return '#30FFC7'
	if at_name=='Dy':
		return '#1FFFC7'
	if at_name=='Ho':
		return '#00FF9C'
	if at_name=='Er':
		return '#00E675'
	if at_name=='Tm':
		return '#00D452'
	if at_name=='Yb':
		return '#00BF38'
	if at_name=='Lu':
		return '#00AB24'
	if at_name=='Hf':
		return '#4DC2FF'
	if at_name=='Ta':
		return '#4DA6FF'
	if at_name=='W':
		return '#2194D6'
	if at_name=='Re':
		return '#267DAB'
	if at_name=='Os':
		return '#266696'
	if at_name=='Ir':
		return '#175487'
	if at_name=='Pt':
		return '#D0D0E0'
	if at_name=='Au':
		return '#FFD123'
	if at_name=='Hg':
		return '#B8B8D0'
	if at_name=='Tl':
		return '#A6544D'
	if at_name=='Pb':
		return '#575961'
	if at_name=='Bi':
		return '#9E4FB5'
	if at_name=='Po':
		return '#AB5C00'
	if at_name=='At':
		return '#754F45'
	if at_name=='Rn':
		return '#428296'
	if at_name=='Fr':
		return '#420066'
	if at_name=='Ra':
		return '#007D00'
	if at_name=='Ac':
		return '#70ABFA'
	if at_name=='Th':
		return '#00BAFF'
	if at_name=='Pa':
		return '#00A1FF'
	if at_name=='U':
		return '#008FFF'
	if at_name=='Np':
		return '#0080FF'
	if at_name=='Pu':
		return '#006BFF'
	if at_name=='Am':
		return '#545CF2'
	if at_name=='Cm':
		return '#785CE3'
	if at_name=='Bk':
		return '#8A4FE3'
	if at_name=='Cf':
		return '#A136D4'
	if at_name=='Es':
		return '#B31FD4'
	if at_name=='Fm':
		return '#B31FBA'
	if at_name=='Md':
		return '#B30DA6'
	if at_name=='No':
		return '#BD0D87'
	if at_name=='Lr':
		return '#C70066'
	if at_name=='Rf':
		return '#CC0059'
	if at_name=='Db':
		return '#D1004F'
	if at_name=='Sg':
		return '#D90045'
	if at_name=='Bh':
		return '#E00038'
	if at_name=='Hs':
		return '#E6002E'
	if at_name=='Mt':
		return '#EB0026'

def at_size(at_name,multiplier):
	if at_name=='He':  
		return multiplier*0.49
	if at_name=='Ne':  
		return multiplier*0.51
	if at_name=='F':  
		return multiplier*0.57
	if at_name=='O':  
		return multiplier*0.65
	if at_name=='N':  
		return multiplier*0.75
	if at_name=='H':  
		return multiplier*0.79
	if at_name=='Ar':  
		return multiplier*0.88
	if at_name=='C':  
		return multiplier*0.91
	if at_name=='Cl':  
		return multiplier*0.97
	if at_name=='Kr':  
		return multiplier*1.03
	if at_name=='S':  
		return multiplier*1.09
	if at_name=='Br':  
		return multiplier*1.12
	if at_name=='B':  
		return multiplier*1.17
	if at_name=='Se':  
		return multiplier*1.22
	if at_name=='P':  
		return multiplier*1.23
	if at_name=='Xe':  
		return multiplier*1.24
	if at_name=='I':  
		return multiplier*1.32
	if at_name=='As':  
		return multiplier*1.33
	if at_name=='Rn':  
		return multiplier*1.34
	if at_name=='Be':  
		return multiplier*1.40
	if at_name=='Te':  
		return multiplier*1.42
	if at_name=='At':  
		return multiplier*1.43
	if at_name=='Si':  
		return multiplier*1.46
	if at_name=='Ge':  
		return multiplier*1.52
	if at_name=='Po':  
		return multiplier*1.53
	if at_name=='Sb':  
		return multiplier*1.53
	if at_name=='Zn':  
		return multiplier*1.53
	if at_name=='Cu':  
		return multiplier*1.57
	if at_name=='Ni':  
		return multiplier*1.62
	if at_name=='Bi':  
		return multiplier*1.63
	if at_name=='Co':  
		return multiplier*1.67
	if at_name=='Cd':  
		return multiplier*1.71
	if at_name=='Sn':  
		return multiplier*1.72
	if at_name=='Fe':  
		return multiplier*1.72
	if at_name=='Mg':  
		return multiplier*1.72
	if at_name=='Ag':  
		return multiplier*1.75
	if at_name=='Hg':  
		return multiplier*1.76
	if at_name=='Pd':  
		return multiplier*1.79
	if at_name=='Mn':  
		return multiplier*1.79
	if at_name=='Au':  
		return multiplier*1.79
	if at_name=='Ga':  
		return multiplier*1.81
	if at_name=='Pb':  
		return multiplier*1.81
	if at_name=='Al':  
		return multiplier*1.82
	if at_name=='Pt':  
		return multiplier*1.83
	if at_name=='Rh':  
		return multiplier*1.83
	if at_name=='Cr':  
		return multiplier*1.85
	if at_name=='Ir':  
		return multiplier*1.87
	if at_name=='Ac':  
		return multiplier*1.88
	if at_name=='Ru':  
		return multiplier*1.89
	if at_name=='V':  
		return multiplier*1.92
	if at_name=='Os':  
		return multiplier*1.92
	if at_name=='Tc':  
		return multiplier*1.95
	if at_name=='Re':  
		return multiplier*1.97
	if at_name=='In':  
		return multiplier*2.00
	if at_name=='Ti':  
		return multiplier*2.00
	if at_name=='Mo':  
		return multiplier*2.01
	if at_name=='W':  
		return multiplier*2.02
	if at_name=='Li':  
		return multiplier*2.05
	if at_name=='Nb':  
		return multiplier*2.08
	if at_name=='Tl':  
		return multiplier*2.08
	if at_name=='Sc':  
		return multiplier*2.09
	if at_name=='Ta':  
		return multiplier*2.09
	if at_name=='Hf':  
		return multiplier*2.16
	if at_name=='Zr':  
		return multiplier*2.16
	if at_name=='Na':  
		return multiplier*2.23
	if at_name=='Ca':  
		return multiplier*2.23
	if at_name=='Lu':  
		return multiplier*2.25
	if at_name=='Y':  
		return multiplier*2.27
	if at_name=='Yb':  
		return multiplier*2.40
	if at_name=='Tm':  
		return multiplier*2.42
	if at_name=='Sr':  
		return multiplier*2.45
	if at_name=='Er':  
		return multiplier*2.45
	if at_name=='Ho':  
		return multiplier*2.47
	if at_name=='Dy':  
		return multiplier*2.49
	if at_name=='Tb':  
		return multiplier*2.51
	if at_name=='Gd':  
		return multiplier*2.54
	if at_name=='Eu':  
		return multiplier*2.56
	if at_name=='Sm':  
		return multiplier*2.59
	if at_name=='Pm':  
		return multiplier*2.62
	if at_name=='Nd':  
		return multiplier*2.64
	if at_name=='Pr':  
		return multiplier*2.67
	if at_name=='Ce':  
		return multiplier*2.70
	if at_name=='La':  
		return multiplier*2.74
	if at_name=='K':  
		return multiplier*2.77
	if at_name=='Ba':  
		return multiplier*2.78
	if at_name=='Rb':  
		return multiplier*2.98
	if at_name=='Cs':  
		return multiplier*3.34

def draw_bond(at_names,x_coords,y_coords,z_coords):
	dummy = len(x_coords)
	for i in range(dummy):
		for j in range(i+1,dummy):
			distance = math.sqrt((x_coords[i]-x_coords[j])**2+
				(y_coords[i]-y_coords[j])**2+
				(z_coords[i]-z_coords[j])**2)
			if distance<1.6:
				ax.plot([x_coords[i],x_coords[j]],[y_coords[i],y_coords[j]],[z_coords[i],z_coords[j]],color = 'g')

def draw_unitcell(data):
	origin = [0.,0.,0.]
	origin = np.array(origin)
	ax.plot([0,data[0][0]],[0.,data[0][1]],[0.,data[0][2]],color = 'r')
	ax.plot([0,data[1][0]],[0.,data[1][1]],[0.,data[1][2]],color = 'r')
	ax.plot([0,data[2][0]],[0.,data[2][1]],[0.,data[2][2]],color = 'r')
	ax.plot([data[0][0],data[0][0]+data[1][0]],[data[0][1],data[0][1]+data[1][1]],[data[0][2],data[0][2]+data[1][2]],color = 'r')
	ax.plot([data[0][0],data[0][0]+data[2][0]],[data[0][1],data[0][1]+data[2][1]],[data[0][2],data[0][2]+data[2][2]],color = 'r')
	ax.plot([(data[0]+data[1])[0],(data[0]+data[2]+data[1])[0]],[(data[0]+data[1])[1],(data[0]+data[2]+data[1])[1]],[(data[0]+data[1])[2],(data[0]+data[2]+data[1])[2]],color = 'r')
	ax.plot([(data[0]+data[2])[0],(data[0]+data[2]+data[1])[0]],[(data[0]+data[2])[1],(data[0]+data[2]+data[1])[1]],[(data[0]+data[2])[2],(data[0]+data[2]+data[1])[2]],color = 'r')
	ax.plot([(data[1]+data[2])[0],(data[0]+data[2]+data[1])[0]],[(data[1]+data[2])[1],(data[0]+data[2]+data[1])[1]],[(data[1]+data[2])[2],(data[0]+data[2]+data[1])[2]],color = 'r')
	ax.plot([(data[1])[0],(data[1]+data[2])[0]],[(data[1])[1],(data[1]+data[2])[1]],[(data[1])[2],(data[1]+data[2])[2]],color = 'r')
	ax.plot([(data[2])[0],(data[1]+data[2])[0]],[(data[2])[1],(data[1]+data[2])[1]],[(data[2])[2],(data[1]+data[2])[2]],color = 'r')
	ax.plot([(data[2])[0],(data[0]+data[2])[0]],[(data[2])[1],(data[0]+data[2])[1]],[(data[2])[2],(data[0]+data[2])[2]],color = 'r')
	ax.plot([(data[1])[0],(data[0]+data[1])[0]],[(data[1])[1],(data[0]+data[1])[1]],[(data[1])[2],(data[0]+data[1])[2]],color = 'r')

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
#ax._axis3don = False
xyz_file = open(XyzFileName,"r").readlines()
at_names = []
x_coords = []
y_coords = []
z_coords = []
#Lets remove first 2 line to get only the data
cell_raw = open(cell_file,"r").readlines()
cell_arr = np.zeros(9).reshape(3,3)
for i in range(len(cell_raw)):
	cell_raw[i] = cell_raw[i].rstrip("\n").split()
	for j in range(3):
		cell_arr[i][j] = cell_raw[i][j]

print cell_arr
xyz_file = xyz_file[2:]
#Writing data to arrays
size = []
colors = []
for i in range(len(xyz_file)):
    xyz_file[i] = xyz_file[i].rstrip("\n")
    xyz_file[i] = xyz_file[i].split()
    at_names.append(xyz_file[i][0])
    x_coords.append(float(xyz_file[i][1]))
    y_coords.append(float(xyz_file[i][2]))
    z_coords.append(float(xyz_file[i][3]))
    size.append(at_size(at_names[i],1000))
    colors.append(at_color(at_names[i]))

draw_unitcell(cell_arr)

print(colors)
ax.set_facecolor((0., 0., 0.))
ax.scatter(x_coords,y_coords,z_coords,s=size,color=colors)
draw_bond(at_names,x_coords,y_coords,z_coords)
plt.show()