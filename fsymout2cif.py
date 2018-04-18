#!/usr/bin/env python2
import subprocess
from subprocess import PIPE, Popen
import string
from pprint import pprint

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def fsymout2cif(at_types,cif_name):
	#getting the cif start line
	startline = cmdline("grep -nr 'data_findsym-output' findsym.out")
	startline = startline.split(":")[0]
	#getting the starting line number of coordinates
	coord_start = cmdline("grep -nr '_atom_site_occupancy' findsym.out")
	coord_start = coord_start.split(":")[0]
	#taking the lines to fix
	lines_without_atnames = cmdline("awk 'FNR>"+str(coord_start)+"' findsym.out")
	lines_without_atnames = lines_without_atnames.split("\n")
	#removing empty lines
	lines_without_atnames = [x for x in lines_without_atnames if x != '' and x != ' ']
	#letter dictionary
	letter_list = dict(zip(string.ascii_uppercase, range(0,26)))
	#now the fixing part
	lines_with_atnames = []
	for i in xrange(len(lines_without_atnames)):
		dummyarr = lines_without_atnames[i].split()
		#Changing letter to element of firts element
		first_elem = at_types[letter_list[dummyarr[0][0]]]+dummyarr[0][1:]
		dummyarr[0] = first_elem
		#Changing letter of the second element
		second_elem = at_types[letter_list[dummyarr[1]]]
		dummyarr[1] = second_elem
		lines_with_atnames.append(dummyarr)
	#Now we have a corrected cif elements
	lines_until_coord = cmdline("awk 'FNR>="+str(startline)+" && FNR<="+str(coord_start)+"' findsym.out")
	lines_until_coord = lines_until_coord.split("\n")[:-1]
	#Lets write it
	cif_file = open(cif_name,"w")
	for i in xrange(len(lines_until_coord)):
		cif_file.write(lines_until_coord[i]+"\n")
	for i in xrange(len(lines_with_atnames)):
		for j in xrange(len(lines_with_atnames[i])):
			cif_file.write(lines_with_atnames[i][j]+"\t")
		cif_file.write("\n")
	cif_file.close()
	