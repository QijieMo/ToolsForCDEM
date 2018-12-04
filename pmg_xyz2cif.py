#!/usr/bin/env python2
"""
converts xyz files to cif
written by Samet Demir
usage: pmg_xyz2cif.py xyz_file cell_file sym_tol ang_tol cif_name

cell_file data must be angstrom
"""
import os
import math
import numpy as np
import subprocess
from subprocess import PIPE, Popen
import sys
import numpy as np
import pymatgen as mg
from pymatgen.io.cif import CifWriter

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def read_xyz(filename):
    xyz_file = open(filename,"r")
    xyz_data = xyz_file.readlines()
    if len(xyz_data[0].split())<2:
        xyz_data=xyz_data[2:]
    xyz_file.close()
    return  xyz_data

def read_cell(filename):
    cell_file = open(filename,"r")
    cell_data = cell_file.readlines()
    returndata = []
    for i in xrange(len(cell_data)):
        cell_data[i]=cell_data[i].split()
        for j in xrange(len(cell_data[i])):
            returndata.append(cell_data[i][j])
    cell_file.close()
    return returndata

def process_xyz(xyz):
    returndata = []
    at_namedata = []
    for i in xrange(len(xyz)):
        xyz[i]=xyz[i].split()
        at_namedata.append(xyz[i][0])
        xyz[i] = [float(xyz[i][1]),float(xyz[i][2]),float(xyz[i][3])]
    return xyz,at_namedata
    
def process_cell(cell):
    a=[float(cell[0]),float(cell[1]),float(cell[2])]
    b=[float(cell[3]),float(cell[4]),float(cell[5])]
    c=[float(cell[6]),float(cell[7]),float(cell[8])]
    returndata = [a,b,c]
    return returndata

def at_types_fromnamedata(at_namedata):
    at_types = []
    for x in xrange(len(at_namedata)):
        if at_namedata[x] not in at_types:
            at_types.append(at_namedata[x])
    return at_types


#Taking arguments with error control
if len(sys.argv)<5 or len(sys.argv)>5:
    print "Arguments are wrong.\n" \
          "Correct usage: pmg_xyz2cif.py xyz_file cell_file sym_tol ang_tol cif_name"
    exit(0)
else:
    xyz_file_name = sys.argv[1]
    cell_file_name = sys.argv[2]
    sym_tol = float(sys.argv[3])
    cif_name = sys.argv[4]

xyz = read_xyz(sys.argv[1])
cell = read_cell(sys.argv[2])
#getting rid of scientific notation
np.set_printoptions(suppress=True)
#processing for conversion
cell_processed = process_cell(cell)
xyz_processed, at_namedata = process_xyz(xyz)
st = mg.Structure(cell_processed,at_namedata,xyz_processed,coords_are_cartesian=True)
cifFile = open(cif_name,"w")
cifFile.write(str(CifWriter(st,symprec=sym_tol)))
cifFile.close()
print "Space"