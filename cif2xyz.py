#!/usr/bin/env python2
from ase import Atoms
#from ase.build import fcc111, add_adsorbate
import ase.io
import sys
import numpy as np
from atomnum2name import atomnum2name

if len(sys.argv)<3 or len(sys.argv)>3:
	print """Arguments are wrong! Right usage:
python2 cif2xyz.py cif_name xyz_name"""
	exit(0)
else:
	cif_name = sys.argv[1]
	xyz_name = sys.argv[2]

np.set_printoptions(suppress=True)

datas = ase.io.read(cif_name,format="cif")

#Taking atomnumbers and position data
mol_atnumberlist = datas.get_atomic_numbers()
mol_cell = datas.get_cell()
print mol_cell
mol_positions = datas.get_positions()
mol_totalatom = datas.get_number_of_atoms()
np.set_printoptions(suppress=True)
#Converting numbers to atom names
at_name_list = []
for number in mol_atnumberlist:
	at_name_list.append(atomnum2name[number])
#Preparing cell data for xyz file both in angstrom and bohr
cell_data_angstrom = []
for i in xrange(len(mol_cell)):
	for j in xrange(len(mol_cell[i])):
		cell_data_angstrom.append(mol_cell[i][j])
cell_data_bohr = []
for cell_elem in cell_data_angstrom:
	cell_data_bohr.append(cell_elem*1.889725989)
#Now i can easily write an xyz file
xyz_file = open(xyz_name,"w")
xyz_file.write(str(mol_totalatom)+"\n")
xyz_file.write("Cell Angstrom="+str(cell_data_angstrom)+
	" Cell Bohr="+str(cell_data_bohr)+"\n")
for i in xrange(len(mol_positions)):
	xyz_file.write(str(at_name_list[i])+"\t"+str(mol_positions[i])[1:-1]+"\n")
cell_file = open("cell_file","w")
for i in xrange(3):
	a = str(cell_data_angstrom[(i*3)+0])
	b = str(cell_data_angstrom[(i*3)+1])
	c = str(cell_data_angstrom[(i*3)+2])
	cell_file.write(a+"\t"+b+"\t"+c+"\n")
cell_file.close()