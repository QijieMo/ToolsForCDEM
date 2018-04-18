#!/usr/bin/env python2
import os
from functions_of_caspesa import (cmdline)
import sys

if len(sys.argv)<3 or len(sys.argv)>3:
    print "Arguments are wrong.\n" \
          "Correct usage: qe_out2xyzmovie.py qe_outfile xyz_name"
    exit(0)
else:
	out_name = sys.argv[1]
	xyz_name = sys.argv[2]

how_many = cmdline("head -100 "+out_name+" |grep -i \"number of atoms\"").rstrip("\n").split("=")[1].lstrip(" ")
print "Atom Count in a cell: "+how_many
coord_line_numbers = cmdline("grep -nr -i \"ATOMIC_POSITIONS\" "+out_name).split("\n")
coord_line_numbers.remove('')
just_linenumbers =[]
for i in xrange(len(coord_line_numbers)):
	coord_line_numbers[i] = coord_line_numbers[i].split(":")
	just_linenumbers.append(coord_line_numbers[i][0])
print "Iteration Count: "+str(len(just_linenumbers))
print "Writing operation is started. Please wait.."
xyz_file = open(xyz_name,"w")
for i in xrange(len(just_linenumbers)):
	print "Writing "+str(i)+" of "+str(len(just_linenumbers))
	begin_line= str(int(just_linenumbers[i])+1)
	end_line = str(int(begin_line) + int(how_many)-1)
	command = "awk 'NR >="+begin_line+" && NR <= "+end_line+"' "+out_name
	coord = cmdline(command).rstrip("\n")
	xyz_file.write(str(how_many)+"\n"+"\n")
	xyz_file.write(coord+"\n")
print "FINISHED"
xyz_file.close()

