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

slFile = cmdline("find . -iname *.sl")
addresses = slFile.split("\n")[:-1]
cwd = os.getcwd()
pp(addresses)
for i in range(len(addresses)):
    slurmName = addresses[i].split("/")[-1]
    addressLoc = str(addresses[i].split(slurmName)[:-1][0])
    pp(addressLoc)
    os.chdir(cwd)
    os.chdir(addressLoc)
    os.system("sbatch "+slurmName)