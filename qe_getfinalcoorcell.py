#!/usr/bin/env python2
import sys
import os
from pprint import pprint
from functions_of_caspesa import (cmdline)

qe_out_address = sys.argv[1]
xyz_name = sys.argv[2]
at_number = sys.argv[3]

coord_line_numbers = cmdline("grep -nr -i \"ATOMIC_POSITIONS\" "+qe_out_address).split("\n")
coord_line_numbers.remove('')
line_with_string = coord_line_numbers[-1]
angstrom = "angstrom"
bohr = "bohr"
crystal = "crystal"
alat = "alat"

print line_with_string.find(angstrom)
