import os,sys,glob
import loadgmt,kevent
import pimchelp
import MCstat
import argparse
import numpy as np
import matplotlib.pyplot as plt
import subprocess

# Reduce and average results for a single PIMC run based on a single parameter
# which varies.  This could be density for fixed system size, etc.

# ----------------------------------------------------------------------
def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually would at 
    the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    
# ----------------------------------------------------------------------
def getScalarStats(data,weights,mergedstatus,dim=0):
    ''' Get the average and error of all columns in the data matrix for a scalar
    estimator.'''
    if data.ndim > dim: 
        if mergedstatus:
            # Columns alternate between actual data and their variances
            dataArray = data[:,0::2]
            varArray = data[:,1::2]
            # Compute the standard error using the variances (requires unflattened
            # weights array
            dataErr = np.sqrt(np.sum(varArray*weights**2,dim)/(np.sum(weights,0))**2)
            # Average all the data (requires flattened weights array)
            weights=weights.flatten()
            dataAve = np.average(dataArray,dim,weights=weights)
        else: 
            weights=weights.flatten()
            numBins  = np.size(data,dim) 
            dataAve  = np.average(data,dim,weights=weights) 
            dataAve2 = np.average(data*data,dim,weights=weights)
            bins = MCstat.bin(data)
            dataErr = np.amax(bins,axis=0)
            dataErr2 = np.sqrt( abs(dataAve2-dataAve**2)/(1.0*numBins-1.0) ) 

    else:
        dataAve = data
        dataErr = 0.0*data

    return dataAve,dataErr
# ----------------------------------------------------------------------
def getVectorStats(data,weights,mergedstatus,dim=0):
    ''' Get the average and error of all columns in the data matrix for a vector 
    estimator.'''

    if data.ndim > dim: 
        if mergedstatus:
            numBins  = np.size(data,dim) 
            # Average all the data (requires flattened weights array)
            weights=weights.flatten()
            dataAve = np.average(data,dim,weights=weights)
            dataAve2 = np.average(data*data,dim,weights=weights)
            # For a vector estimator get the error the usual way, ignoring the 
            # weights. This introduces a slight inaccurary in error bars but saves
            # a lot of time and effort 
            
            # MC stat will not work unless you have more than 32 random seeds.
            # The binning analysis done in MCstat is for a long run of correlated 
            # bins. However, for a merged file all "bins" (avrgs of random seeds)
            # are completetely uncorrelated so we don't even need to do the binning 
            # analysis 
            
            #bins = MCstat.bin(data)
            #dataErr = np.amax(bins,axis=0)
            dataErr = np.sqrt( abs(dataAve2-dataAve**2)/(1.0*numBins-1.0) ) 
        else: 
            weights  = weights.flatten()
            numBins  = np.size(data,dim) 
            dataAve  = np.average(data,dim,weights=weights) 
            dataAve2 = np.average(data*data,dim,weights=weights)
            bins = MCstat.bin(data)
            dataErr = np.amax(bins,axis=0)
            dataErr2 = np.sqrt( abs(dataAve2-dataAve**2)/(1.0*numBins-1.0) ) 

    else:
        dataAve = data
        dataErr = 0.0*data

    return dataAve,dataErr
