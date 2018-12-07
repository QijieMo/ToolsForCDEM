from pymatgen import Structure
from pymatgen.analysis.structure_matcher import StructureMatcher
from subprocess import PIPE, Popen
import sys
import pickle

import numpy as np
np.set_printoptions(threshold=np.nan)

def cmdline(command):
  process = Popen(
    args=command,
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE,
    shell=True,
  )
  return process.communicate()[0]

def findMatch(cifFiles,matchTable):
  diff = np.array([])
  stDiff = []
  for i in range(len(cifFiles)):
#    print "Processing ",i,"of",len(cifFiles)-1
    if(i not in diff):
      for j in range(i+1,len(cifFiles)):
      	if(j not in diff):
          s1 = Structure.from_file(cifFiles[i])
          s2 = Structure.from_file(cifFiles[j])
          if(StructureMatcher(ltol=lengthTol,stol=siteTol,angle_tol=angleTol).fit(s1,s2)):
            matchTable[i,j] = 1
            stDiff.append(j)
      for k in stDiff:
        for l in stDiff:
          if l>k:
            matchTable[k,l] = 1
      if(len(stDiff)!=0):
        reporter(i,matchTable[i,:])
      else:
      	print "\n",i,"numarali",cifFiles[i],"adresli yapinin BENZERI YOK"
      stDiff.append(i)
      unique_list.append(stDiff)
      diff = np.append(diff,stDiff)
      stDiff = []

def reporter(i,match_i):
  print "\n",i,"numarali yapinin adresi:",cifFiles[i]
  print i," numarali yapiya benzeyen yapilar"
  print "\t",np.where(match_i[:])[0]
  print "\t\tBenzeyen yapilarin adresleri:"
  for k in range(len(np.where(match_i[:])[0])):
    print "\t\t\t",cifFiles[(np.where(match_i[:])[0])[k]]


lengthTol = 0.2 # default 0.2
siteTol = 0.3 # default 0.3
angleTol = 5 # default 5 degree
# finding all cif files under this folder
unique_list = []
cifFiles = cmdline("find . -iname *.cif").split("\n")[:-1]
matchTable = np.zeros([len(cifFiles),len(cifFiles)])
findMatch(cifFiles,matchTable)
print "Benzersiz yapilar:"
print unique_list

with open('matchAndAddress.pkl', 'wb') as f:
  pickle.dump(matchTable, f)
  pickle.dump(cifFiles, f)
  pickle.dump(unique_list,f)