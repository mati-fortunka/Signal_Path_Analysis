#!/usr/bin/env python3
"""
Created on 29.06.2021

@author: Mateusz Fortunka

"""

import sys

if __name__ == "__main__":
	if len(sys.argv)!=2:
		sys.exit("Wrong number of arguments given. Correct syntax: list_res.py file.pdb")
	else:
		file_pdb=sys.argv[1]
		if file_pdb[-4:] != '.pdb':
			print("Input file has a wrong extension. Nevertheless, the program will try to open it. However, the results can be incorrect! Correct syntax: list_res.py file.pdb")


infile = open(file_pdb, "r")
out = file_pdb[0:-4]+"_res"+".txt" 
outfile = open(out, "w")
i=1
j=1
res_name=""
chain=""
for line in infile:
	if line[0:6] == 'HETATM' or line[0:4] == "ATOM":
		if line[23:26]!=res_name:
			if line[21]!=chain: j=1
			newline = str(i) + '\t' + str(j) + '\t' + line[23:26] + '\t' + line[21] + '\t' + line[17:21] + '\n'
			outfile.write(newline)
			i+=1
			j+=1
		res_name=line[23:26]
		chain = line[21]
infile.close()
outfile.close()
sys.exit(f"Output succesfully written to the {out} file.")