# -----------------------------------------------------------------------------
def getScalarEst(type,pimc,outName,reduceFlag, skip=0):
    ''' Return the arrays containing the reduced averaged scalar
        estimators in question.'''
    
    # Get the files corresponding to this particular estimator
    fileNames = pimc.getFileList(type)
    
    # Grab the headers from the data files
    for i in range(len(fileNames)):
        fileNames[i]=pimc.baseDir+fileNames[i]
    headers   = pimchelp.getHeadersFromFile(fileNames[0])
    
    # If the last header is "bins", we are dealing with a MERGED file and must 
    # handle things appropriately
    if headers[-1] == 'bins':
        merged = True
        # Remove the bins header at the end because it is unecessary in a reduced file
        headers.pop(-1)
        # Remove all the "variance" headers because these are also unneccessary 
        headers = filter(lambda string: string != "variance", headers)
    else: 
        merged = False
        
    ave = np.zeros([len(fileNames),len(headers)],float)
    err = np.zeros([len(fileNames),len(headers)],float)
    
    if merged:
        # Compute the averages and error using appropriate weighting
        for i,fname in enumerate(fileNames):
            # Grab the file data
            filedata = np.loadtxt(fname,ndmin=2,skiprows=skip+2) # Skip number of bins user specified +2 for the two comment rows
            # All the data is in the first through 2nd to last columns for a merged file
            data = np.array_split(filedata,[filedata.shape[1]-1,filedata.shape[1]],axis=1)[0]
            # The weights are the last column
            weights = np.array_split(filedata,[filedata.shape[1]-1,filedata.shape[1]],axis=1)[1]
            # Pass getStats the data and weights and get the averages and errors
            ave[i,:],err[i,:] = getScalarStats(data,weights,merged)
    else: 
        # Compute the averages and errors as usual 
        for i,fname in enumerate(fileNames):
            # Grab the data
            data = np.loadtxt(fname,ndmin=2,skiprows=skip+2) # Skip number of bins user specified +2 for the two comment rows
            # The file isn't a merged file so give np.average None for weights in getStats and all weights will be 1
            weights = None
            ave[i,:],err[i,:] = getScalarStats(data,weights,merged)

    # output the estimator data to disk
    outFile = open(pimc.baseDir+'%s-%s' % (type,outName),'w');

    # the headers
    outFile.write('#%15s' % reduceFlag[0])
    for head in headers:
        outFile.write('%16s%16s' % (head,'+/-'))
    outFile.write('\n')

    # the data
    for i,f in enumerate(fileNames):
        outFile.write('%16.8E' % float(pimc.params[pimc.id[i]][reduceFlag[1]]))
        for j,h in enumerate(headers):
            outFile.write('%16.8E%16.8E' % (ave[i,j],err[i,j]))
        outFile.write('\n')
    outFile.close()

    return headers,ave,err;

# -----------------------------------------------------------------------------
def getVectorEst(type,pimc,outName,reduceFlag,xlab,ylab, skip=0):
    ''' Return the arrays consisting of the reduec averaged vector 
        estimators. '''

    fileNames = pimc.getFileList(type)
    try:
        # Grab the headers from the data files
        for i in range(len(fileNames)):
            fileNames[i]=pimc.baseDir+fileNames[i]
        headers   = pimchelp.getHeadersFromFile(fileNames[0])
        
        # If the last header is "bins", we are dealing with a MERGED file and must 
        # handle things appropriately
        if headers[-1] == 'bins':
            merged = True
            # Remove the bins header at the end because it is unecessary in a reduced file
            headers.pop(-1)
        else: 
            merged = False 
        
    
        numParams = len(fileNames)
        Nx = len(headers)
    
        x   = np.zeros([numParams,Nx],float)
        ave = np.zeros([numParams,Nx],float)
        err = np.zeros([numParams,Nx],float)
    
        if merged:
            # Compute the averages and errors using appropriate weighting 
            for i,fname in enumerate(fileNames):
                # Grab the file data
                filedata = np.loadtxt(fname,ndmin=2,skiprows=skip+2) # Skip number of bins user specified +2 for the two column rows
                # All the data is in the first through 2nd to last columns for a merged file
                data = np.array_split(filedata,[filedata.shape[1]-1,filedata.shape[1]],axis=1)[0]
                # The weights are the last column
                weights = np.array_split(filedata,[filedata.shape[1]-1,filedata.shape[1]],axis=1)[1]
                # Pass getStats the data and weights and get the averages and errors
                ave[i,:],err[i,:] = getVectorStats(data,weights,merged)
                    
                # get the headers
                headers2 = pimchelp.getHeadersFromFile(fname)
                headers2.pop(-1)
                x[i,:] = headers2
    
                # Compute the normalized averages and error for the OBDM
                if type == 'obdm':
                    norm = ave[i,0]
                    ave[i,:] /= norm
                    err[i,:] /= norm
        else: 
            # Compute averages and errors as usual
            data = np.loadtxt(fname,ndmin=2)[skip:,:]
            ave[i,:],err[i,:] = getVectorStats(data)
    
            # get the headers
            x[i,:] = pimchelp.getHeadersFromFile(fname)
    
            # Compute the normalized averages and error for the OBDM
            if type == 'obdm':
                norm = ave[i,0]
                ave[i,:] /= norm
                err[i,:] /= norm
    
        # output the vector data to disk
        outFile = open(pimc.baseDir+'%s-%s' % (type,outName),'w');
    
        # the headers
        lab = '%s = %4.2f' % (reduceFlag[0],float(pimc.params[pimc.id[0]][reduceFlag[1]])) # error is happening here. 'List index out of range' cuz id is empty
        outFile.write('#%15s%16s%16s' % ('',lab,''))
        for j in range(numParams-1):
            lab = '%s = %4.2f' % (reduceFlag[0],float(pimc.params[pimc.id[j+1]][reduceFlag[1]]))
            outFile.write('%16s%16s%16s' % ('',lab,''))
        outFile.write('\n')
        outFile.write('#%15s%16s%16s' % (xlab,ylab,'+/-'))
        for j in range(numParams-1):
            outFile.write('%16s%16s%16s' % (xlab,ylab,'+/-'))
        outFile.write('\n')
    
        # the data
        for i,h in enumerate(headers):
            for j in range(numParams):
                outFile.write('%16.8E%16.8E%16.8E' % (x[j,i],ave[j,i],err[j,i]))
            outFile.write('\n')
        outFile.close()
        return x,ave,err

    except:
        print 'Problem Reducing %s files' % type
        return 0,0,0


