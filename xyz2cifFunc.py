#!/usr/bin/env python2
"""
converts xyz files to cif
written by Samet Demir
usage: xyz2cif.py xyz_file cell_file sym_tol cif_name

cell_file data must be angstrom
"""
import os
import numpy as np
from findsym_writer import write_findsym
from fsymout2cif import fsymout2cif
from functions_of_caspesa import (cmdline)

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
        xyz[i].pop(0)
    return np.array(xyz),at_namedata
    
def process_cell(cell):
    a=[cell[0],cell[1],cell[2]]
    b=[cell[3],cell[4],cell[5]]
    c=[cell[6],cell[7],cell[8]]
    returndata = [a,b,c]
    return np.array(returndata)

def at_types_fromnamedata(at_namedata):
    at_types = []
    for x in xrange(len(at_namedata)):
        if at_namedata[x] not in at_types:
            at_types.append(at_namedata[x])
    return at_types

def cellFloat(cell):
    a=[float(cell[0][0]),float(cell[0][1]),float(cell[0][2])]
    b=[float(cell[1][0]),float(cell[1][1]),float(cell[1][2])]
    c=[float(cell[2][0]),float(cell[2][1]),float(cell[2][2])]
    returndata = [a,b,c]
    return np.array(returndata)

def xyz2cifFunc(xyzFilename,cell_file,sym_tol,cifFilename):
  xyz = read_xyz(xyzFilename)
  cell = read_cell(cell_file)
  #processing for conversion
  cell_processed = process_cell(cell)
  xyz_processed, at_namedata = process_xyz(xyz)
  #taking transposes for the shape
  cell_processed_transposed = np.transpose(cell_processed).astype(float)
  xyz_processed_transposed = np.transpose(xyz_processed).astype(float)
  #the conversion
  converted = np.linalg.solve(cell_processed_transposed,xyz_processed_transposed)
  #and the result
  result = np.transpose(converted)
  #finding different atom names from atom list
  at_types = at_types_fromnamedata(at_namedata)
  cf = cellFloat(cell_processed)
  volume = np.fabs(np.dot(np.cross(cf[0],cf[1]),cf[2]))
  write_findsym(cell,xyz,result,sym_tol,at_namedata)
  os.system("findsym < findsym.in > findsym.out")
  symnum=cmdline("grep \"Space Group\" findsym.out")
  fsymout2cif(at_types,cifFilename)
  return symnum,volume
