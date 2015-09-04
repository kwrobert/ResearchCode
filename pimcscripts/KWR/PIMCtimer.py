# -*- coding: utf-8 -*-

#####################################################################################################
# Script: PIMCtimer.py
# Author: Kyle Robertson
# Del Maestro Research Group
# Description: A script for timing the PIMC code for a generic set of parameter to determine if the 
# lookup table actually reduces run time and improves performance. 
#####################################################################################################



import subprocess as sub
import shutil as sh
import time
import sys
import numpy as np
import os

def main():
    # Get the arguments to the PIMC code
    args = '-T 2.0 -n 0.0182 -r 6 -b cylinder -L 30 -t 0.004 -I aziz -X hex_tube -l 7 -u -7.2 -M 8 -S 1000 -E 250 —action primitive —relax'
    
    # Get the paths to the two executables we are comparing
    path1 = '/Users/Kyle/local/PIMC/pimc.e '
    path2 = '/Users/Kyle/local/PIMCNoLookup/pimc.e '
    
    # Create commands for subprocess
    cmd1 = path1 + args
    cmd2 = path2 + args
    
    # Create a null file to catch all the pesky PIMC output 
    null = open(os.devnull, 'w')
    
    # Time the second process
    process2cpu = np.array([])
    process2wall = np.array([])
    print '########## Timing w/o Lookup Table #############'
    for i in range(5):
        print "Iteration %i" % (i+1)
        WALLstart2 = time.time()
        CPUstart2 = time.clock()
        sub.call(cmd2, shell=True)
        #sub.call(cmd2, shell=True, stdout = null)
        #sub.call(cmd2, stdout = null)
        CPUend2 = time.clock()
        WALLend2 = time.time()
        sh.rmtree('/Users/Kyle/local/PythonScripts/OUTPUT')
        walltime2 = WALLend2 - WALLstart2
        cputime2 = CPUend2 - CPUstart2
        print "The CPU time was %5.4f" % cputime2
        print 'The wall time was %5.4f' % walltime2
        sys.stdout.flush()
        process2cpu = np.append(process2cpu,cputime2)
        process2wall = np.append(process2wall,walltime2)
    
    # Time the first process
    process1cpu = np.array([])
    process1wall = np.array([])
    print '########## Timing w/ Lookup Table #############'
    for i in range(5):
        print "Iteration %i" % (i+1)
        WALLstart1 = time.time()
        CPUstart1 = time.clock()
        sub.call(cmd1, shell=True)
        #sub.call(cmd1, shell=True, stdout = null)
        CPUend1 = time.clock()
        WALLend1 = time.time()
        sh.rmtree('/Users/Kyle/local/PythonScripts/OUTPUT')
        walltime1 = WALLend1 - WALLstart1
        cputime1 = CPUend1 - CPUstart1
        print "The CPU time was %5.4f" % cputime1
        print 'The wall time was %5.4f' % walltime1
        sys.stdout.flush()
        process1cpu = np.append(process1cpu,cputime1)
        process1wall = np.append(process1wall,walltime1)
    
    # Compute some average times
    wallavg1 = np.average(process1wall)
    cpuavg1 = np.average(process1cpu)
    print '---------- Lookup ----------'
    print 'The average wall time was %5.4f' % wallavg1
    print 'The average CPU time was %5.4f' % cpuavg1
    
    wallavg2 = np.average(process2wall)
    cpuavg2 = np.average(process2cpu)
    print '---------- No Lookup ----------'
    print 'The average wall time was %5.4f' % wallavg2
    print 'The average CPU time was %5.4f' % cpuavg2
    
    cpuspeedup = cpuavg2 - cpuavg1
    wallspeedup = wallavg2 - wallavg1
    print '\nSo the lookup table is faster by %5.4f CPU seconds and %5.4f wall seconds' % (cpuspeedup, wallspeedup)
    print '\n The lookup table is faster by a factor of %5.4f' % (wallavg2/wallavg1)
    
if __name__=='__main__':
    main()
