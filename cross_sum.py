#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 1.09.2021

@author: Mateusz Fortunka

Program show differences beetween paths in native protein and the one with mutations. Minus sign in values shows that parameter of path in mutated protein is bigger.

"""
import sys
import numpy as np
import statistics as s

if __name__ == "__main__":
    if len(sys.argv)!=3:
        sys.exit("Wrong number of arguments given. Correct syntax: cross_sum.py first_file second_file")
    else:
        file1 = sys.argv[1]
        file2 = sys.argv[2]

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

out = file1.rstrip(".txt") + '-' + file2.split('/')[-1]
infile = open(file1, "r")
lines1 = infile.readlines()
infile.close()
infile = open(file2, "r")
lines2 = infile.readlines()
infile.close()

j=0
for j in range(len(lines2)):
    lines2[j]=lines2[j].replace("Start: A_LEU_185", "Start: A_PHE_185")
    lines2[j]=lines2[j].replace("Start: B_ASP_265", "Start: B_GLU_264")
    lines2[j]=lines2[j].replace("End: A_LEU_185", "End: A_PHE_185")
    lines2[j]=lines2[j].replace("End: B_ASP_265", "End: B_GLU_264")

outfile = open(out, "w")
outfile.write("Name of path\t Opt. id. [%]\t st. dev. [%]\t Opt. id. rev. [%]\t st. dev. [%]\t diff in no. of paths\t st. dev.\t diff. in length [aa]\t st. dev.\t diff. in length [nm]\t st. dev.\t diff. A_FL\t st. dev.\t diff. B_F\t st. dev.\t diff. A_E\t st. dev.\t diff. B_ED\t st. dev.\n")

i=0
for i in range(len(lines1)//6):
    name = lines1[i*6].rstrip("\n")
    check(name[0], 'S', i*6+1)
    id_2=lines2.index(name + '\n')
    path1={}
    path2={}
    optimal1=[]
    optimal2=[]
    number=[]
    len_aa=[]
    len_nm=[]
    A_FL=[]
    B_F=[]
    A_E=[]
    B_ED=[]
    for x in range(1,6):
        path1[f"{x}"]=[lines1[i*6+x].split('\t')]
        check(lines1[i*6+x][0], f'{x-1}', i*6+x)
        opt1 = path1[f"{x}"][0][1].split(',')
        optimal1.append(opt1[1:len(opt1)-1])

        path2[f"{x}"]=[lines2[id_2+x].split('\t')]
        check(lines2[id_2+x][0], f'{x-1}', id_2+x)
        opt2 = path2[f"{x}"][0][1].split(',')
        optimal2.append(opt2[1:len(opt2)-1])

        number.append(int(path1[f"{x}"][0][2])-int(path2[f"{x}"][0][2]))
        len_aa.append(float(path1[f"{x}"][0][3])-float(path2[f"{x}"][0][3]))
        len_nm.append(float(path1[f"{x}"][0][5])-float(path2[f"{x}"][0][5]))
        A_FL.append(int(path1[f"{x}"][0][-8])-int(path2[f"{x}"][0][-8]))
        B_F.append(int(path1[f"{x}"][0][-6])-int(path2[f"{x}"][0][-6]))
        A_E.append(int(path1[f"{x}"][0][-4])-int(path2[f"{x}"][0][-4]))
        B_ED.append(int(path1[f"{x}"][0][-2])-int(path2[f"{x}"][0][-2]))
    similarity1=[]
    similarity2=[]   
    for y in range(5):
        temp1=[]
        temp2=[]
        for z in range(5):
            wynik1=100*len(set(optimal1[y]).intersection(optimal2[z]))/len(set(optimal1[y]))
            temp1.append(wynik1)
            wynik2=100*len(set(optimal2[z]).intersection(optimal1[y]))/len(set(optimal2[z]))
            temp2.append(wynik2)
        similarity1.append(np.average(temp1))
        similarity2.append(np.average(temp2))
    
    sim1_avg = round(np.average(similarity1), 2)
    sim1_sd = round(s.stdev(similarity1), 2)
    sim2_avg = round(np.average(similarity2), 2)
    sim2_sd = round(s.stdev(similarity2), 2)
    num_avg = round(np.average(number), 2)
    num_sd = round(s.stdev(number), 2)
    aa_avg = round(np.average(len_aa), 2)
    aa_sd = round(s.stdev(len_aa), 2)
    nm_avg = round(np.average(len_nm), 2)
    nm_sd = round(s.stdev(len_nm), 2)
    A_FL_avg = round(np.average(A_FL), 2)
    A_FL_sd = round(s.stdev(A_FL), 2)
    B_F_avg = round(np.average(B_F), 2)
    B_F_sd = round(s.stdev(B_F), 2)
    A_E_avg = round(np.average(A_E), 2)
    A_E_sd = round(s.stdev(A_E), 2)
    B_ED_avg = round(np.average(B_ED), 2)
    B_ED_sd = round(s.stdev(B_ED), 2)    
    outfile.write(f"{name}\t{sim1_avg}\t{sim1_sd}\t{sim2_avg}\t{sim2_sd}\t{num_avg}\t{num_sd}\t{aa_avg}\t{aa_sd}\t{nm_avg}\t{nm_sd}\t{A_FL_avg}\t{A_FL_sd}\t{B_F_avg}\t{B_F_sd}\t{A_E_avg}\t{A_E_sd}\t{B_ED_avg}\t{B_ED_sd}\n")
    
outfile.write('\n')
outfile.close()
sys.exit(f"Output succesfully written to the {out} file.")

