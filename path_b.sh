#!/bin/bash -l
#SBATCH --job-name="path3_b"
#SBATCH --nodes=1
#SBATCH --ntasks=6
#SBATCH --mem 8gb
#SBATCH --partition=ogr
#SBATCH --exclusive

./subopt contact.dat A_L185-B_G79.out 20 148 482
./subopt contact.dat A_L185-B_H91.out 20 148 494

./subopt contact.dat B_D264-A_G79.out 20 42 667
./subopt contact.dat B_D264-A_H91.out 20 54 667
./subopt contact.dat A_D264-B_G79.out 20 227 482
./subopt contact.dat A_D264-B_H91.out 20 227 494

./subopt contact.dat A_L185-B_F185.out 20 148 588
./subopt contact.dat A_D264-B_D264.out 20 227 667
./subopt contact.dat A_L185-B_D264.out 20 148 667
./subopt contact.dat A_D264-B_F185.out 20 227 588
