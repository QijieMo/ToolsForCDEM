#!/usr/bin/env python2
import pybel
from math import sqrt,sin,cos,pi,acos,floor,ceil
import numpy
mol=pybel.readfile("cif","paperstructure.cif").next()
uc = mol.unitcell
print uc
uc.FillUnitCell(mol.OBMol)
print mol.OBMol
uc.SetSpaceGroup("P1") 
print uc.GetFractionalMatrix()
mol.write("xyz","sametdemir.xyz")
