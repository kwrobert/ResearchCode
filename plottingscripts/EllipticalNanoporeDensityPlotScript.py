# -*- coding: utf-8 -*-
"""
Created on Sun Mar 30 14:05:14 2014

@author: Kyle
"""

##Plot the Lennard Jones Potential in an elliptical nanopore

import numpy as np
import scipy as sp
import scipy.integrate
import matplotlib.pyplot as plt
from math import *

def IntegrateFunction(f, g, a, b):
    
    #Calculates the LJ Potential numerically for any point (f,g) inside an 
    #ellipse
    
    integrand = lambda angle:(pi*(7 - 32*(-((b**2*f*cos(angle) + 
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
    
    a = input('What is the length of the semi major axis?')
    b = input('What is the length of the semi minor axis?')
    c = sqrt(a**2-b**2)
    
    fDim = 350
    gDim = 350
    tempF = np.linspace(-a, a, fDim)
    tempG = np.linspace(-b, b, gDim)
    print tempF
    print tempG
   # Creating plot  
    
    PotentialMatrix = np.zeros([fDim, gDim])
    
    for nf, f in enumerate(tempF): 
        for ng, g in enumerate(tempG):
                            
            test = sqrt((f + c)**2 + g**2) + sqrt((c - f)**2 + g**2) 
                
            if test < 2*a:
                PotentialMatrix[ng, nf] = IntegrateFunction(f,g,a,b)
            else:
                PotentialMatrix[ng,nf] = None 
    
#    for row in PotentialMatrix:
#        list = []
#        for element in row:
#            list.append(element)
#        print list 
    
    plt.figure(1)
    plt.imshow(PotentialMatrix, vmin=-1,vmax=1)
    plt.colorbar()
    plt.suptitle('Semi-Major Axis=10 Semi-Minor Axis=10')
    plt.show()
    
if __name__=='__main__':
    main()
