import os
import subprocess
from subprocess import PIPE, Popen
import operator
from pprint import pprint
import math

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def center_it(file_name,coord_val):
	xyz_file = open(file_name,"r")
	xyz_data = xyz_file.readlines()
	#first x coordinates
	coord = []
	for i in range(2,len(xyz_data)):
		coord.append(float(xyz_data[i].rstrip("\n").split()[coord_val]))
	coord_diff = max(coord) - min(coord)
	coord_add_val =  (-1.)*(min(coord) + (coord_diff / 2.))
	coord_add_list = [coord_add_val]*len(coord)
	coord_new = map(sum,zip(coord,coord_add_list))
	xyz_file.close()
	return coord_new

def get_atname(file_name):
	xyz_file = open(file_name,"r")
	xyz_data = xyz_file.readlines()
	atnames = []
	for i in range(2,len(xyz_data)):
		atnames.append(xyz_data[i].split()[0])
	return atnames

xyz_name_to_ls = "r333"
ls_result = (str(cmdline("ls "+xyz_name_to_ls+"*.xyz")).split("\n"))
ls_result = filter(None, ls_result)

for i in range(len(ls_result)):
	#1 for x, 2 for y, 3 for z
	x_vals = center_it(ls_result[i],1)
	y_vals = center_it(ls_result[i],2)
	z_vals = center_it(ls_result[i],3)
	at_names = get_atname(ls_result[i])
	xyz_file = open(ls_result[i],"r")
	atom_count = str(int(xyz_file.readline().rstrip("\n")))
	energy = str(float(xyz_file.readline().split("=")[1].split()[0].rstrip("\n")))
	xyz_file.close()
	centered_file = open("processed_"+ls_result[i],"w")
	centered_file.write(atom_count+"\n")
	centered_file.write("Energy = "+energy+"\n")
	for i in range(int(atom_count)):
		centered_file.write(at_names[i]+"\t"+str(x_vals[i])+"\t"+str(y_vals[i])+"\t"+str(z_vals[i])+"\n")
	centered_file.close()


