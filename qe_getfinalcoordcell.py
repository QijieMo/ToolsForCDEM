#!/usr/bin/env python2
import sys
import os
from pprint import pprint
from functions_of_caspesa import (cmdline)

if len(sys.argv)<4 or len(sys.argv)>4:
    print "Arguments are wrong.\n" \
          "Correct usage: qe_getfinalcoordcell.py qe_outfile xyz_name atom_number"
    exit(0)
else:
	qe_out_address = sys.argv[1]
	xyz_name = sys.argv[2]
	at_number = sys.argv[3]

coord_line_numbers = cmdline("grep -nr -i \"ATOMIC_POSITIONS\" "+qe_out_address).split("\n")
cell_line_numbers = cmdline("grep -nr -i \"CELL_PARAMETERS\" "+qe_out_address).split("\n")
coord_line_numbers.remove('')
cell_line_numbers.remove('')
line_with_coordstring = coord_line_numbers[-1]
line_with_cellstring = cell_line_numbers[-1]

#Finding the units of the data
angstrom = "angstrom"
bohr = "bohr"
crystal = "crystal"
alat = "alat"

#Firstly for cell
cell_is_bohr = line_with_cellstring.find(bohr)
cell_is_ang = line_with_cellstring.find(angstrom)
cell_is_alat = line_with_cellstring.find(alat)

cell_file = open("cell_file","w")

if cell_is_ang!=-1:
	begin_line = str(int(line_with_cellstring.split(":")[0])+1)
	end_line = str(int(line_with_cellstring.split(":")[0])+3)
	command = "awk 'NR >="+begin_line+" && NR <= "+end_line+"' "+qe_out_address
	cell_data = cmdline(command).split()
	cell_file.write(cell_data[0]+"\t"+cell_data[1]+"\t"+cell_data[2]+"\n")
	cell_file.write(cell_data[3]+"\t"+cell_data[4]+"\t"+cell_data[5]+"\n")
	cell_file.write(cell_data[6]+"\t"+cell_data[7]+"\t"+cell_data[8]+"\n")

if cell_is_bohr!=-1:
	begin_line = str(int(line_with_cellstring.split(":")[0])+1)
	end_line = str(int(line_with_cellstring.split(":")[0])+3)
	command = "awk 'NR >="+begin_line+" && NR <= "+end_line+"' "+qe_out_address
	cell_data = cmdline(command).split()
	for i in xrange(len(cell_data)):
		cell_data[i] = str(float(cell_data[i])*0.529177249)
	cell_file.write(cell_data[0]+"\t"+cell_data[1]+"\t"+cell_data[2]+"\n")
	cell_file.write(cell_data[3]+"\t"+cell_data[4]+"\t"+cell_data[5]+"\n")
	cell_file.write(cell_data[6]+"\t"+cell_data[7]+"\t"+cell_data[8]+"\n")

if cell_is_alat!=-1:
	begin_line = str(int(line_with_cellstring.split(":")[0])+1)
	end_line = str(int(line_with_cellstring.split(":")[0])+3)
	command = "awk 'NR >="+begin_line+" && NR <= "+end_line+"' "+qe_out_address
	cell_data = cmdline(command).split()
	alat_value = float(line_with_cellstring.split("alat=")[-1][:-1].lstrip(" "))
	alat_to_ang = alat_value/1.889725989
	for i in xrange(len(cell_data)):
		cell_data[i] = str(float(cell_data[i])*alat_to_ang)
	cell_file.write(cell_data[0]+"\t"+cell_data[1]+"\t"+cell_data[2]+"\n")
	cell_file.write(cell_data[3]+"\t"+cell_data[4]+"\t"+cell_data[5]+"\n")
	cell_file.write(cell_data[6]+"\t"+cell_data[7]+"\t"+cell_data[8]+"\n")

cell_file.close()

#Now for coord file
coord_is_ang = line_with_coordstring.find(angstrom)
filename = qe_out_address.split("/")[-1].split(".")[0]+"_final.xyz"
coord_file = open(filename,"w")
if coord_is_ang!=-1:
	coord_file.write(str(at_number)+"\n\n")
	begin_line = str(int(line_with_coordstring.split(":")[0])+1)
	end_line = str(int(line_with_coordstring.split(":")[0])+int(at_number))
	command = "awk 'NR >="+begin_line+" && NR <= "+end_line+"' "+qe_out_address
	coord_data = cmdline(command)
	coord_file.write(coord_data)
else:
	print "Coord File is not in Angstrom"
	
coord_file.close()

