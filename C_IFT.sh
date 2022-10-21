#!/bin/sh

#SBATCH -p i8cpu
#SBATCH -N 8
#SBATCH -n 128
#SBATCH -c 8
#SBATCH -t 00:30:00
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-user=naofuji.1220@gmail.com

source /home/issp/materiapps/intel/lammps/lammpsvars.sh

python3 generate.py
srun lammps < interface_tension.input
