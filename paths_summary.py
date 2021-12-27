#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 21.07.2021

@author: Mateusz Fortunka
"""

import sys
import glob

if __name__ == "__main__":
    if len(sys.argv)!=2:
        sys.exit("Wrong number of arguments given. Correct syntax: psummary2.py path_to_folder")
    else:
        folder = sys.argv[1]


def calcnwrite(x , i , j):
    opt=x[j+2].rstrip("\n")
    no=[int(s) for s in x[j+3].split() if s.isdigit()]
    avg1=x[j+4][34:].rstrip("\n")
    sd1=x[j+5][20:].rstrip("\n")
    avg2=x[j+6][26:].rstrip("\n")
    sd2=x[j+7][20:].rstrip("\n")
    freq=''
    p=0
    while x[j+9+p] != "\n":
        res=x[j+9+p].rstrip("\n")
        freq+=res + '\t'
        p+=1
    freq=freq.rstrip(', ')
    line = f"{i}\t{opt}\t{no[0]}\t{avg1}\t{sd1}\t{avg2}\t{sd2}\t{freq}"
    outf.write(f"{line}\n")


files_list = [f for f in glob.glob(folder + "/*.txt", recursive=True)]
files_list = sorted(files_list)

summaries={}
nr=0
for f in files_list:
    infile = open(f, "r")
    summaries[f"{nr}"] = [infile.readlines()]
    infile.close()
    nr+=1

name = folder.rstrip('/').split('/')[-1]
out = folder + f"/{name}_summary.txt"
outf = open(out, "w")


for idx, val in enumerate(summaries["0"][0]):
    if val[0:6]=="Start:":
        start=val.rstrip("\n")
        end=summaries["0"][0][idx+1]
        outf.write(f"{start} - {end}")
        calcnwrite(summaries["0"][0], 0, idx)
        for k in summaries.keys():
            for li, lv in enumerate(summaries[k][0]):
                if lv==val and summaries[k][0][li+1]==summaries["0"][0][idx+1]:
                    calcnwrite(summaries[k][0], k, li)
            
outf.close()
