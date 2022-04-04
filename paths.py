# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 03:15:31 2021

@author: Mateusz Fortunka
"""

import sys
import glob
import numpy as np
import statistics as s

if __name__ == "__main__":
    if len(sys.argv)!=3:
        sys.exit("Wrong number of arguments given. Correct syntax: paths.py path_to_folder res_list")
    else:
        path = sys.argv[1]
        residue_list = sys.argv[2]


res = np.genfromtxt(residue_list, dtype='|U5', autostrip=True)
mut = { "A_FL": 0, "B_F": 0, "A_E": 0, "B_ED": 0}

def ch_res(no):
    name = res[no, 3] + "_" + res[no, 4] + "_" + res[no, 2]
    return(name)

def add_res(nm):
    name = ch_res(nm)
    if name == "A_PHE_185" or name == "A_LEU_185":
        mut["A_FL"]+=1
    elif name == "B_PHE_185":
        mut["B_F"]+=1
    elif name == "A_GLU_264":
        mut["A_E"]+=1
    elif name == "B_GLU_264" or name == "B_ASP_265":
        mut["B_ED"]+=1


files = [f for f in glob.glob(path + "/*.out.out", recursive=True)]

out = residue_list[0:-7] + "sum.txt"
outfile = open(out, "w")

for file in files:
    infile = open(file, "r")
    if not infile.readline():
        print(f"{file} is empty")
        continue
    infile.readline()
    infile.readline()
    line1=infile.readline()
    line2=infile.readline()
    start = ch_res(int(line1[-5:-2]))
    end = ch_res(int(line2[-5:-2]))
    outfile.write(f"Start: {start}\nEnd: {end}\n")  
    aa_len=[]
    length=[]
    no_of_paths=1
    for i in infile:
        if i=='The final paths are:\n':
            line3=infile.readline()
            aa_len.append(int(line3.count(",")))
            line3=line3.split(', ')
            length.append(int(line3.pop().replace(')', '').replace('(', '')))
            optimal=''
            for rs in line3:
                optimal+= ch_res(int(rs)) + ', '
                add_res(int(rs))
            optimal=optimal.rstrip(', ')
            outfile.write(optimal)
            outfile.write('\n')
        elif i[0:6]=="Number":
            outfile.write(i)     
            break
        else:
            aa_len.append(int(i.count(",")))
            no_of_paths+=1
            resi=i.replace(" ", "").split(',')
            try:
                length.append(int(resi.pop().replace(')', '').replace('(', '')))
            except ValueError:
                pass
            if "148" in resi or "485" in resi or "227" in resi or "564" in resi:
                for x in resi:
                    add_res(int(x))    
    if i[0:6]!="Number":
        aa_len.pop()
        length.pop()
        outfile.write(f"Number of paths is {no_of_paths} (unfinished)\n")
    avg = round(np.average(aa_len), 2)
    avg2 = round(np.average(length), 2)
    sd = round(s.stdev(aa_len), 2)
    sd2 = round(s.stdev(length), 2)
    outfile.write(f"Average path length (aminoacids): {avg}\nStandard deviation: {sd}\nAverage path length (nm): {avg2}\nStandard deviation: {sd2}\n")
    infile.readline()
    outfile.write("The most frequent/interesting residues:\n")
    for i in infile:
        if i[0:3]=="The":
            break
        line = ch_res(int(i[0:3])) + '\t' + i[3:]
        outfile.write(line)
    #outfile.write("Interesting residues:\n")
    for k,v in mut.items():
        ln=str(k)+'\t'+str(v) + '\n'
        outfile.write(ln)
    outfile.write('\n')
    outfile.write('\n')
    infile.close()

outfile.close()
sys.exit(f"Output succesfully written to the {out} file.")

