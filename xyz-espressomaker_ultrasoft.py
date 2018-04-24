#!/usr/bin/env python2
import sys
import os

if(len(sys.argv)!=3):
	print "HATA!!!\nDogru kullanim > xyz-espressomaker.py xyz_dosyasi atom veya mars"
	exit(0)

def atom_list(filename):
	at_list = []
	xyzfile = open(filename,"r")
	line_num=0
	for at in xyzfile.readlines():
		line_num+=1
		if line_num>2:
			at=at.split()
			if(at[0] not in at_list):
				at_list.append(at[0])
	xyzfile.close()
	return at_list

def pseudor(at_name):
    if at_name=="Ag": return "ag_pbe_v1.4.uspp.F.UPF"
    if at_name=="Al": return "Al.pbe-n-kjpaw_psl.1.0.0.UPF"
    if at_name=="Ar": return "Ar.pbe-n-rrkjus_psl.1.0.0.UPF"
    if at_name=="As": return "As.pbe-n-rrkjus_psl.0.2.UPF"
    if at_name=="Au": return "Au_ONCV_PBE-1.0.upf"
    if at_name=="Ba": return "Ba_ONCV_PBE-1.0.upf"
    if at_name=="Be": return "Be_ONCV_PBE-1.0.upf"
    if at_name=="Bi": return "Bi.pbe-dn-kjpaw_psl.0.2.2.UPF"
    if at_name=="B": return "B.pbe-n-kjpaw_psl.0.1.UPF"
    if at_name=="Br": return "br_pbe_v1.4.uspp.F.UPF"
    if at_name=="Ca": return "Ca_pbe_v1.uspp.F.UPF"
    if at_name=="Cd": return "Cd.pbe-dn-rrkjus_psl.0.3.1.UPF"
    if at_name=="Ce": return "Ce.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Cl": return "Cl.pbe-n-rrkjus_psl.1.0.0.UPF"
    if at_name=="Co": return "Co_pbe_v1.2.uspp.F.UPF"
    if at_name=="C": return "C_pbe_v1.2.uspp.F.UPF"
    if at_name=="Cr": return "cr_pbe_v1.5.uspp.F.UPF"
    if at_name=="Cs": return "Cs_pbe_v1.uspp.F.UPF"
    if at_name=="Cu": return "Cu_pbe_v1.2.uspp.F.UPF"
    if at_name=="Dy": return "Dy.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Er": return "Er.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Eu": return "Eu.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Fe": return "Fe.pbe-spn-kjpaw_psl.0.2.1.UPF"
    if at_name=="F": return "f_pbe_v1.4.uspp.F.UPF"
    if at_name=="Ga": return "Ga.pbe-dn-kjpaw_psl.1.0.0.UPF"
    if at_name=="Gd": return "Gd.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Ge": return "Ge.pbe-dn-kjpaw_psl.1.0.0.UPF"
    if at_name=="He": return "He_ONCV_PBE-1.0.upf"
    if at_name=="Hf": return "Hf.pbe-spdfn-kjpaw_psl.1.0.0.UPF"
    if at_name=="Hg": return "Hg_pbe_v1.uspp.F.UPF"
    if at_name=="Ho": return "Ho.GGA-PBE-paw-v1.0.UPF"
    if at_name=="H": return "H.pbe-rrkjus_psl.0.1.UPF"
    if at_name=="In": return "In.pbe-dn-rrkjus_psl.0.2.2.UPF"
    if at_name=="I": return "I_pbe_v1.uspp.F.UPF"
    if at_name=="Ir": return "Ir_pbe_v1.2.uspp.F.UPF"
    if at_name=="K": return "K.pbe-spn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Kr": return "Kr.pbe-n-rrkjus_psl.0.2.3.UPF"
    if at_name=="La": return "La.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Li": return "li_pbe_v1.4.uspp.F.UPF"
    if at_name=="Lu": return "Lu.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Mg": return "mg_pbe_v1.4.uspp.F.UPF"
    if at_name=="Mn": return "Mn.pbe-spn-kjpaw_psl.0.3.1.UPF"
    if at_name=="Mo": return "Mo_ONCV_PBE-1.0.upf"
    if at_name=="Na": return "Na_pbe_v1.uspp.F.UPF"
    if at_name=="Nb": return "Nb.pbe-spn-kjpaw_psl.0.3.0.UPF"
    if at_name=="Nd": return "Nd.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Ne": return "Ne.pbe-n-kjpaw_psl.1.0.0.UPF"
    if at_name=="Ni": return "ni_pbe_v1.4.uspp.F.UPF"
    if at_name=="N": return "N.pbe.theos.UPF"
    if at_name=="O": return "O.pbe-n-kjpaw_psl.0.1.UPF"
    if at_name=="Os": return "Os.pbe-spfn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Pb": return "Pb.pbe-dn-kjpaw_psl.0.2.2.UPF"
    if at_name=="Pd": return "Pd.pbe-spn-kjpaw_psl.1.0.0.UPF"
    if at_name=="Pm": return "Pm.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Po": return "Po.pbe-dn-rrkjus_psl.1.0.0.UPF"
    if at_name=="P": return "P.pbe-n-rrkjus_psl.1.0.0.UPF"
    if at_name=="Pr": return "Pr.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Pt": return "Pt.pbe-spfn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Rb": return "Rb_ONCV_PBE-1.0.upf"
    if at_name=="Re": return "Re_pbe_v1.2.uspp.F.UPF"
    if at_name=="Rh": return "Rh.pbe-spn-kjpaw_psl.1.0.0.UPF"
    if at_name=="Rn": return "Rn.pbe-dn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Ru": return "Ru_ONCV_PBE-1.0.upf"
    if at_name=="Sb": return "sb_pbe_v1.4.uspp.F.UPF"
    if at_name=="Sc": return "Sc_pbe_v1.uspp.F.UPF"
    if at_name=="Se": return "Se_pbe_v1.uspp.F.UPF"
    if at_name=="Si": return "Si.pbe-n-rrkjus_psl.1.0.0.UPF"
    if at_name=="Sm": return "Sm.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Sn": return "Sn_pbe_v1.uspp.F.UPF"
    if at_name=="S": return "S_pbe_v1.2.uspp.F.UPF"
    if at_name=="Sr": return "Sr.pbe-spn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Ta": return "Ta.pbe-spfn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Tb": return "Tb.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Tc": return "Tc_ONCV_PBE-1.0.upf"
    if at_name=="Te": return "Te_pbe_v1.uspp.F.UPF"
    if at_name=="Ti": return "ti_pbe_v1.4.uspp.F.UPF"
    if at_name=="Tl": return "Tl.pbe-dn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Tm": return "Tm.GGA-PBE-paw-v1.0.UPF"
    if at_name=="V": return "V_pbe_v1.uspp.F.UPF"
    if at_name=="W": return "W_pbe_v1.2.uspp.F.UPF"
    if at_name=="Xe": return "Xe.pbe-dn-rrkjus_psl.1.0.0.UPF"
    if at_name=="Yb": return "Yb.GGA-PBE-paw-v1.0.UPF"
    if at_name=="Y": return "Y_pbe_v1.uspp.F.UPF"
    if at_name=="Zn": return "Zn_pbe_v1.uspp.F.UPF"
    if at_name=="Zr": return "Zr_pbe_v1.uspp.F.UPF"

