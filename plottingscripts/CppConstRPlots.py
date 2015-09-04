import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def main():
    path = '/Users/Kyle/local/PIMC/OUTPUT/'
    file1 = 'gce-debug2-02.000-040.000-+100.000-0.00400-192847962.dat'
    file2 = 'gce-debug4-02.000-030.000--007.200-0.00400-185160469.dat'
    
    theta1, potential1 = np.loadtxt(path+file1,unpack=True)
    #theta2, potential2 = np.loadtxt(path+file2,unpack=True)
    print max(potential1)
    print len(potential1)
    print np.argmax(potential1)
    for i in range(np.argmax(potential1), len(potential1)-1):
        print potential1[i]
    plt.figure(1)
    plt.plot(-theta1, potential1)
    plt.title('Potential')
    plt.xlabel('R')
    plt.ylabel('Potential')
    plt.ylim(2.8e67,3.0e68)
    plt.show()
    
    #plt.figure(2)
    #plt.plot(theta2, potential2)
    #plt.title('Potential for Constant R (5t/6')
    #plt.xlabel('Theta [Rads]')
    #plt.ylabel('Potential')
    #plt.ylim(-1,10)
    #plt.show()
    
if __name__== '__main__':
    main()