# -----------------------------------------------------------------------------
def getKappa(pimc,outName,reduceFlag,skip=0):
    ''' Return the arrays containing the reduced averaged compressibility. '''

    fileNames = pimc.getFileList('estimator')
    headers   = pimchelp.getHeadersFromFile(fileNames[0])

    aveKappa = np.zeros([len(fileNames)],float)
    errKappa = np.zeros([len(fileNames)],float)

    for i,fname in enumerate(fileNames):

        # Now get the temperature, volume and linear system size
        ID = pimc.getID(fname)
        T = float(pimc.params[ID]['Temperature'])

        # We need to get the correct volume, depending on whether or not we are
        # looking at the core
        if len(glob.glob('../CYLINDER')) > 0:
            V = np.pi*(1.75)**2*float(pimc.params[ID]['Container Length'])
        else:
            V = float(pimc.params[ID]['Container Volume'])

        # Compute the average compressibility and its error
        estData = np.loadtxt(fname,ndmin=2)

        N     = estData[:,headers.index('N')]
        N2    = estData[:,headers.index('N^2')] 
        N3 = N*N2

        numBins = len(N)

        # Get the averages
        aveN,errN = getStats(N)
        aveN2,errN2 = getStats(N2)
        aveNN2,errNN2 = getStats(N3)


        # Get the covariance
        # This is finite, so it must be calculated!
        covNN2 = (aveNN2 - aveN*aveN2)/(1.0*numBins-1.0)

        # Get the value of rho^2 * kappa and the error
        aveKappa[i] = (aveN2-aveN**2)/(T*V)
        errKappa[i] = np.sqrt(errN2**2 + 4.0*errN**2*aveN**2 - 4.0*aveN*covNN2)/(T*V)
    
    # output the estimator data to disk
    outFile = open('%s-%s' % ('kappa',outName),'w');

    # the headers
    outFile.write('#%15s' % reduceFlag[0])
    outFile.write('%16s%16s' % ('kappa','+/-'))
    outFile.write('\n')

    # the data
    for i in range(len(fileNames)):
        outFile.write('%16.8E' % float(pimc.params[pimc.id[i]][reduceFlag[1]]))
        outFile.write('%16.8E%16.8E\n' % (aveKappa[i],errKappa[i]))
    outFile.close()

    return aveKappa,errKappa


