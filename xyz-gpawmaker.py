#!/usr/bin/env python2
import sys
import os

if(len(sys.argv)!=2):
        print "HATA!!!\nDogru kullanim > xyz-gpawmaker.py xyz_dosyasi"
        exit(0)


filename = sys.argv[1]
file = open(filename,"r")
cell_raw = file.readline()
cell_raw = file.readline()
cell_processed = cell_raw.split()[7:]
cell1 = cell_processed[0][2:-1]
cell2 = cell_processed[1][:-1]
cell3 = cell_processed[2].split("[")[0][:-1]
cell4 = cell_processed[2].split("[")[1][:-1]
cell5 = cell_processed[3][:-1]
cell6 = cell_processed[4].split("[")[0][:-1]
cell7 = cell_processed[4].split("[")[1][:-1]
cell8 = cell_processed[5][:-1]
cell9 = cell_processed[6][:-1]

foldername = filename.split(".")[0]
os.system("mkdir -p "+foldername)
os.system("cp "+filename+" "+foldername)
inputfilename=filename.split(".")[0]+".py"
inputfile=open(foldername+"/"+inputfilename,"w")
inputfile.write("""
from ase import *
from ase.build import *
from ase.io.xyz import *
from ase.io import read,write,Trajectory
from ase.optimize import BFGS
from ase import Atoms, Atom
from gpaw import GPAW, Mixer, ConvergenceError,PW, FermiDirac
from gpaw.mpi import size
from ase.optimize import bfgs
from ase.constraints import FixAtoms
from ase.constraints import UnitCellFilter
import time,numpy,string
 

nametoken = "out" 
qnlogfile = nametoken+".qn" 
hessianfile = nametoken+".hessian" 
trajectoryfile  = nametoken+".traj" 
""")
inputfile.write("atoms=read('"+filename+"',format=\"xyz\")\n")
inputfile.write("atoms.set_cell([("+str(cell1)+","+str(cell2)+","+str(cell3)+"),("
        +str(cell4)+","+str(cell5)+","+str(cell6)+"),("+str(cell7)+","
        +str(cell8)+","+str(cell9)+")])\n")
inputfile.write("""
atoms.set_pbc((True, True, True)) 
niggli_reduce(atoms) 
write("init111.xyz", atoms.repeat([1,1,1])) 
write("init222.xyz", atoms.repeat([2,2,2])) 
write("init333.xyz", atoms.repeat([3,3,3])) 
 

h = 0.2
kpt = 2

calc = GPAW(h=h,mode=PW(340),
            kpts=(kpt,kpt,kpt), xc='RPBE',
            maxiter=1500,
            txt=nametoken+'.txt'
           )


atoms.set_calculator(calc) 

ucf = UnitCellFilter(atoms)
relax = BFGS(ucf,logfile='qn.log')
traj = Trajectory('qn.traj', 'w', atoms)
relax.attach(traj)
relax.run(fmax=0.05)

write("out111.xyz", atoms.repeat([1,1,1])) 
write("out222.xyz", atoms.repeat([2,2,2])) 
write("out333.xyz", atoms.repeat([3,3,3]))
""")

inputfile.close()
