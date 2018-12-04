#!/usr/bin/env python2
from subprocess import PIPE, Popen
import os
import sys

def cmdline(command):
    process = Popen(
        args=command,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        shell=True,
#        close_fds=True,
#        bufsize=-1
    )
    return process.communicate()[0]

def check_analysis(Analysis_dir):
	ls = cmdline("ls")
	if Analysis_dir in ls:
		print """An old analysis folder already exist."""
		print """Do you want to remove the old files and execute a new analysis(Y/N)"""
		sys.stdin = open('/dev/tty')
		ans = raw_input()
		if ans=="Y" or ans=="y":
			os.system("rm -rf "+Analysis_dir+" "+Analysis_dir+".txt")
			print "Old files has been removed"
		elif ans=="N" or ans=="n":
			print "Exiting now.."
			exit(0)
		else:
			print "Incorrect input...Exiting"
			exit(0)

def generate_cellfile(xyzfolder_path,name_without_xyz):
	exact_path=xyzfolder_path+"/"+name_without_xyz+".xyz"
	file = open(exact_path,"r")
	cell_raw = file.readline()
	cell_raw = file.readline()
	cell_processed = cell_raw.split()[7:]
	cell1 = cell_processed[0][2:-1]
	cell2 = cell_processed[1][:-1]
	cell3 = cell_processed[2].split("[")[0][:-1]
	cell4 = cell_processed[2].split("[")[1][:-1]
	cell5 = cell_processed[3][:-1]
	cell6 = cell_processed[4].split("[")[0][:-1]
	cell7 = cell_processed[4].split("[")[1][:-1]
	cell8 = cell_processed[5][:-1]
	cell9 = cell_processed[6][:-1]
	file.close()
	cell_file = open(xyzfolder_path+"/cell_file","w")
	cell_file.write(
		str(cell1)+"\t"+
		str(cell2)+"\t"+
		str(cell3)+"\n"+
		str(cell4)+"\t"+
		str(cell5)+"\t"+
		str(cell6)+"\n"+
		str(cell7)+"\t"+
		str(cell8)+"\t"+
		str(cell9)
		)
	cell_file.close()

def generate_cellfile_fcaspesa(xyzfolder_path,name_without_xyz):
	exact_path=xyzfolder_path+"/"+name_without_xyz+".xyz"
	file = open(exact_path,"r")
	cell_raw = file.readline()
	cell_raw = file.readline()
	cell_processed = cell_raw.split()
	cell1 = cell_processed[-9]
	cell2 = cell_processed[-8]
	cell3 = cell_processed[-7]
	cell4 = cell_processed[-6]
	cell5 = cell_processed[-5]
	cell6 = cell_processed[-4]
	cell7 = cell_processed[-3]
	cell8 = cell_processed[-2]
	cell9 = cell_processed[-1]
	file.close()
	cell_file = open(xyzfolder_path+"/cell_file","w")
	cell_file.write(
		str(cell1)+"\t"+
		str(cell2)+"\t"+
		str(cell3)+"\n"+
		str(cell4)+"\t"+
		str(cell5)+"\t"+
		str(cell6)+"\n"+
		str(cell7)+"\t"+
		str(cell8)+"\t"+
		str(cell9)
		)
	cell_file.close()

def get_energy(xyzfolder_path,name_without_xyz,energy_dict):
	exact_path=xyzfolder_path+"/"+name_without_xyz+".xyz"
	file = open(exact_path,"r")
	energy_raw = file.readline()
	energy_raw = file.readline()
	energy_splitted = energy_raw.split()
	energy_dict[exact_path] = energy_splitted[1]

def get_energy_fcaspesa(xyzfolder_path,name_without_xyz,energy_dict):
	exact_path=xyzfolder_path+"/"+name_without_xyz+".xyz"
	file = open(exact_path,"r")
	energy_raw = file.readline()
	energy_raw = file.readline()
	energy_splitted = energy_raw.split()
	if energy_splitted[1] == "Cell":
		energy_dict[exact_path] = float(energy_splitted[0].split("=")[-1])
	else:
		energy_dict[exact_path] = float(energy_splitted[1])

def check_analysis_qe(Analysis_dir):
	directories = cmdline("find . -name "+Analysis_dir).split("\n")
	if directories[0]!='':
		print """Older Analysis folders have been found!
Do you want to remove the old files and execute a new analysis(Y/N)"""
		ans = raw_input()
		if ans=="Y" or ans=="y":
			for i in xrange(len(directories)):
				os.system("rm -rf "+str(directories[i]))
			os.system("rm -rf "+Analysis_dir+".txt")
			print "Old files has been removed"
		elif ans=="N" or ans=="n":
			print "Exiting now.."
			exit(0)
		else:
			print "Incorrect input...Exiting"
			exit(0)
