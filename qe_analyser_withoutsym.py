#!/usr/bin/env python2
import os
from pprint import pprint
from functions_of_caspesa import (cmdline,check_analysis_qe)
import sys
from prettytable import PrettyTable

print """QE-Analyser v1
I recommend you to use this script with the vesions above 6.0
If you execute this script on a big folder, functions may take several minutes.."""

Analysis_dir = "Analysis"
check_analysis_qe(Analysis_dir)

qe_outandver_list = cmdline("grep --exclude=*.py --binary-files=text -Ro \"PWSCF v[\.0-9]*\" *").split("\n")
qe_outandver_list.remove("")

qe_outandver_dict = {}
for i in xrange(len(qe_outandver_list)):
	qe_outandver_dict[qe_outandver_list[i].split()[0].split(":")[0]] = qe_outandver_list[i].split()[1]

print "Found QE out file count:",len(qe_outandver_dict)
print "Checking if they are finished or not.."
print "Extracting properties from data files.."
is_finished = {}
how_many_atom = {}
how_many_diffrent_atom = {}
address_vs_volume = {}
address_vs_energy = {}
address_vs_name = {}
address_vs_kincutoff = {}
address_vs_chdencutoff = {}
address_vs_kpoint = {}
address_vs_version ={}
has_error = {}
for i in xrange(len(qe_outandver_dict)):
	error = 0
	#taking just file name
	address = qe_outandver_dict.keys()[i]
	print "Extracting info from "+str(i)+" of "+str(len(qe_outandver_dict))+" address=> "+address+" version =>"+qe_outandver_dict.values()[i]
	address_vs_version[address] = qe_outandver_dict.values()[i]
	#checking error
	input_coord_error = cmdline("grep -i \"atomic position info missing\" "+address).rstrip("\n")
	rights_error = cmdline("grep -i \"error opening\" "+address).rstrip("\n")
	chddencutoff = cmdline("grep -i \"charge density cutoff\" "+address).split("\n")[0].split("=")[-1].lstrip(" ")
	kincutoff = cmdline("grep -i \"kinetic-energy cutoff\" "+address).split("\n")[0].split("=")[-1].lstrip(" ")
	kpoint = cmdline("grep \"number of k points\" "+address)
	if len(rights_error)>2:
		error = 2
		has_error[address] = "Yes"
	if kincutoff=="" or chddencutoff=="" or kpoint=="" or kpoint[:5]=="Binar":
		error = 3
		has_error[address] = "Yes"
	if len(input_coord_error)>2:
		error = 1
		has_error[address] = "Yes"
	if error == 0:
		has_error[address] = "No"
		name = address.split("/")[-1].split(".")[0]
		address_vs_name[address] = name
		#taking cut offs kinetic and charge density and kpoint
		kincutoff = cmdline("grep -i \"kinetic-energy cutoff\" "+address).split("\n")[0].split("=")[-1].lstrip(" ")
		address_vs_kincutoff[address] = kincutoff.split()[0]
		chddencutoff = cmdline("grep -i \"charge density cutoff\" "+address).split("\n")[0].split("=")[-1].lstrip(" ")
		address_vs_chdencutoff[address] = chddencutoff.split()[0]
		kpoint = cmdline("grep \"number of k points\" "+address).split("\n")[0].split()[4]
		address_vs_kpoint[address] = kpoint
		#Finding atom count and different atom types
		how_many = cmdline("head -100 "+address+" |grep -i \"number of atoms\"").rstrip("\n").split("=")[1]
		how_many_dif = cmdline("head -100 "+address+" |grep -i \"number of atomic types\"").rstrip("\n").split("=")[1]
		how_many_diffrent_atom[address] = how_many_dif.lstrip(" ")
		how_many_atom[address]  = how_many.lstrip(" ")
		#Finding if the job finished or not
		tail = cmdline("tail -n 30 "+address+" |grep -i \"DONE\"").rstrip("\n")
		if len(tail)>1:
			is_finished[address] = "Finished"
		else:
			is_finished[address] = "Not Finished"
		#Finding final density and volume and energy
		if is_finished[address] == "Finished":
			converged = cmdline("grep \"convergence NOT achieved after\" "+address).rstrip("\n")
			if len(converged)>2:
				address_vs_volume[address] = "Not Converged"
				address_vs_energy[address] = "Not Converged"
				has_error[address] = "Yes"
			else:
				density_volume_raw = cmdline("grep -A 2 \"Begin final coordinates\" "+address).rstrip("\n")
				density_volume_raw = density_volume_raw.split("\n")
				volume = density_volume_raw[1].split("=")[1].lstrip(" ")
				volume = volume.split("a.u.^3")[1][2:-1].lstrip(" ")
				address_vs_volume[address] = volume
				energy_raw = cmdline("grep -i \"final enthalpy\" "+address).rstrip("\n").split("=")[1].lstrip(" ")
				address_vs_energy[address] = energy_raw
		else:
			address_vs_volume[address] = "Job Not Finished"
			address_vs_energy[address] = "Job Not Finished"
	if error==1:
		address_vs_kpoint[address] = "Input Error"
		address_vs_kincutoff[address] = "Input Error"
		address_vs_chdencutoff[address] = "Input Error"
		address_vs_name[address] = "Input Error"
		address_vs_energy[address] = "Input Error"
		address_vs_volume[address] = "Input Error"
		how_many_diffrent_atom[address] = "Input Error"
		how_many_atom[address] = "Input Error"
		is_finished[address] = "Input Error"
	if error==2:
		address_vs_kpoint[address] = "Rights Error"
		address_vs_kincutoff[address] = "Rights Error"
		address_vs_chdencutoff[address] = "Rights Error"
		address_vs_name[address] = "Rights Error"
		address_vs_energy[address] = "Rights Error"
		address_vs_volume[address] = "Rights Error"
		how_many_diffrent_atom[address] = "Rights Error"
		how_many_atom[address] = "Rights Error"
		is_finished[address] = "Rights Error"
	if error==3:
		address_vs_kpoint[address] = "Strange Error"
		address_vs_kincutoff[address] = "Strange Error"
		address_vs_chdencutoff[address] = "Strange Error"
		address_vs_name[address] = "Strange Error"
		address_vs_energy[address] = "Strange Error"
		address_vs_volume[address] = "Strange Error"
		how_many_diffrent_atom[address] = "Strange Error"
		how_many_atom[address] = "Strange Error"
		is_finished[address] = "Strange Error"

