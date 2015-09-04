#####################################################################################################
# Script: check_convergence.py
# Author: Kyle Robertson
# Del Maestro Research Group
# Description: Simple script for plotting all the energy vs. bin numbers for a particular job run
# to check convergence for each parameter set. Just opens window of plot and does not save plot to 
# a file. 
#####################################################################################################


import argparse
import os
import glob
import subprocess 
import numpy as np
import matplotlib.pyplot as plt

def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually
    would at the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    
def makeplots():
    print 'Making plots'
    print os.getcwd()
    sh('python /Users/Kyle/local/pimcscripts/KWR/pimcplot.py -e E gce-estimator*')
    
    
def main():
    parser = argparse.ArgumentParser(description='Creates and saves a bunch of energy vs. bin number plots for checking convergence')
    parser.add_argument('parentdir',type=str,help='Parent directory of run containing subdirectories of data files')
    args = parser.parse_args()
    pdir = args.parentdir
    
    # Loop through all subdirectories under the parent directory
    for item in os.listdir(pdir):
        if os.path.isdir(item):
            # if OUTPUT exists, cd into it and begin plotting
            if 'OUTPUT' in os.listdir(os.path.join(pdir,item)):
                print 'Found output'
                os.chdir(os.path.join(pdir,item)+'/OUTPUT')
                makeplots()
                os.chdir(pdir)
            else:
                os.chdir(os.path.join(pdir,item))
                makeplots()
                os.chdir(pdir)
            
    
if __name__=='__main__':
    main()
