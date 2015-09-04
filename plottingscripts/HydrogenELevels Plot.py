# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:03:47 2013

@author: Kyle
"""

## Plot the energy levels of the hydrogen atom
import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from math import *
        
def CoordinateConverter(x, y, z):
    #phi is polar angle and theta is azimuthal angle

    r = sqrt(x**2+y**2+z**2)
    phi = np.arccos(z/r)
    if x == 0:
        theta = 0
    else:
        theta = np.arctan(y/x)
    
    return r, phi, theta
    
    
def WaveFunction(x, y, z, n, l, m):
    
    # theta is azimuthal angle and phi is polar angle  
    r, phi, theta = CoordinateConverter(x, y, z)
    # a is the Bohr radius in angstroms
    
    a = .529 
    
    spherical = special.sph_harm(m, n, theta, phi)
    
    LaguerreOrder = 2*l + 1
    LaguerrePoint = (2*r)/(n*a)
    laguerre = special.assoc_laguerre(LaguerreOrder, LaguerrePoint)
    radial = sqrt((2/(n*a))**3 * (float(factorial(n-l-1))/(float(2*n*(factorial(n+l))**3))))*exp(-r/(n*a))*((2*r)/(n*a))**l
    
    value = radial * laguerre * spherical
    probability = abs(value)**2
    
    return probability
    
def main():
    
    xDim = 100
    yDim = 100
    zDim = 100
    tempX = np.linspace(-10, 10, xDim)
    tempY = np.linspace(-10, 10, yDim)
    tempZ = np.linspace(-10, 10, zDim)
    
    n = input('Which principal quantum number?')
    l = input('Which azimuthal quantum number?')
    m = input('Which magnetic quantum number?')
   
   # plotting in the xz plane  
    
    ProbabilityMatrix = np.zeros([xDim, zDim])
    
    for nx, x in enumerate(tempX): 
        for nz, z in enumerate(tempZ):
            ProbabilityMatrix[nx, nz] = WaveFunction(x, 0, z, n, l, m)
    
    fig, ax = plt.subplots()
    cax = ax.imshow(ProbabilityMatrix,interpolation='nearest', cmap=cm.coolwarm)
    ax.set_title('XZ Projection')
    cbar = fig.colorbar(cax, ticks=[-10, 0, 10])
    cbar.ax.set_yticklabels(['Low', 'Medium', 'High'])
    fig.show()
    
    #plotting in the xy plane
    
    ProbabilityMatrix2 = np.zeros([xDim, yDim])
    for nx, x in enumerate(tempX): 
        for ny, y in enumerate(tempY):
            ProbabilityMatrix2[nx, ny] = WaveFunction(x, y, 0, n, l, m)
    
    fig2, ax2 = plt.subplots()
    cax2 = ax2.imshow(ProbabilityMatrix2,interpolation='nearest', cmap=cm.coolwarm)
    ax2.set_title('XY Projection')
    cbar2 = fig2.colorbar(cax2, ticks=[-10, 0, 10])
    cbar2.ax.set_yticklabels(['Low', 'Medium', 'High'])
    fig2.show()
    
    #plotting in yz plane
    
    ProbabilityMatrix3 = np.zeros([yDim, zDim])
    for nz, z in enumerate(tempZ): 
        for ny, y in enumerate(tempY):
            ProbabilityMatrix3[nz, ny] = WaveFunction(0, y, z, n, l, m)
    
    fig3, ax3 = plt.subplots()
    cax3 = ax3.imshow(ProbabilityMatrix3,interpolation='nearest', cmap=cm.coolwarm)
    ax3.set_title('YZ Projection')
    cbar3 = fig3.colorbar(cax3, ticks=[-10, 0, 10])
    cbar3.ax.set_yticklabels(['Low', 'Medium', 'High'])
    fig3.show()
    
if __name__=='__main__':
    main()
