import os
from subprocess import PIPE, Popen
from pprint import pprint as pp

def cmdline(command):
    process = Popen(
        args=command,
        stdin=PIPE,
        stdout=PIPE,
        shell=True,
        close_fds=True,
        bufsize=-1
    )
    return process.communicate()[0]

inputs = cmdline("find . -iname *.in")
addresses = inputs.split("\n")[:-1]
print "Found inputs:"
pp(addresses)
cwd = os.getcwd() 
for i in range(len(addresses)):
    inputNname = addresses[i].split("/")[-1]
    inputNnameOut = inputNname.split(".in")[0]+".out"
    addressLoc = str(addresses[i].split(inputNname)[:-1][0])
    os.chdir(cwd)
    os.chdir(addressLoc)
    slurm = open("submit.sl","w")
    slurm.write("#!/bin/bash\n")
    slurm.write("#SBATCH -A dbmae1\n")
    slurm.write("#SBATCH -n 28\n")
    slurm.write("#SBATCH -p defq\n")
    slurm.write("#SBATCH -t 0-7:00\n")
    slurm.write("module load QuantumESPRESSO/qe-6.1-intel-2017.4-epw-4.2\n")
    slurm.write("mpirun pw.x < "+inputNname+" > " + inputNnameOut)
    slurm.close()