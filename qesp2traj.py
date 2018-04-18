#!/usr/bin/env python2
"""
This script reads quantum espresso output
and writes ase traj file of it
so it can be easily viewed from ase-gui
"""
import sys
import ase.io

if len(sys.argv)<3 or len(sys.argv)>3:
	print """Arguments are wrong! Right usage:
python2 qesp2traj.py espresso_outfile trajname"""
	exit(0)
else:
	espOut_name = sys.argv[1]
	traj_name = sys.argv[2]

#a,b,c = parseCell(espOut_name)
qesp = ase.io.read(espOut_name,index=slice(None),format="espresso-out")
ase.io.write(traj_name, qesp, format="traj")