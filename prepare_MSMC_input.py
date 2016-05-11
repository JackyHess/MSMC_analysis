#! /usr/bin/env python

import os

from subprocess import *

def call_SNPS_and_make_mask(input_bam, ref_fasta, seq_depth, genome_file, output_dir):

    if not os.path.exists(output_dir+"/masks"):
        os.mkdir(output_dir+"/masks")

    if not os.path.exists(output_dir+"/vcf"):
        os.mkdir(output_dir+"/vcf")

    cmd = "samtools index "+input_bam
    call(cmd, shell=True)
    
    fp_in = open(genome_file, "r")
    lines = fp_in.readlines()
    fp_in.close()

    scaffolds = []
    for line in lines:
        scaffolds.append(line.split()[0])
    
    for scaffold in scaffolds:
        cmd = "samtools mpileup -q 20 -Q20 -C 50 -g -r "+scaffold+" -f "+ref_fasta+" "+input_bam+" | bcftools call -c | /usit/abel/u1/jacqueh/Software/msmc-tools/bamCaller.py "+seq_depth+" "+output_dir+"/masks/"+scaffold+"_mask.bed.gz | bcftools view -O z > "+output_dir+"/vcf/"+scaffold+".vcf"
        call(cmd, shell=True)


def make_hetstep(genome_file, input_dir, mappability_dir):

    fp_in = open(genome_file, "r")
    lines = fp_in.readlines()
    fp_in.close()

    if not os.path.exists(input_dir+"/input"):
        os.mkdir(input_dir+"/input")

    scaffolds = []
    for line in lines:
        scaffolds.append(line.split()[0])

    for scaffold in scaffolds:
        # little hack to fix the issue that if the mask file does not have the correct file ending ".bed.gz" the script won't work
        if os.path.exists(input_dir+"/masks/"+scaffold+".mask"):
            cmd = "mv "+input_dir+"/masks/"+scaffold+".mask "+input_dir+"/masks/"+scaffold+"_mask.bed.gz"
            call(cmd, shell=True)
        
        # a mask file is only generated if there are SNPs on the scaffold, so need to check if mask file is present before processing
        if os.path.exists(input_dir+"/masks/"+scaffold+"_mask.bed.gz"):
            cmd = "/usit/abel/u1/jacqueh/Software/msmc-tools/generate_multihetsep.py --mask="+input_dir+"/masks/"+scaffold+"_mask.bed.gz --mask="+mappability_dir+"/chr"+scaffold+".mask.bed.gz vcf/"+scaffold+".vcf > "+input_dir+"/input/"+scaffold+"_msmc_input.txt"
            call(cmd, shell=True)

if __name__ == '__main__':

    import sys

    if len(sys.argv) == 6:
        call_SNPS_and_make_mask(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
    elif len(sys.argv) == 4:
        make_hetstep(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print "call_SNPS_and_make_mask(input_bam, ref_fasta, seq_depth, genome_file, output_dir)"
        print "make_hetstep(genome_file, input_dir, mappability_dir)"