# -----------------------------------------------------------------------------
# Begin Main Program 
# -----------------------------------------------------------------------------
def main():

    # define the mapping between short names and label names 
    shortFlags = ['n','T','N','t','u','V','L','W','D']
    parMap = {'n':'Initial Density', 'T':'Temperature', 'N':'Initial Number Particles',
              't':'Imaginary Time Step', 'u':'Chemical Potential', 'V':'Container Volume',
              'L':'Container Length', 'W':'Virial Window', 'M':'Update Length'}  #'M':'Update Slices (Mbar)'}
    
    # Set up the command line parser
    parser = argparse.ArgumentParser(description='''Takes PIMC data and reduces it over a desired variable. For example, take a parameter sweep 
    through chemical potential and organize data by chemical potential in one, unifying file. This particular script is a modification of 
    reduce-one.py designed to handle MERGED files that are the resulting of merging many random seeds.''') 
    parser.add_argument("-T", "--temperature",dest="T", type=float,
                      help="simulation temperature in Kelvin") 
    parser.add_argument("-N", "--number-particles", dest="N", type=int,
                      help="number of particles") 
    parser.add_argument("-n", "--density", dest="n",metavar="Density", type=float,
                      help="number density in Angstroms^{-d}")
    parser.add_argument("-t", "--imag-time-step", dest="tau", type=float,
                      help="imaginary time step")
    parser.add_argument("-u", "--chemical-potential", dest="mu", type=float,
                      help="chemical potential in Kelvin") 
    parser.add_argument("-L", "--Lz", dest="L", metavar="Simulation Cell Length",type=float,
                      help="Length in Angstroms") 
    parser.add_argument("-V", "--volume", dest="V", metavar="Container Volume",type=float,
                      help="volume in Angstroms^d") 
    parser.add_argument("-r", "--reduce", dest="reduce",metavar="Reduction Variable",
                      choices=['T','N','n','u','t','L','V','W','M'], 
                      help="variable name for reduction [T,N,n,u,t,L,V,W,M]") 
    parser.add_argument("--canonical", action="store_true",default=False,dest="canonical",
                      help="are we in the canonical ensemble?")
    parser.add_argument("-p", "--plot", action="store_true", default=False, dest="plot",
                      help="do we want to produce data plots?") 
    parser.add_argument("-R", "--radius", dest="R", metavar="Radius",type=float,
                      help="radius in Angstroms") 
    parser.add_argument("-s", "--skip", dest="skip",metavar='# bins to skip', default=0, type=int,
                      help="number of measurements to skip") 
    parser.add_argument("-e", "--estimator",metavar="Estimator", dest="estimator", type=str,
                      help="specify a single estimator to reduce") 
    parser.add_argument("-i", "--pimcid", dest="pimcid", metavar="PIMCID",type=str,
                      help="specify a single pimcid") 
    #parser.add_argument("--collect",action="store_true",default=False,help='''If data files are seperated into subdirectories under the basedir 
    #                  containing identical simulation parameters but varying process number, collect the files from MERGED into a directory called REDUCE 
    #                  and then execute reduction in REDUCE''')
    parser.add_argument("basedir",type=str,help='''Base directory in which reduce will be executed. Always
    add trailing slash when specifying directory path.''')
    args=parser.parse_args()
    
    # Make sure the user specified a reduce flag
    if (not args.reduce):
        parser.error("need a correct reduce flag (-r,--reduce): [T,N,n,u,t,L,V,W,D]")
     
    # Determine the working directory
    if args:
        baseDir = args.basedir
        if baseDir == '.':
            baseDir = ''
    else:
        baseDir = ''
    
    # Store the number of bins to skip
    skip = args.skip

    # Check that we are in the correct ensemble
    pimchelp.checkEnsemble(args.canonical)
    
    dataName,outName = pimchelp.getFileString(args)
    reduceFlag = []
    reduceFlag.append(args.reduce)
    reduceFlag.append(parMap[args.reduce])

    # Create the PIMC analysis helper and fill up the simulation parameters maps
    pimc = pimchelp.PimcHelp(dataName,args.canonical,baseDir=baseDir)
    pimc.getSimulationParameters()
    
    dataName,outName = pimchelp.getFileString(args)
    reduceFlag = []
    reduceFlag.append(args.reduce)
    reduceFlag.append(parMap[args.reduce])

    # Form the full output file name
    if args.R == None:
        outName += '.dat'
    else:
        outName += '-R-%04.1f.dat' % args.R

    # possible types of estimators we may want to reduce
    estList = ['estimator', 'super', 'obdm', 'pair', 'radial', 'number', 
               'radwind', 'radarea', 'planedensity', 'planearea',
               'planewind','virial','linedensity','linepotential']
    estDo = {e:False for e in estList}

    # if we specify a single estimator, only do that one
    if args.estimator:
        estDo[args.estimator] = True
    # otherwise test to see if the file exists
    else:
        for e in estList:
            if pimc.getFileList(e):
                estDo[e] = True
            else:
                estDo[e] = False

    # We first reduce the scalar estimators and output them to disk
    if estDo['estimator']:
        head1,scAve1,scErr1 = getScalarEst('estimator',pimc,outName,reduceFlag,skip=skip)

    if estDo['virial']:
        head1,scAve1,scErr1 = getScalarEst('virial',pimc,outName,reduceFlag,skip=skip)

    if estDo['super']:
        head2,scAve2,scErr2 = getScalarEst('super',pimc,outName,reduceFlag,skip=skip)

    # Now we do the normalized one body density matrix
    if estDo['obdm']:
        x1,ave1,err1 = getVectorEst('obdm',pimc,outName,reduceFlag,'r [A]','n(r)',skip=skip)

    # Now we do the pair correlation function
    if estDo['pair']:
        x2,ave2,err2 = getVectorEst('pair',pimc,outName,reduceFlag,'r [A]','g(r)',skip=skip)

    # The radial Density
    if estDo['radial']:
        x3,ave3,err3 = getVectorEst('radial',pimc,outName,reduceFlag,'r [A]','rho(r)',skip=skip)

    # Compute the number distribution function and compressibility if we are in
    # the grand canonical ensemble
    if estDo['number']:
        x4,ave4,err4 = getVectorEst('number',pimc,outName,reduceFlag,'N','P(N)',skip=skip)

