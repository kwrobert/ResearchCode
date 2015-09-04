#####################################################################################################
# Script: plot_planar_density.py 
# Author: Kyle Robertson
# Del Maestro Research Group
# Description: Creates all the planar density plots from data in reduced planar density files. 
#####################################################################################################

import argparse
import os
import subprocess 
import numpy as np
import pylab as pl
import mplrcparams

def main():
    parser = argparse.ArgumentParser(description='Plots multiple planar density estimator files')
    parser.add_argument('-p', metavar='Input Path',type=str,help='Path to reduced planar density file')
    parser.add_argument('-n',metavar='File Name',type=str,help='Name of planar density file')
    parser.add_argument('-o', metavar='Output Path',type=str,help='Path to desired output directory')
    parser.add_argument('-r',metavar='Reduction Variable',type=str,help='Variable planar density files are reduced over')
    parser.add_argument('-T',metavar='Temperature',type=str,help='Temperature of planar density plots')
    args = parser.parse_args()
    
    #name = args.n
    #reducevar = args.r
    #path = args.p
    #filepath = os.path.join(path,name)
    #reduceFile = open(filepath,'r')
    
    if args.r:
    # Reduce all plane density estimators over specified reduction variable
        print 'Reducing planar density files' 
        reductionvar = '-r '+str(args.r)
        cmd = 'python $HOME/local/pimcscripts/reduce-one.py '+reductionvar+' -e planedensity '+args.p
        subprocess.call(cmd,shell=True)
    
    #Move to directory of reduced plane density file
    os.chdir(args.p) 
    
    # Grab the reduced planar density file
    for fn in os.listdir(args.p):
        if os.path.isfile(fn):
            if ('planedensity' in fn) and ('reduce' in fn):
                name = fn 
                reducevar = name.split('-')[1]
                reduceFile = open(name,'r')
    
    # Get values of reduced variable 
    lines = reduceFile.readlines()
    reduceVals = lines[0].split() 
    reduceVals.pop(0)
    fixreduceVals = []
    for i in range(len(reduceVals)):
        if (reducevar not in reduceVals[i]) and ('=' not in reduceVals[i]):
            fixreduceVals.append(reduceVals[i])  
    print reduceVals 
    print fixreduceVals 
    reduceFile.close()
    
    # Grab data for each reduced variable value and plot
    ncount = 0
    densitycount = 1
    figcount = 1
    for i in fixreduceVals:
        print "Making density plot %i of %i" % (figcount, len(fixreduceVals))
        titlevar = i
        n, density = np.loadtxt(name, unpack=True, usecols=(ncount, densitycount))
        N = int(np.sqrt(density.shape[0]))
        density = density.reshape([N,N])
        density = density.transpose()
        pl.figure(figcount)
        pl.imshow(density,cmap='BuGn',extent=[0,18,0,18],vmin=0,vmax=.5)
        pl.xlabel("X " + r"$(\AA)$",fontsize=20)
        pl.ylabel("Y " + r"$(\AA)$",fontsize=20)
        pl.xticks(pl.arange(0,18,1),range(0,18))
        pl.yticks(pl.arange(0,18,1),range(0,18))
        #pl.axis([0, 18, 0, 18])
        cbar = pl.colorbar()
        cbar.set_label("Number Density"+ r"$\left(\AA^{-3}\right)$",labelpad=30,fontsize=20,rotation=270)
        pl.title( r"$%s = %s K$"%(reducevar, titlevar),fontsize=24)
        i = i.rstrip('00')
        i = i.rstrip('.')
        pl.savefig(args.o+'%splanardensityplot_'%args.T+reducevar+'=%s.pdf'%i,format='pdf')
        pl.close()
        print "Finished making density plot %i of %i" % (figcount, len(fixreduceVals))
        ncount += 3
        densitycount += 3
        figcount += 1
        
if __name__=='__main__':
    main() 
