import os
import subprocess
from subprocess import PIPE, Popen
import operator
from pprint import pprint

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

xyz_name_to_ls = "processed"
ls_result = (str(cmdline("ls "+xyz_name_to_ls+"*.xyz")).split("\n"))
ls_result = filter(None, ls_result)
mol_energy = {}
for xyz_name in ls_result:
	mol_energy[xyz_name] = float(cmdline("grep Energy "+xyz_name).rstrip("\n").lstrip(" Energy=  "))
sorted_xyz = sorted(mol_energy.items(), key=operator.itemgetter(1))
cat_command = "cat "
for i in range(len(ls_result)):
	cat_command += sorted_xyz[i][0]+" "
cat_command += " > all.xyz"
pprint(sorted_xyz)
os.system(cat_command)