def weights(at_name):
    if at_name=="H": return 1.008
    if at_name=="He": return 4.003
    if at_name=="Li": return 6.941
    if at_name=="Be": return 9.012
    if at_name=="B": return 10.811
    if at_name=="C": return 12.011
    if at_name=="N": return 14.007
    if at_name=="O": return 15.999
    if at_name=="F": return 18.998
    if at_name=="Ne": return 20.180
    if at_name=="Na": return 22.990
    if at_name=="Mg": return 24.305
    if at_name=="Al": return 26.982
    if at_name=="Si": return 28.086
    if at_name=="P": return 30.974
    if at_name=="S": return 32.065
    if at_name=="Cl": return 35.453
    if at_name=="Ar": return 39.948
    if at_name=="K": return 39.098
    if at_name=="Ca": return 40.078
    if at_name=="Sc": return 44.956
    if at_name=="Ti": return 47.867
    if at_name=="V": return 50.942
    if at_name=="Cr": return 51.996
    if at_name=="Mn": return 54.938
    if at_name=="Fe": return 55.845
    if at_name=="Co": return 58.933
    if at_name=="Ni": return 58.693
    if at_name=="Cu": return 63.546
    if at_name=="Zn": return 65.390
    if at_name=="Ga": return 69.723
    if at_name=="Ge": return 72.640
    if at_name=="81": return 74.922
    if at_name=="Se": return 78.960
    if at_name=="Br": return 79.904
    if at_name=="Kr": return 83.800
    if at_name=="Rb": return 85.468
    if at_name=="Sr": return 87.620
    if at_name=="Y": return 88.906
    if at_name=="Zr": return 91.224
    if at_name=="Nb": return 92.906
    if at_name=="Mo": return 95.940
    if at_name=="Tc": return 98.000
    if at_name=="Ru": return 101.070
    if at_name=="Rh": return 102.906
    if at_name=="Pd": return 106.420
    if at_name=="Ag": return 107.868
    if at_name=="Cd": return 112.411
    if at_name=="In": return 114.818
    if at_name=="Sn": return 118.710
    if at_name=="Sb": return 121.760
    if at_name=="Te": return 127.600
    if at_name=="I": return 126.905
    if at_name=="Xe": return 131.293
    if at_name=="Cs": return 132.906
    if at_name=="Ba": return 137.327
    if at_name=="La": return 138.906
    if at_name=="Ce": return 140.116
    if at_name=="Pr": return 140.908
    if at_name=="Nd": return 144.240
    if at_name=="Pm": return 145.000
    if at_name=="Sm": return 150.360
    if at_name=="Eu": return 151.964
    if at_name=="Gd": return 157.250
    if at_name=="Tb": return 158.925
    if at_name=="Dy": return 162.500
    if at_name=="Ho": return 164.930
    if at_name=="Er": return 167.259
    if at_name=="Tm": return 168.934
    if at_name=="Yb": return 173.040
    if at_name=="Lu": return 174.967
    if at_name=="Hf": return 178.490
    if at_name=="Ta": return 180.948
    if at_name=="W": return 183.840
    if at_name=="Re": return 186.207
    if at_name=="Os": return 190.230
    if at_name=="Ir": return 192.217
    if at_name=="Pt": return 195.078
    if at_name=="Au": return 196.967
    if at_name=="Hg": return 200.590
    if at_name=="Tl": return 204.383
    if at_name=="Pb": return 207.200
    if at_name=="Bi": return 208.980
    if at_name=="Po": return 209.000
    if at_name=="At": return 210.000
    if at_name=="Rn": return 222.000
    if at_name=="Fr": return 223.000
    if at_name=="Ra": return 226.000
    if at_name=="Ac": return 227.000
    if at_name=="Th": return 232.038
    if at_name=="Pa": return 231.036
    if at_name=="U": return 238.029
    if at_name=="Np": return 237.000
    if at_name=="Pu": return 244.000
    if at_name=="Am": return 243.000
    if at_name=="Cm": return 247.000
    if at_name=="Bk": return 247.000
    if at_name=="Cf": return 251.000
    if at_name=="Es": return 252.000
    if at_name=="Fm": return 257.000
    if at_name=="Md": return 258.000
    if at_name=="No": return 259.000
    if at_name=="Lr": return 262.000
    if at_name=="Rf": return 261.000
    if at_name=="Db": return 262.000
    if at_name=="Sg": return 266.000
    if at_name=="Bh": return 264.000
    if at_name=="Hs": return 277.000
    if at_name=="Mt": return 268.000 

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
at_list = atom_list(filename)
if(sys.argv[2]=="mars"):
	pseudo_dir="'/ORTAK/progs/QuantumESPRESSO/pseudo',\n"
