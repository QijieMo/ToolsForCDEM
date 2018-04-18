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

def weights(at_name):
    if at_name=="Mg": return 24.305;
    if at_name=="Ca": return 40.078;
    if at_name=="Sc": return 44.955908;
    if at_name=="Ti": return 47.867;
    if at_name=="Mn": return 54.9380;
    if at_name=="Co": return 58.9331;
    if at_name=="Ni": return 58.6934;
    if at_name=="Zn": return 65.38;
    if at_name=="Al": return 26.98153;
    if at_name=="Mo": return 95.95;
    if at_name=="Y": return 88.90584;
    if at_name=="Sr": return 87.62;
    if at_name=="Zr": return 91.224;
    if at_name=="H": return 1.0079;
    if at_name=="B": return 10.811;
    if at_name=="N": return 14.0067;
    if at_name=="Li": return 6.941;
    if at_name=="Na": return 22.990;
    if at_name=="K": return 39.098;

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
	pseudo_dir="'/opt/pseudo',\n"
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
inputfile.write("""    ecutwfc =80.0,
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
	inputfile.write(at_list[i]+"\t"+str(weights(at_list[i]))+"\t"+at_list[i]+".pbe-mt_fhi.UPF\n")
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