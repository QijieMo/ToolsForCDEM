import os
from pprint import pprint as pp
import sys
################################################
from subprocess import PIPE, Popen
import os
def cmdline(command):
    process = Popen(
        args=command,
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        shell=True,
        close_fds=True,
        bufsize=-1
    )
    return process.communicate()[0]
################################################
if len(sys.argv)<3 or len(sys.argv)>3:
    print "Arguments are wrong.\n" \
          "Correct usage: fcas_executer_writer.py preName howmany"
    exit(0)
else:
    preName = sys.argv[1]
    howmany = sys.argv[2]
################################################
executables = cmdline("find . -iname 'fcaspesa_*' ").split("\n")[:-1]
folder_vs_exe = {}
for i in range(len(executables)):
  folder_vs_exe[executables[i].split("/")[1]] = executables[i].split("/")[2]

print "Found folders vs Excecutables"
pp(folder_vs_exe)
################################################
print "Now writing executer.py files"
for i in range(len(folder_vs_exe)):
  executer = open(folder_vs_exe.keys()[i]+"/executer.py","w")
  executer.write("import os\n")
  executer.write("how_many = "+str(howmany)+"\n")
  executer.write("name = \""+str(preName)+"_"+str(folder_vs_exe.keys()[i])+"_\"\n")
  executer.write("for i in range(how_many):\n")
  executer.write("        os.system(\"mpirun \"+\" ./"+str(folder_vs_exe[folder_vs_exe.keys()[i]])+" \"+name+str(i)+\".xyz\")\n")
  executer.close()

