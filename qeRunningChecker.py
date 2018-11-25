#!/usr/bin/env python2
import os
from subprocess import PIPE, Popen
from pprint import pprint as pp
from prettytable import PrettyTable

def cmdline(command):
    process = Popen(
        args=command,
        stdin=PIPE,
        stdout=PIPE,
        shell=True,
    )
    return process.communicate()[0]

print "This script finds running QE jobs and prints last energy"

runningDirs = cmdline("squeue -u eaybey --states=RUNNING --format \"%Z\" | awk 'NR>=2'").split("\n")[:-1]

addressVsLastEnergy = {}
addressVsOneBeforeLastEnergy = {}
addressVsHowMany = {}
rawData = []

for directory in runningDirs:
  isQe = cmdline("head "+directory+"/*.out |grep 'PWSCF'").lstrip(" ").rstrip("\n")
  if 'pwscf' in isQe.lower():
    isNew = cmdline("grep -i 'enthalpy new' "+directory+"/*.out |wc -l").rstrip("\n")
    if(int(isNew)>=2):
      rawData.append(cmdline("grep -i 'enthalpy new' "+directory+"/*.out |tail -n2").split("\n")[:-1])
    else:
      rawData.append(str(directory + "/*.out: JustStarted 0 JustStarted\n"+directory + "/*.out: JustStarted 0 JustStarted\n").split("\n"))

for i in range(len(rawData)):
  address = rawData[i][0].split()[0][:-1]
  lastEnergy = rawData[i][1].split()[-2]
  oneBeforeLastEnergy = rawData[i][0].split()[-2]
  howMany = cmdline("grep -i 'enthalpy new' "+address+" |wc -l").rstrip("\n")
  addressVsLastEnergy[address] = lastEnergy
  addressVsOneBeforeLastEnergy[address] = oneBeforeLastEnergy
  addressVsHowMany[address] = howMany

table = PrettyTable([
"Address",
"Energy",
"HowManyIteration",
"LastDiff"
])

for i in range(len(addressVsLastEnergy)):
  address = addressVsLastEnergy.keys()[i]
  lastEn = addressVsLastEnergy[address]
  oneBeforeLast = addressVsOneBeforeLastEnergy[address]
  howManyIt = addressVsHowMany[address]
  table.add_row([address,lastEn,howManyIt,format((float(lastEn) - float(oneBeforeLast)),'.8f')])

print table.get_string(sortby="Energy", reversesort=True)
