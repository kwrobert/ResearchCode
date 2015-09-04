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
    
def main():
    
    parser = argparse.ArgumentParser(description='quickie')
    parser.add_argument('parentdir',type=str,help='Parent directory of run containing subdirectories of data files')
    args = parser.parse_args()
    pdir = args.parentdir
    
    # Loop through all subdirectories under the parent directory
    for item in os.listdir(pdir):
        if os.path.isdir(os.path.join(pdir,item)):
            # if OUTPUT exists, cd into it and begin plotting
            if 'OUTPUT' in os.listdir(os.path.join(pdir,item)):
                print 'Found output'
                os.chdir(os.path.join(pdir,item)+'/OUTPUT')
                try:
                    os.mkdir('donotdelete')
                except OSError:
                    None
                supers = glob.glob('gce-super*')
                for supfile in supers:
                    ID = supfile[-13:]
                    newfiles = glob.glob('*%s'%ID)
                    for newfile in newfiles:
                        sh('mv %s donotdelete'%newfile)
                sh('rm *.dat')
                os.chdir(pdir)
            else:
                None
                
if __name__=='__main__':
    main() 