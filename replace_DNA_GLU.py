import os
import sys
import numpy as np
inputfile = sys.argv[1]
outputfile = sys.argv[2]
data = ""
with open(inputfile,"r") as fopen:
     for line in fopen.readlines():
         resname = line[17:20]
         if resname == "CYT" or resname == "ADE" or resname == "GUA" or resname == "THY":
            name = line[13:14]
            if name == "S":
               namen = "C   "
            elif name == "P":
               namen = "O   "
            else:
               namen = "CB  "
            print (resname,name,namen)
            data += line[0:13] + namen + "GLU" + line[20:66] + "           " + namen[0:1] + "\n"
         else:
            data += line
with open(outputfile,"w") as fwrite:
     fwrite.writelines(data)
