import os
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdin=PIPE,
        stdout=PIPE,
        shell=True,
        close_fds=True,
        bufsize=-1
    )
    return process.communicate()[0]

chosenNumbers = [207,138,113,130,32,341,125,204,245,331,19,84,205,171,86,386,396,230,107,211,223,336,380,80,368,33,50,85,363,212,378,316]
preName = "SrN1geo33_Mono_"
copyAddr = "/home/mulo/Desktop/Sr/n1/1_fu_espresso/Mono"
cwd = os.getcwd() # current working directory

for num in chosenNumbers:
	dirName = preName+str(num)
	os.chdir(cwd+"/"+dirName)
	print "maker command:"
	print "xyz-espressomaker_ultrasoft_d3disp.py "+preName+str(num)+".xyz"+" cell_file uhem"
	os.system("xyz-espressomaker_ultrasoft_d3disp.py "+preName+str(num)+".xyz"+" cell_file uhem")
	print "Copy command:"
	print "cp -r *_esp "+copyAddr
	os.system("cp -r *_esp "+copyAddr)