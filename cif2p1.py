import pybel
from math import sqrt,sin,cos,pi,acos,floor,ceil
import numpy
mol=pybel.readfile("cif","Experimental.cif").next()
uc = mol.unitcell
print uc
uc.FillUnitCell(mol.OBMol)
print mol.OBMol
uc.SetSpaceGroup("P1") 
print uc.GetFractionalMatrix()
mol.write("xyz","sametdemir.xyz")