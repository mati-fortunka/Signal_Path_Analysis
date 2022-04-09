#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 1.09.2021

@author: Mateusz Fortunka
"""
import sys
import numpy as np
import statistics as s

if __name__ == "__main__":
    if len(sys.argv)!=3:
        sys.exit("Wrong number of arguments given. Correct syntax: in_sum.py path_to_file no_of_repetitions")
    else:
        file = sys.argv[1]
        reps = int(sys.argv[2]) + 1

def ch_res(rs1, rs2):
    if rs1 == rs2:
        return(1)
    elif (rs1 == "A_PHE_185" or rs1 == "A_LEU_185") and (rs2 == "A_PHE_185" or rs2 == "A_LEU_185"):
        return(1) 
    elif (rs1 == "B_GLU_264" or rs1 == "B_ASP_265") and (rs2 == "B_GLU_264" or rs2 == "B_ASP_265"):
        return(1)
    else:
        return(0)
    
def check(a, b, no):
    if a != b:
        print(f"Program encountered problem with file structure at line {no}.")


out = file.rstrip(".txt") + "_in.txt"
infile = open(file, "r")
lines = infile.readlines()
infile.close()
outfile = open(out, "w")
outfile.write("Name of path\t Opt. id. [%]\t st. dev. [%]\t No. of paths\t st. dev.\t length [aa]\t st. dev.\t length [dist]\t st. dev.\t A_FL\t st. dev.\t B_F\t st. dev.\t A_E\t st. dev.\t B_ED\t st. dev.\n")

for i in range(len(lines)//reps):
    name = lines[i*reps].rstrip("\n")
    check(name[0:6], 'Start:', i*reps+1)
    path={}
    optimal=[]
    number=[]
    len_aa=[]
    len_d=[]
    A_FL=[]
    B_F=[]
    A_E=[]
    B_ED=[]
    similarity=[]
    for x in range(1,reps):
        path[f"{x}"]=[lines[i*reps+x].split('\t')]
        check(lines[i*reps+x][0], f'{x-1}', i*reps+x)
        opt = path[f"{x}"][0][1].split(',')
        optimal.append(opt[1:len(opt)-1])
        number.append(int(path[f"{x}"][0][2]))
        len_aa.append(float(path[f"{x}"][0][3]))
        len_d.append(float(path[f"{x}"][0][5]))
        A_FL.append(int(path[f"{x}"][0][-8]))
        B_F.append(int(path[f"{x}"][0][-6]))
        A_E.append(int(path[f"{x}"][0][-4]))
        B_ED.append(int(path[f"{x}"][0][-2]))
    for y in range(reps-1):
        temp=[]
        for z in range(reps-1):
            if z!=y:
                wynik=100*len(set(optimal[y]).intersection(optimal[z]))/len(set(optimal[y]))
                temp.append(wynik)
        similarity.append(np.average(temp))        
    sim_avg = round(np.average(similarity), 2)
    sim_sd = round(s.stdev(similarity), 2)
    num_avg = round(np.average(number), 2)
    num_sd = round(s.stdev(number), 2)
    aa_avg = round(np.average(len_aa), 2)
    aa_sd = round(s.stdev(len_aa), 2)
    d_avg = round(np.average(len_d), 2)
    d_sd = round(s.stdev(len_d), 2)
    A_FL_avg = round(np.average(A_FL), 2)
    A_FL_sd = round(s.stdev(A_FL), 2)
    B_F_avg = round(np.average(B_F), 2)
    B_F_sd = round(s.stdev(B_F), 2)
    A_E_avg = round(np.average(A_E), 2)
    A_E_sd = round(s.stdev(A_E), 2)
    B_ED_avg = round(np.average(B_ED), 2)
    B_ED_sd = round(s.stdev(B_ED), 2)    
    outfile.write(f"{name}\t{sim_avg}\t{sim_sd}\t{num_avg}\t{num_sd}\t{aa_avg}\t{aa_sd}\t{d_avg}\t{d_sd}\t{A_FL_avg}\t{A_FL_sd}\t{B_F_avg}\t{B_F_sd}\t{A_E_avg}\t{A_E_sd}\t{B_ED_avg}\t{B_ED_sd}\n")
    
outfile.write('\n')
outfile.close()
sys.exit(f"Output succesfully written to the {out} file.")
