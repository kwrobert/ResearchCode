## Plot the Lennard Jones Potential in an Elliptical Nanopore
## along fixed angles

import numpy as np
import scipy as sp
import scipy.integrate
import matplotlib.pyplot as plt
from math import *

def IntegrateFunction(f, g, a, b):
    
    #Calculates the LJ Potential numerically for any point (f,g) inside an 
    #ellipse
    
    integrand = lambda angle:((7 - 32*(-((b**2*f*cos(angle) + 
              a**2*g*sin(angle))/(b**2*cos(angle)**2 + 
                        a**2*sin(angle)**2)) + 
         sqrt((b**2*f*cos(angle) + a**2*g*sin(angle))**2/
                      (b**2*cos(angle)**2 + 
               a**2*sin(angle)**2)**2 + ((-b**2)*f**2 + a**2*(b**2 - g**2))/
                      (b**2*cos(angle)**2 + a**2*sin(angle)**2)))**6))/(256*(-((b**2*f*cos(angle) + a**2*g*sin(angle))/(b**2*cos(angle)**2 + 
           a**2*sin(angle)**2)) + sqrt((b**2*f*cos(angle) + 
            a**2*g*sin(angle))**2/(b**2*cos(angle)**2 + 
            a**2*sin(angle)**2)**2 + 
               ((-b**2)*f**2 + a**2*(b**2 - g**2))/(b**2*cos(angle)**2 + 
           a**2*sin(angle)**2)))**9)
           
    I,error = sp.integrate.quad(integrand, 0, 2*pi)
    
    return I
        
def main():
    
    a = 25
    b = 5
    c = sqrt(a**2-b**2)
    
    fDim = 400
    gDim = 400
    tempF = np.linspace(0, a, fDim)
    tempG = np.linspace(0, b, gDim)
    
    #Pi/4 cut
    R = []
    feqgcut = []
    for f in tempF:
        test = sqrt((f + c)**2 + f**2) + sqrt((c - f)**2 + f**2)     
        if test < 2*a:
            r = sqrt(2)*f 
            R.append(r)
            feqgcut.append(IntegrateFunction(f,f,a,b))
    
    #pi/2 cut
    fzerocut = []  
    for g in tempG:
        fzerocut.append(IntegrateFunction(0.0,g,a,b))
    
    #angle=0 cut
    gzerocut = []  
    for f in tempF:
        gzerocut.append(IntegrateFunction(f,0.0,a,b))    
    
    plt.figure(1)
    plt.plot(tempF,gzerocut,label='Theta=0')
    plt.plot(tempG, fzerocut,label='Theta=$\pi/2$')
    plt.plot(R,feqgcut,label='Theta=$\pi/4$')
    plt.legend(loc=2)
    plt.xlabel('Radial Distance from Center', fontsize=20)
    plt.ylabel(r'Effective Potential', fontsize=20)
    plt.title('Semi Major Axis = %d Semi Minor Axis = %d' %(a,b),fontsize = 20)
    plt.tick_params(axis='x',labelsize=20)
    plt.tick_params(axis='y',labelsize=20)
    plt.ylim(-.4,1) 
    plt.show()
    #plt.savefig('EllipticalNanoporePlotFixedAngle.pdf', format='pdf', bbox_inches='tight')

if __name__=='__main__':
    main()