#pprint(has_error)
#pprint(address_vs_kpoint)
#pprint(address_vs_kincutoff)
#pprint(address_vs_chdencutoff)
#pprint(address_vs_name)
#pprint(address_vs_energy)
#pprint(address_vs_volume)
#pprint(how_many_diffrent_atom)
#pprint(how_many_atom)
#pprint(is_finished)

table = PrettyTable([
"Address",
"K-Coff(Ry)",
"Ch-Den-Coff(Ry)",
"Kpt",
"UC Volume",
"Atom Count",
"Type Count",
"Status",
"Error",
"QE ver",
"Energy(Ry)"
])

energy_sorted = sorted(address_vs_energy.items(), key=lambda t: t[1], reverse=True)

for i in xrange(len(energy_sorted)):
	table.add_row([energy_sorted[i][0],
	address_vs_kincutoff[energy_sorted[i][0]],
	address_vs_chdencutoff[energy_sorted[i][0]],
	address_vs_kpoint[energy_sorted[i][0]],
	address_vs_volume[energy_sorted[i][0]],
	how_many_atom[energy_sorted[i][0]],
	how_many_diffrent_atom[energy_sorted[i][0]],
	is_finished[energy_sorted[i][0]],
	has_error[energy_sorted[i][0]],
	address_vs_version[energy_sorted[i][0]],
	address_vs_energy[energy_sorted[i][0]]
	])

print table