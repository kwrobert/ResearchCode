import os
import subprocess 
import glob
import argparse

def sh(cmd):
    '''A useful function that allows direct access to the bash shell. Simply type what you usually would at 
    the terminal into this function and you can interact with the bash shell'''
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).communicate()[0]
    
def main():
    parser = argparse.ArgumentParser(description='''Sorts image files based on some varying parameter in their name''')
    parser.add_argument('path',type=str,help='''Path to image files that need to be sorted, always add trailing slash.''')
    args = parser.parse_args()
    
    path = args.path
    print path
    
    os.chdir(path) 
    files = glob.glob('*.png')
    print files
    
    vals = []
    for n in range(len(files)):
        i = files[n].find('=')
        j = files[n].find('.png')
        vals.append(int(files[n][i+1:j]))

    vals, files = (list(t) for t in zip(*sorted(zip(vals, files))))
    
    print vals
    print files
    
    count = 1
    for pic in files:
        cmd  = 'cp %s plot%i.png'%(pic, count)
        sh(cmd)
        count += 1
    
if __name__=='__main__':
    main()