# I don't know why this isn't working, MCStat is giving me an error, will
    # return to this later. AGD 
        #kappa,kappaErr = getKappa(pimc,outName,reduceFlag)

    # The radially averaged Winding superfluid density
    if estDo['radwind']:
        x5,ave5,err5 = getVectorEst('radwind',pimc,outName,reduceFlag,'r [A]','rho_s(r)',skip=skip)

    # The radially averaged area superfliud density
    if estDo['radarea']:
        x6,ave6,err6 = getVectorEst('radarea',pimc,outName,reduceFlag,'r [A]','rho_s(r)',skip=skip)

    if estDo['planewind']:
        x7,ave7,err7 = getVectorEst('planewind',pimc,outName,reduceFlag,'n','rho_s(r)',skip=skip)

    if estDo['planearea']:
        x8,ave8,err8 = getVectorEst('planearea',pimc,outName,reduceFlag,'n','rho_s(r)',skip=skip)

    if estDo['planedensity']:
        x9,ave9,err9 = getVectorEst('planedensity',pimc,outName,reduceFlag,'n','rho(r)',skip=skip)

    if estDo['linedensity']:
        x10,ave10,err10 = getVectorEst('linedensity',pimc,outName,reduceFlag,\
                                       'r [A]','rho1d(r)',skip=skip)
    if estDo['linepotential']:
        x11,ave11,err11 = getVectorEst('linepotential',pimc,outName,reduceFlag,\
                                       'r [A]','V1d(r)',skip=skip)

    # Do we show plots?
    if args.plot:

        figNum = 1
        # Get the changing parameter that we are plotting against
        param = []
        for ID in pimc.id:
            param.append(float(pimc.params[ID][reduceFlag[1]]))
        numParams = len(param)
        markers = loadgmt.getMarkerList()
        colors  = loadgmt.getColorList('cw/1','cw1-029',10)

        # -----------------------------------------------------------------------------
        # Plot the averaged data
        # -----------------------------------------------------------------------------
        if estDo['estimator']:

            headLab = ['E/N','K/N','V/N','N', 'diagonal']
            dataCol = []
            for head in headLab:
                n = 0
                for h in head1:
                    if head == h:
                        dataCol.append(n)
                        break
                    n += 1
            yLabelCol = ['Energy / N', 'Kinetic Energy / N', 'Potential Energy / N',\
                    'Number Particles', 'Diagonal Fraction']

        
            # ============================================================================
            # Figure -- Various thermodynamic quantities
            # ============================================================================
            for n in range(len(dataCol)):
                plt.figure(figNum)
                plt.connect('key_press_event',kevent.press)
        
                plt.errorbar(param, scAve1[:,dataCol[n]], yerr=scErr1[:,dataCol[n]],\
                        color=colors[n],marker=markers[n],markeredgecolor=colors[n],\
                        markersize=8,linestyle='None',capsize=4)
        
                plt.xlabel('%s'%args.reduce)
                plt.ylabel(yLabelCol[n])
                plt.tight_layout()
                figNum += 1
    
        # ============================================================================
        # Figure -- The superfluid density
        # ============================================================================
        if estDo['super']:
            plt.figure(figNum)
            plt.connect('key_press_event',kevent.press)
        
            plt.errorbar(param, scAve2[:,0], yerr=scErr2[:,0],\
                    color=colors[0],marker=markers[0],markeredgecolor=colors[0],\
                    markersize=8,linestyle='None',capsize=4)
        
            plt.tight_layout()
            plt.xlabel('%s'%args.reduce)
            plt.ylabel('Superfluid Density')
    
        # ============================================================================
        # Figure -- The one body density matrix
        # ============================================================================
        if estDo['obdm']:
            figNum += 1
            plt.figure(figNum)
            plt.connect('key_press_event',kevent.press)
            ax = plt.subplot(111)
    
            for n in range(numParams):
                lab = '%s = %s' % (args.reduce,param[n])
                plt.errorbar(x1[n,:], (ave1[n,:]+1.0E-15), err1[n,:],color=colors[n],marker=markers[0],\
                        markeredgecolor=colors[n], markersize=8,linestyle='None',label=lab)
    
                #axis([0,21,1.0E-5,1.1])
            plt.xlabel('r [Angstroms]')
            plt.ylabel('One Body Density Matrix')
            plt.tight_layout()
            plt.legend(loc='best', frameon=False, prop={'size':16},ncol=2)
    
        # ============================================================================
        # Figure -- The pair correlation function
        # ============================================================================
        if estDo['pair']:
            figNum += 1
            plt.figure(figNum)
            plt.connect('key_press_event',kevent.press)
        
            for n in range(numParams):
                lab = '%s = %s' % (args.reduce,param[n])
                plt.errorbar(x2[n,:], ave2[n,:], yerr=err2[n,:],color=colors[n],marker=markers[0],\
                        markeredgecolor=colors[n], markersize=8,linestyle='None',label=lab,capsize=6)
        
                #   axis([0,256,1.0E-5,1.2])
            plt.xlabel('r [Angstroms]')
            plt.ylabel('Pair Correlation Function')
            plt.legend(loc='best', frameon=False, prop={'size':16},ncol=2)
            plt.tight_layout()
    
        # We only plot the compressibility if we are in the grand-canonical ensemble
        if not args.canonical:
    
            # ============================================================================
            # Figure -- The Number distribution
            # ============================================================================
            if estDo['number']:
                figNum += 1
                plt.figure(figNum)
                plt.connect('key_press_event',kevent.press) 

                # Find which column contains the average number of particles
                for hn,h in enumerate(head1):
                    if h == 'N':
                        break

                for n in range(numParams): 
                    lab = '%s = %s' % (args.reduce,param[n]) 
                    aN = scAve1[n,hn] 
                    plt.errorbar(x4[n,:]-aN, ave4[n,:], err4[n,:],color=colors[n],marker=markers[0],\
                             markeredgecolor=colors[n],\
                             markersize=8,linestyle='None',label=lab,capsize=6) 
        
                plt.axis([-30,30,0.0,1.2])
                plt.xlabel(r'$N-\langle N \rangle$')
                plt.ylabel('P(N)')
                plt.tight_layout()
                plt.legend(loc='best', frameon=False, prop={'size':16},ncol=2)
        
                # ============================================================================
                # Figure -- The Compressibility
                # ============================================================================
                #figNum += 1
                #figure(figNum)
                #connect('key_press_event',kevent.press)

                #errorbar(param, kappa, yerr=kappaErr, color=colors[0],marker=markers[0],\
                #        markeredgecolor=colors[0], markersize=8,linestyle='None',capsize=6)
        
                #tight_layout()
                #xlabel('%s'%args.reduce)
                #ylabel(r'$\rho^2 \kappa$')
    
        # ============================================================================
        # Figure -- The radial density
        # ============================================================================
        if len(glob.glob('CYLINDER')) > 0:
            figNum += 1
            plt.figure(figNum)
            plt.connect('key_press_event',kevent.press)
            plt.ax = plt.subplot(111)
    
            for n in range(numParams):
                lab = '%s = %s' % (args.reduce,param[n])
                plt.errorbar(x3[n,:], (ave3[n,:]+1.0E-15), err3[n,:],color=colors[n],marker=markers[0],\
                        markeredgecolor=colors[n], markersize=8,linestyle='None',label=lab)
    
                #axis([0,21,1.0E-5,1.1])
            plt.tight_layout()
            plt.xlabel('r [Angstroms]')
            plt.ylabel('Radial Density')
            plt.legend(loc='best', frameon=False, prop={'size':16},ncol=2)
    
        plt.show()
        
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
if __name__ == "__main__": 
    main()

