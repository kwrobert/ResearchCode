#####################################################################################################
# Script: trimplots.py
# Author: Kyle Robertson
# Del Maestro Research Group
# Description: A simple script to trim whitespace off the edges of plots saved by matplotlib.
# Requires some image processing command line utilities to be installed.  
#####################################################################################################

import argparse
import glob 
import os
import subprocess

def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually would at 
    the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]

def main():
    parser = argparse.ArgumentParser(description='''Trims whitespace from edges of plots''')
    parser.add_argument('-p','--path',type=str,help='''Path to image files that need to be trimmed, always add trailing slash.''')
    parser.add_argument('-t','--type',type=str,help='''File extension, always include the dot.''')
    args = parser.parse_args()
    
    os.chdir(args.path)
    pdfs = glob.glob('*.pdf')
    for i, pdf in enumerate(pdfs):
        print "Trimming plot %i of %i"%(i+1, len(pdfs))
        pdfnoext = pdf[0:-4]
        sh('convert -quality 00 -density 400x400 -trim %s %s.png'%(pdf,pdfnoext)) 
        #sh('convert -quality 100 -density 400x400 -trim %s.png %s'%(pdfnoext,pdf)) 
    
if __name__=='__main__':
    main()
