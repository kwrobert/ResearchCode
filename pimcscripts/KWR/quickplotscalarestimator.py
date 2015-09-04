import numpy as np
import matplotlib.pyplot as plt
import argparse
import mplrcparams

def main():
    parser = argparse.ArgumentParser(description='''Plots scalar estimator files''')
    parser.add_argument('-e','--estimator',dest='e',type=str,help='''Estimator to be plotted''')
    parser.add_argument('reducefiles',type=str,nargs='+',help='''List of reduced estimator files''')
    parser.add_argument('-l, --label',type=str,dest='label',action='append',help='''Label for reduced estimator files''')
    args=parser.parse_args()
    
    est = args.e
    labels = args.label
    xlists = []
    ylists = []
    errlists = []
    for reducefile in args.reducefiles:
        # Find the estimator in the header
        fn = open(reducefile,'r')
        headers = fn.readlines()[0]
        fn.close()
        headers = headers.split()
        headers.pop(0)
        col = headers.index(est)
        xvals, yvals, err = np.loadtxt(reducefile,unpack=True,usecols=(0,col,col+1))
        xlists.append(xvals)
        ylists.append(yvals)
        errlists.append(err)
        
    for i in range(len(xlists)):
        xlist = xlists[i]
        ylist = ylists[i]
        errlist = errlists[i] 
        xlist, ylist, errlist = (list(t) for t in zip(*sorted(zip(xlist, ylist,errlist))))
        xlists[i] = xlist
        ylists[i] = ylist
        errlists[i] = errlist
        
    plt.figure()
    for i in range(len(xlists)):
        plt.plot(xlists[i],ylists[i],label=labels[i])
        plt.errorbar(xlists[i],ylists[i],yerr=errlists[i],fmt=None,color='crimson')
        #plt.errorbar(xlists[i],ylists[i],yerr=errlists[i],fmt=None,label=labels[i])
        
    plt.xlabel("Chemical Potential [K]")
    plt.ylabel(r"E/N [K]")
    plt.legend(loc='best')
    #plt.title("Density vs. Chemical Potential")
    plt.show()
        
    
if __name__=='__main__':
    main()
