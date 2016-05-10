# MSMC_analysis
Scripts to run MSMC on genomes with large numbers of scaffolds

## Input requirements

**Data**

- Read alignment in .bam format, coordinate sorted
- Genome sequence (.fa)

**Software**

- MSMC https://github.com/stschiff/msmc 
- MSMC tools https://github.com/stschiff/msmc-tools
- Samtools (> v1.1) and BCFtools http://www.htslib.org/
- Bedtools https://github.com/arq5x/bedtools2/releases
- SNPable http://lh3lh3.users.sourceforge.net/snpable.shtml

## Data preparation

### Determine coverage distribution of the aligned sample

Make genome index file for Bedtools

`python get_sequence_lengths.py final.assembly.fasta final.assembly.genome`

Get coverage distribution of aligned sample

`bedtools genomecov -ibam alignment_sorted.bam -g final.assembly.genome > <sample_id>.genomecov_summary`

Plot coverage distributions in R to determine coverage peak and whether there is any indication of heterozygous regions included in the assembly. 

_Good sample_

![SL468_coverage.jpeg](SL468_coverage.jpeg)

One single peak around 65x.

### Prepare MSMC input files

Generate single sample VCF and mask files from .bam


Make mappability mask (according to http://lh3lh3.users.sourceforge.net/snpable.shtml)

`splitfa final.assembly.fasta 250 | split -l 20000000`

Choose a kmer number to reflect the library type you are using for alignment. For paired-ed libraries this is a bit tricky, since this was conceptualised for single end libraries, but since my libraries are narrow 100bp PE libraries, I chose 250 which is on the liberal end.





















