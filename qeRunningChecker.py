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
rawData = []
for directory in runningDirs:
  rawData.append(cmdline("grep -i 'enthalpy new' "+directory+"/*.out |tail -n2").split("\n")[:-1])

for i in range(len(rawData)):
  address = rawData[i][0].split()[0][:-1]
  lastEnergy = rawData[i][1].split()[-2]
  oneBeforeLastEnergy = rawData[i][0].split()[-2]
  addressVsLastEnergy[address] = lastEnergy
  addressVsOneBeforeLastEnergy[address] = oneBeforeLastEnergy

table = PrettyTable([
"Address",
"Energy",
"LastDiff"
])

for i in range(len(addressVsLastEnergy)):
  address = addressVsLastEnergy.keys()[i]
  lastEn = addressVsLastEnergy[address]
  oneBeforeLast = addressVsOneBeforeLastEnergy[address]
  table.add_row([address,lastEn,format((float(lastEn) - float(oneBeforeLast)),'.8f')])

print table
