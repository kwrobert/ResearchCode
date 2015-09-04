import os 
import argparse
import mergehelper
import subprocess

def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually would at 
    the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    
def removeFiles(fileList):
    '''Remove any files that are not data files'''
    return filter(lambda filename: (filename[-4:] == '.dat') and (filename[0] != '.'), fileList)

def getHeadersFromFile(fileName): 
    ''' Get the headers from a PIMC output file. '''

    with open(fileName,'r') as inFile:
        inLines = inFile.readlines();
        headers = [inLines[0], inLines[1]]
    return headers

def line_prepender(filename, line):
    ''''Add line to beginning of a file'''
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)   

def getID(fileName): 
    ''' Return the ID number corresponding to a given filename. '''
    ID = int(fileName[-13:-4])
    return ID        
    
def Add_Headers(datfile,estimator,sampledir):
    '''Adds correct headers to a data file that is missing them'''
    for samplefile in os.listdir(sampledir):
        if estimator in samplefile:
            headers=getHeadersFromFile(os.path.join(sampledir,samplefile))
    # Remove sample file PIMCID
    headers[0] = headers[0][0:-10]
    # Add datfile's PIMCID
    pimcid = getID(datfile)
    headers[0] = headers[0]+str(pimcid)
    # Add header lines to file
    line_prepender(datfile,headers[1])
    line_prepender(datfile,headers[0])
    
    return 0
             
def main():
    parser = argparse.ArgumentParser(description='''Checks all data files to make sure they have the required headers and adds them if they don't''')
    parser.add_argument("parentdir",type=str,help='''Parent directory where subdirectories containing data files of identical physical parameters that 
    may be missing headers exist. Always add the trailing slash''')
    parser.add_argument('samplefiles',type=str,help='''Path to directory containing correctly formatted sample files that the necessary headers will be pulled from''')
    args=parser.parse_args()
    
    parentdir = args.parentdir
    sampledir = args.samplefiles
    
    for root, dirs, files in os.walk(parentdir):
        datfiles = removeFiles(files)
        if len(datfiles) > 0:
            emptyfilesdir = root+'/emptyfiles'
            sh('mkdir %s'%emptyfilesdir)
        print '#'*22+' Subdirectory %s '%root+'#'*22+'\n'
        for datfile in datfiles:
            estimator = mergehelper.getEstimator(datfile)
            if (estimator == 'state') or (estimator == 'log'):
                pass
            else:
                filepath = os.path.join(root,datfile)
                with open(filepath,'r') as inFile:
                    lines = inFile.readlines()
                    if len(lines) <= 5:
                        print "%s FILE IS EMPTY, MOVING IT"%filepath
                        sh('mv %s %s'%(filepath,emptyfilesdir))
                    elif not "# PIMCID" in lines[0]:
                        print "%s FILE NEEDS HEADER"%filepath
                        Add_Headers(filepath,estimator,sampledir)
                    else:
                        print "%s HAS HEADER"%filepath
                            
    
if __name__=='__main__':
    main()