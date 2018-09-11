#!/usr/bin/env python2
import os
from pprint import pprint
from prettytable import PrettyTable
import sys
from functions_of_caspesa import (cmdline,check_analysis,
generate_cellfile_fcaspesa,get_energy_fcaspesa)

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: fcaspesa_analyser.py sym_tol"
    exit(0)
else:
    sym_tol = sys.argv[1]

Analysis_dir = "Analysis"

check_analysis(Analysis_dir)

filelist_pseudo = cmdline("find . -iname r333_*.xyz").split("\n")[:-1]
filelist_all = []
xyz_adress = []
"""
address: address is for 333 repeated xyz
xyz_adress: xyz_adress is for one unit cell 
"""

for address in filelist_pseudo:
	address = address.split("./")
	address = address[1]
	dummy = address.split("r333_")
	dummy2 = ""
	for i in xrange(len(dummy)):
		dummy2 += dummy[i]
	xyz_adress.append(dummy2)

#Opening Analysis Directory
os.system("mkdir "+Analysis_dir)
#Opening other directories for all xyz files
Analysis_folder_paths = []
Analysis_xyz_paths = []
energy_dict = {}
for i in xrange(len(xyz_adress)):
	#taking structure name
	name_without_xyz = xyz_adress[i].split(".xyz")[0].split("/")[-1]
	#Generating folders
	xyzfolder_path = Analysis_dir+"/"+name_without_xyz
	Analysis_folder_paths.append(xyzfolder_path)
	os.system("mkdir -p "+xyzfolder_path)
	#Copying the files
	copy_command = "cp -r "+xyz_adress[i]+" "+Analysis_folder_paths[i]
	RepAdress = xyz_adress[i].split("/")
	RepAdressFull = ""
	for j in range(len(RepAdress)-1):
		RepAdressFull += RepAdress[j] + "/"
	RepAdressFull += "r333_"+name_without_xyz+".xyz"
	copy_command_333 = "cp -r "+RepAdressFull+" "+Analysis_folder_paths[i]
	Analysis_xyz_paths.append(Analysis_folder_paths[i]+"/"+xyz_adress[i].split("/")[-1])
	os.system(copy_command)
	os.system(copy_command_333)
	#Generating the cell_file for xyz2cif
#	print xyz_adress[i]
	generate_cellfile_fcaspesa(xyzfolder_path,name_without_xyz)
	#Getting energy
	get_energy_fcaspesa(xyzfolder_path,name_without_xyz,energy_dict)

energy_sorted = sorted(energy_dict.items(), key=lambda t: t[1], reverse=True)

table = PrettyTable([
"Address",
"Energy",
"Volume",
"Symmetry Tolerance",
"Symmetry"
])
#Finding symmetries and creating cif files
base_directory = cmdline("pwd").rstrip("\n")
for i in xrange(len(energy_sorted)):
	print("Processing "+str(i)+" of "+ str(len(energy_sorted))
		+" name-> "+ energy_sorted[i][0])
	dummy_tol = sym_tol
	#taking working directory to change
	work_path_raw = energy_sorted[i][0].split("/")
	work_path_raw = work_path_raw[:-1]
	#xyz file name without xyz extension
	xyz_file_name = work_path_raw[-1]
	work_path_processed = ""
	for j in xrange(len(work_path_raw)):
		work_path_processed += work_path_raw[j]+"/"
	#now i can change working directory and execute the xyz2cif
	os.chdir(work_path_processed)
	if(float(energy_sorted[i][1])!=0.):
		sym_res = cmdline("xyz2cif.py "+xyz_file_name+".xyz cell_file "+sym_tol+" "
			+xyz_file_name+".cif").rstrip("\n")
		while sym_res[:5] != "Space":
			print "\t Tolerance Decreasing to:",float(dummy_tol)*0.9
			dummy_tol = float(dummy_tol)*0.9
			sym_res = cmdline("xyz2cif.py "+xyz_file_name+".xyz cell_file "+str(dummy_tol)+" "
				+xyz_file_name+".cif").rstrip("\n")
			if(float(dummy_tol)<0.1):
				sym_res = "Space must be planar or problematic, sym wont work"
	else:
		sym_res = "E=0,wont look for sym"
	volume = cmdline("get_volume.py cell_file").rstrip("\n") + " Ang^3"
	table.add_row([energy_sorted[i][0],energy_sorted[i][1],volume,str(dummy_tol),sym_res.rstrip(" ")])
	os.chdir(base_directory)

print(table)

Analysis_file = open(Analysis_dir+".txt","w")
Analysis_file.write(str(table)+"\n")
Analysis_file.close()
#os.system("cat "+Analysis_dir+".txt")
for i in xrange(len(energy_sorted)):
	os.system("cat "+energy_sorted[i][0]+" >> "+Analysis_dir+"/all.xyz")
	RepAdress = energy_sorted[i][0].split("/")
	RepAdressFull = ""
	for j in range(len(RepAdress)-1):
		RepAdressFull += RepAdress[j] + "/"
	RepAdressFull += "r333_"+RepAdress[-1]
	os.system("cat "+RepAdressFull+" >> "+Analysis_dir+"/all_333.xyz")
