#! /bin/bash

#SBATCH --account=uio
#SBATCH -t 1000
#SBATCH --partition=lowpri
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4000

module load bcftools
module load python3

python /usit/abel/u1/jacqueh/Code/Population_genomics/prepare_MSMC_input.py Abrun_genome_alignment_sorted.bam Abrun_final.assembly.fasta 26 Abrun_final.assembly.genome .


python /usit/abel/u1/jacqueh/Code/Population_genomics/prepare_MSMC_input.py Abrun_final.assembly.genome . mapping_mask/
