import argparse
import os
import subprocess
import shutil

def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually would at 
    the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    
def main():
    parser = argparse.ArgumentParser(description='''Creates directory structure necessary for
            running jobs on VACC using vaccsubmit.py. As of 6/14/15 all this does is add the OUTPUT
            directory if files already exist in subdirs characterized by parameter set. Must add
            functionality to organize a huge jumbled mess of data files.''')
    parser.add_argument('-d','--directory',dest='d',type=str,help='''Parent directory containing subdirectories that need restructuring exist. Always add the trailing slash''')
    args=parser.parse_args()
    
    parentdir=args.d
    print parentdir
    for subdir in os.listdir(parentdir):
        print subdir
        subdir = os.path.join(parentdir,subdir)
        if os.path.isdir(subdir):
            print 'isdir'
            os.chdir(subdir)
            print os.getcwd()
            print os.listdir(os.getcwd())
            if not ('OUTPUT' in os.listdir(os.getcwd())):
                os.mkdir('OUTPUT')
                print 'making output'
            sh('mv *ce-*.dat OUTPUT')
            os.chdir(parentdir)
                          
if __name__=='__main__':
    main()
