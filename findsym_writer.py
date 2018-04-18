#!/usr/bin/env python2
from atomnum2name import atomnum2name

#reversing atomnum2name
atomname2num = {v: k for k, v in atomnum2name.iteritems()}

def write_findsym(cell,xyz,result,sym_tol,at_namedata):
	fsym_in = open("findsym.in","w")
	fsym_in.write("TCCDEM group\n")
	fsym_in.write(str(sym_tol)+"\n")
	fsym_in.write(str(1))
	for i in xrange(len(cell)):
		if i%3==0:
			fsym_in.write("\n")
		fsym_in.write(cell[i]+"\t")
	fsym_in.write("\n"+"2"+"\n"+"P"+"\n")
	fsym_in.write(str(result.shape[0])+"\n")
	for i in xrange(len(at_namedata)):
		fsym_in.write(str(atomname2num[at_namedata[i]])+" ")
	fsym_in.write("\n")
	for i in xrange(len(xyz)):
		fsym_in.write(str(result[i])[1:-1]+"\n")
	fsym_in.close()
