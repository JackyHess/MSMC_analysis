#! /usr/bin/env python

# Run MSMC analysis using the input generated with "prepare_MSMC_input.py"
# Assume that 12 processors are available, if not change option -t accordingly

import os

from subprocess import *

def run_MSMC(input_dir):

    inp_files = os.listdir(input_dir)
    
    
    cmd = "msmc -t 12 -o msmc_out "
    for i_file in inp_files:
        if os.path.getsize(input_dir+"/"+i_file) > 0:
            cmd += input_dir+"/"+i_file+" "
    call(cmd, shell=True)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 2:
        run_MSMC(sys.argv[1])
    else:
        print "run_MSMC(input_dir)"
    
    
