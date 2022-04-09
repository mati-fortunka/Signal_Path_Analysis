#!/bin/bash -l
#SBATCH --job-name="path3_a"
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem 8gb
#SBATCH --partition=ogr
#SBATCH --exclusive

./gncommunities contact.dat communities.out

./subopt contact.dat A_L185-A_G79.out 20 42 148
./subopt contact.dat A_L185-A_H91.out 20 54 148
./subopt contact.dat B_F185-B_G79.out 20 482 588
/subopt contact.dat B_F185-B_H91.out 20 494 588

/subopt contact.dat A_D264-A_G79.out 20 42 227
./subopt contact.dat A_D264-A_H91.out 20 54 227
./subopt contact.dat B_D264-B_G79.out 20 482 667
./subopt contact.dat B_D264-B_H91.out 20 494 667

./subopt contact.dat B_F185-A_G79.out 20 42 588
./subopt contact.dat B_F185-A_H91.out 20 54 588

