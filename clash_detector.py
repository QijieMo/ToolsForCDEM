#!/usr/bin/env python2
import os
from functions_of_caspesa import (cmdline)
from pprint import pprint
import numpy as np
import sys

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: clash_detector.py clash_thr(in angstrom)"
    exit(0)
else:
    thr = float(sys.argv[1])

print """This script finds all xyz files beneath this
folder and inspect them for possible atomic clash
RESULTS CAN BE FOUND IN THE clash_result.txt FILE
PLEASE PLEASE!!!! REMOVE ANALYSIS FOLDER FIRST!!(of course if it exist)"""

clash_file = open("clash_result.txt","w")

xyz_list = cmdline("find . -iname '*.xyz'").split("\n")[:-1]
print "I found ",len(xyz_list)," xyz file here"
print "Now i am checking them for a clash. It may take time.."

def distance(data1,data2):
	for i in range(1,4):
		data1[i] = float(data1[i])
		data2[i] = float(data2[i])
	return np.sqrt((data1[1]-data2[1])**2 +
	  (data1[2]-data2[2])**2 +
	  (data1[3]-data2[3])**2)

def check_clash(xyz_data,addr):
	#Lets remove newlines and split columns
	for i in range(len(xyz_data)):
		xyz_data[i] = xyz_data[i].rstrip("\n")
		xyz_data[i] = xyz_data[i].split()
	for i in range(len(xyz_data)):
		for j in range(i+1,len(xyz_data)):
			dist = distance(xyz_data[i],xyz_data[j])
			if dist<thr:
				print "I FOUND CLASH IN FILE:"
				clash_file.write("I FOUND CLASH IN FILE:\n")
				print addr
				clash_file.write(addr+"\n")
				print "between atom ",str(i),"and",str(j)
				clash_file.write("between atom "+str(i)+" and "+str(j)+"\n")
				print "Distance between "+xyz_data[i][0]+" and "+xyz_data[j][0]+" is "+str(dist)+"\n"


for addr in xyz_list:
	xyz_file = open(addr,"r")
	xyz_data = xyz_file.readlines()[2:]
	check_clash(xyz_data,addr)
	xyz_file.close()
	
clash_file.close()