if(sys.argv[2]=="atom"):
	pseudo_dir="'/opt/pseudo_test/SSSP_acc_PBE',\n"
foldername = filename.split(".")[0]+"_esp"
os.system("mkdir -p "+foldername)
os.system("cp "+filename+" "+foldername)
inputfilename=filename.split(".")[0]+".in"
inputfile=open(foldername+"/"+inputfilename,"w")
inputfile.write("""&control
    calculation='vc-relax',
    nstep=9000,
    restart_mode='from_scratch',
    prefix='mgli'
""")
inputfile.write("    pseudo_dir = "+pseudo_dir)
inputfile.write("""    outdir='tmp'
    wf_collect=.true.
    etot_conv_thr = 1.0D-5 ,
    forc_conv_thr = 1.0D-4 ,
/
&system
    ibrav=0,\n""")
xyzfile = open(filename,"r")
at_num = xyzfile.readline().rstrip("\n")
xyzfile.close()
inputfile.write("    nat="+str(at_num)+",\n")
inputfile.write("    ntyp="+str(len(at_list))+",\n")
inputfile.write("""    ecutwfc =40.0,
    ecutrho=320,
    occupations = 'smearing',
    degauss = 0.005D0,
    smearing='gaussian',
/
&electrons
    conv_thr = 1.0e-8
    mixing_beta = 0.8
    electron_maxstep = 1000,
/
&ions
     ion_dynamics = 'bfgs' ,
/
&cell
   cell_dynamics = 'bfgs' ,
   cell_factor=1.8D0,
/
ATOMIC_SPECIES
""")
file.close()
for i in range(len(at_list)):
	inputfile.write(at_list[i]+"\t"+str(weights(at_list[i]))+"\t"+pseudor(at_list[i])+"\n")
inputfile.write("CELL_PARAMETERS angstrom\n")
inputfile.write("    "+str(cell1)+"\t"+str(cell2)+"\t"+str(cell3)+"\n")
inputfile.write("    "+str(cell4)+"\t"+str(cell5)+"\t"+str(cell6)+"\n")
inputfile.write("    "+str(cell7)+"\t"+str(cell8)+"\t"+str(cell9)+"\n")
inputfile.write("ATOMIC_POSITIONS angstrom\n")

line_num=0
xyzfile = open(filename,"r")
for line in xyzfile.readlines():
	line_num+=1
	if line_num>2:
		line=line.split()
		inputfile.write('{0:.5s}'.format(line[0])+"\t"+str('{0:.10f}'.format(float(line[1])))+"\t"+
			str('{0:.10f}'.format(float(line[2])))+"\t"+
			str('{0:.10f}'.format(float(line[3])))+"\n")
inputfile.write("""K_POINTS automatic
2 2 2  0 0 0\n""")