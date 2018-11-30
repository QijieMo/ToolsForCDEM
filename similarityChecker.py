from pymatgen import Structure
from pymatgen.analysis.structure_matcher import StructureMatcher
from subprocess import PIPE, Popen
import sys

def cmdline(command):
  process = Popen(
    args=command,
    stdin=PIPE,
    stdout=PIPE,
    stderr=PIPE,
    shell=True,
  )
  return process.communicate()[0]

if len(sys.argv)<2 or len(sys.argv)>2:
    print "Arguments are wrong.\n" \
          "Correct usage: similarityMatcher.py ./cifaddress (./ is important)"
    exit(0)
else:
    cifAddr = sys.argv[1]

lengthTol = 0.45 # default 0.2
siteTol = 0.2 # default 0.3
angleTol = 3 # default 5 degree
# finding all cif files under this folder
cifFiles = cmdline("find . -iname '*.cif'").split("\n")[:-1]
cifFiles.remove(cifAddr)

similarStr = []
for i in range(len(cifFiles)):
  print "Checking",i,"of",len(cifFiles)-1,cifFiles[i]
  s1 = Structure.from_file(cifAddr)
  s2 = Structure.from_file(cifFiles[i])
  if(StructureMatcher(ltol=lengthTol,stol=siteTol,angle_tol=angleTol).fit(s1,s2)):
  	similarStr.append(cifFiles[i])
  	print "ALOHA"

print "Found similar structure addresses:",similarStr