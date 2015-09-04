# Kyle Robertson 
# 10/27/14
# Del Maestro Condensed Matter Research Group
#
# Description: This program calculates the Lennard Jones confinement potential 
# for an isolated hexagonal nanopore surrounded by uniformly polarizable material.The 
# side length and all LJ params are hard coded in and can be changed in main()
# by hand to examine different pore sizes and interaction parameters. It might
# be nice to use docopts so that these parameters can be entered at the 
# command line in the future. 

import numpy as np
import matplotlib.pyplot as plt

def getBounds(f,g,t):
    #Calculates all six bounds on theta and stores them in a list. The list
    #has toprightlbound as first entry and goes counterclockwise from there. 
    #Function returns that list of the bounds
    
    toprightlbound = np.arctan2(-g,(t-f)) 
    toprightubound = np.arctan2(((np.sqrt(3)/2)*t-g),((t/2)-f))
    topmiddleubound = np.arctan2(((np.sqrt(3)/2)*t-g),((-t/2)-f))
    topleftubound = np.arctan2(-g,(-(t+f)))        
    bottomleftubound = 2*np.pi + np.arctan2(((-np.sqrt(3)/2)*t-g),((-t/2)-f))
    bottommiddleubound = 2*np.pi + np.arctan2(((-np.sqrt(3)/2)*t-g),((t/2)-f))
    
    boundList = [toprightlbound,toprightubound,topmiddleubound,topleftubound,bottomleftubound,bottommiddleubound]
    
    return boundList
    
def SectionOnePot(f,g,t,a,b):
    
    V1 = (((-441*np.pi*np.cos(a))/(128*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9)) + 
   (3*np.pi*np.cos(a))/(8*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) - 
   (49*np.pi*np.cos(3*a))/(32*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (np.pi*np.cos(3*a))/(12*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) - 
   (63*np.pi*np.cos(5*a))/(320*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (9*np.pi*np.cos(7*a))/(256*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (7*np.pi*np.cos(9*a))/(1152*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (441*np.pi*np.cos(b))/(128*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (3*np.pi*np.cos(b))/(8*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) + 
   (49*np.pi*np.cos(3*b))/(32*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (np.pi*np.cos(3*b))/(12*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) + 
   (63*np.pi*np.cos(5*b))/(320*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (9*np.pi*np.cos(7*b))/(256*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (7*np.pi*np.cos(9*b))/(1152*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (441*np.sqrt(3)*np.pi*np.sin(a))/(128*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (3*np.sqrt(3)*np.pi*np.sin(a))/(8*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) - 
   (63*np.sqrt(3)*np.pi*np.sin(5*a))/(320*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (9*np.sqrt(3)*np.pi*np.sin(7*a))/(256*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) - 
   (441*np.sqrt(3)*np.pi*np.sin(b))/(128*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (3*np.sqrt(3)*np.pi*np.sin(b))/(8*(np.sqrt(3)*f + g - np.sqrt(3)*t)**3) + 
   (63*np.sqrt(3)*np.pi*np.sin(5*b))/(320*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9) + 
   (9*np.sqrt(3)*np.pi*np.sin(7*b))/(256*(np.sqrt(3)*f + g - np.sqrt(3)*t)**9))
    
    return V1

def SectionTwoPot(f,g,t,b,c):
    
    V2 = (np.pi/(5760*(2*g - np.sqrt(3)*t)**9))*(-39690*np.cos(b) + 8820*np.cos(3*b) - 
      2268*np.cos(5*b) + 405*np.cos(7*b) - 35*np.cos(9*b) + 39690*np.cos(c) - 8820*np.cos(3*c) + 
      480*(-2*g + np.sqrt(3)*t)**6*(9*np.cos(b) - np.cos(3*b) - 9*np.cos(c) + np.cos(3*c)) + 2268*np.cos(5*c) - 
      405*np.cos(7*c) + 35*np.cos(9*c))
    
    return V2
    
def SectionThreePot(f,g,t,c,d):

    V3 = (((-3*np.pi*np.cos(c))/(8*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3)) + 
   (441*np.pi*np.cos(c))/(128*(-g + np.sqrt(3)*(f + t))**9) - 
   (np.pi*np.cos(3*c))/(12*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3) + 
   (49*np.pi*np.cos(3*c))/(32*(-g + np.sqrt(3)*(f + t))**9) + 
   (63*np.pi*np.cos(5*c))/(320*(-g + np.sqrt(3)*(f + t))**9) - 
   (9*np.pi*np.cos(7*c))/(256*(-g + np.sqrt(3)*(f + t))**9) - 
   (7*np.pi*np.cos(9*c))/(1152*(-g + np.sqrt(3)*(f + t))**9) + 
   (3*np.pi*np.cos(d))/(8*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3) - 
   (441*np.pi*np.cos(d))/(128*(-g + np.sqrt(3)*(f + t))**9) + 
   (np.pi*np.cos(3*d))/(12*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3) - 
   (49*np.pi*np.cos(3*d))/(32*(-g + np.sqrt(3)*(f + t))**9) - 
   (63*np.pi*np.cos(5*d))/(320*(-g + np.sqrt(3)*(f + t))**9) + 
   (9*np.pi*np.cos(7*d))/(256*(-g + np.sqrt(3)*(f + t))**9) + 
   (7*np.pi*np.cos(9*d))/(1152*(-g + np.sqrt(3)*(f + t))**9) - 
   (3*np.sqrt(3)*np.pi*np.sin(c))/(8*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3) + 
   (441*np.sqrt(3)*np.pi*np.sin(c))/(128*(-g + np.sqrt(3)*(f + t))**9) - 
   (63*np.sqrt(3)*np.pi*np.sin(5*c))/(320*(-g + np.sqrt(3)*(f + t))**9) - 
   (9*np.sqrt(3)*np.pi*np.sin(7*c))/(256*(-g + np.sqrt(3)*(f + t))**9) + 
   (3*np.sqrt(3)*np.pi*np.sin(d))/(8*(np.sqrt(3)*f - g + np.sqrt(3)*t)**3) - 
   (441*np.sqrt(3)*np.pi*np.sin(d))/(128*(-g + np.sqrt(3)*(f + t))**9) + 
   (63*np.sqrt(3)*np.pi*np.sin(5*d))/(320*(-g + np.sqrt(3)*(f + t))**9) + 
   (9*np.sqrt(3)*np.pi*np.sin(7*d))/(256*(-g + np.sqrt(3)*(f + t))**9))
    
    return V3
    
def SectionFourPot(f,g,t,d,e):

    V4 = ((3*np.pi*np.cos(d))/(8*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) - 
   (441*np.pi*np.cos(d))/(128*(g + np.sqrt(3)*(f + t))**9) + 
   (np.pi*np.cos(3*d))/(12*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) - 
   (49*np.pi*np.cos(3*d))/(32*(g + np.sqrt(3)*(f + t))**9) - 
   (63*np.pi*np.cos(5*d))/(320*(g + np.sqrt(3)*(f + t))**9) + 
   (9*np.pi*np.cos(7*d))/(256*(g + np.sqrt(3)*(f + t))**9) + 
   (7*np.pi*np.cos(9*d))/(1152*(g + np.sqrt(3)*(f + t))**9) - 
   (3*np.pi*np.cos(e))/(8*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) + 
   (441*np.pi*np.cos(e))/(128*(g + np.sqrt(3)*(f + t))**9) - 
   (np.pi*np.cos(3*e))/(12*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) + 
   (49*np.pi*np.cos(3*e))/(32*(g + np.sqrt(3)*(f + t))**9) + 
   (63*np.pi*np.cos(5*e))/(320*(g + np.sqrt(3)*(f + t))**9) - 
   (9*np.pi*np.cos(7*e))/(256*(g + np.sqrt(3)*(f + t))**9) - 
   (7*np.pi*np.cos(9*e))/(1152*(g + np.sqrt(3)*(f + t))**9) - 
   (3*np.sqrt(3)*np.pi*np.sin(d))/(8*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) + 
   (441*np.sqrt(3)*np.pi*np.sin(d))/(128*(g + np.sqrt(3)*(f + t))**9) - 
   (63*np.sqrt(3)*np.pi*np.sin(5*d))/(320*(g + np.sqrt(3)*(f + t))**9) - 
   (9*np.sqrt(3)*np.pi*np.sin(7*d))/(256*(g + np.sqrt(3)*(f + t))**9) + 
   (3*np.sqrt(3)*np.pi*np.sin(e))/(8*(np.sqrt(3)*f + g + np.sqrt(3)*t)**3) - 
   (441*np.sqrt(3)*np.pi*np.sin(e))/(128*(g + np.sqrt(3)*(f + t))**9) + 
   (63*np.sqrt(3)*np.pi*np.sin(5*e))/(320*(g + np.sqrt(3)*(f + t))**9) + 
   (9*np.sqrt(3)*np.pi*np.sin(7*e))/(256*(g + np.sqrt(3)*(f + t))**9))
    return V4

def SectionFivePot(f,g,t,e,h):

    V5 = (np.pi/(5760*(2*g + np.sqrt(3)*t)**9))*(-39690*np.cos(e) + 8820*np.cos(3*e) - 
    2268*np.cos(5*e) + 405*np.cos(7*e) - 35*np.cos(9*e) + 39690*np.cos(h) - 8820*np.cos(3*h) + 
    480*(2*g + np.sqrt(3)*t)**6*(9*np.cos(e) - np.cos(3*e) - 9*np.cos(h) + np.cos(3*h)) + 2268*np.cos(5*h) - 
    405*np.cos(7*h) + 35*np.cos(9*h))
    
    return V5
    
def SectionSixPot(f,g,t,h,a):

    V6 = (np.pi/11520)*((480*(9*np.cos(a) + 2*np.cos(3*a) - 9*np.cos(h) - 2*np.cos(3*h) + 9*np.sqrt(3)*(np.sin(a) - np.sin(h))))/(np.sqrt(3)*f - g - 
    np.sqrt(3)*t)**3 + (1/((-np.sqrt(3))*f + g + np.sqrt(3)*t)**9)*(39690*np.cos(a) + 17640*np.cos(3*a) + 2268*np.cos(5*a) - 
    405*np.cos(7*a) - 70*np.cos(9*a) + 70*np.cos(9*h) - 9*(4410*np.cos(h) + 1960*np.cos(3*h) + 9*(28*np.cos(5*h) - 5*np.cos(7*h) + 
    np.sqrt(3)*(-490*np.sin(a) + 28*np.sin(5*a) + 5*np.sin(7*a) + 490*np.sin(h) - 28*np.sin(5*h) - 5*np.sin(7*h))))))
    
    return V6
          
def PotentialFunction(f,g,t, epsilon, sigma, density):
    
    # Handles collecting the potentials from each section and summing them. Also
    # calls retrieves the bounds on theta for each section from the getBounds 
    # function. Returns the value of the potential for and set of LJ params. 
    
    bounds = getBounds(f,g,t)
    
    a,b,c,d,e,h = bounds
    
    V1 = SectionOnePot(f,g,t,a,b)
    V2 = SectionTwoPot(f,g,t,b,c)
    V3 = SectionThreePot(f,g,t,c,d)
    V4 = SectionFourPot(f,g,t,d,e)
    V5 = SectionFivePot(f,g,t,e,h)
    V6 = SectionSixPot(f,g,t,h,a) 
    
    potList = [V1,V2,V3,V4,V5,V6]
    
    TotalPotential = 4*epsilon*density*sigma**3*sum(potList)
    
    return TotalPotential

def piOverThreePlots(t, epsilon, sigma, density): 
    # Calculates the potential along a line from the center to a corner and then
    # plots it. Only does so for one line, but can be expanded to check all 
    # six, ensuring six-fold symmetry of the potential. 
       
    fVec = np.linspace(0,t,1000)
    Potential = PotentialFunction(fVec, 0.0, t, epsilon, sigma, density)
    #path = '/Users/Kyle/local/PIMCPeriodicTheta/OUTPUT'
    #r, pimcPotential = np.loadtxt(path+'/gce-debug1-02.000-030.000--007.200-0.00400-186373083.dat', unpack=True)
    
    plt.figure(4)
    plt.subplot(211)
    plt.plot(fVec, Potential, label = "Analytic Solution")
    #plt.plot(r, pimcPotential, label = "PIMC Solution")
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.ylim(-200,10)
    plt.legend()
    plt.grid()
    plt.subplot(212)
    #plt.plot(r, pimcPotential, label = "PIMC Solution")
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.suptitle(r'$\frac{\pi}{3}$ Plots, Side Length = %2.1f' % (t), fontsize=20)
    plt.ylim(-4,1)
    plt.legend()
    plt.grid()
    plt.show()

def piOverSixPlots(t, epsilon, sigma, density):
    # Calculates the potential along a line from the center to the point 
    # bisecting an edge and then plots it. Only does so for one line, but can be
    # expanded to check all six, ensuring six-fold symmetry of the potential. 
    
    #fVec = np.linspace(0, (3.0/4.0)*t, 275)
    #gVec = (1.0/np.sqrt(3.0))*fVec
    
    gVec = np.linspace(0,(np.sqrt(3.0)/2.0)*t,1000)
    Potential = PotentialFunction(0.0,gVec,t,epsilon,sigma,density)
    #path = '/Users/Kyle/local/PIMC/OUTPUT'
    #r, pimcPotential = np.loadtxt(path+'/gce-debug2-02.000-030.000--007.200-0.00400-184694579.dat', unpack=True)
    plt.figure(5)
    plt.subplot(211)
    plt.plot(gVec, Potential, label = "Analytic Solution")
    #plt.plot((-1)*r, pimcPotential, label = "PIMC Solution")
    plt.legend(loc=2)
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.title(r'$\frac{\pi}{6}$ Plots, Side Length = %2.1f' % (t), fontsize=20,y=1.01)
    plt.ylim(-200,1)
    plt.grid()
    plt.subplot(212)
    #plt.plot((-1)*r, pimcPotential, label = "PIMC Solution")
    plt.legend(loc=2)
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.ylim(-2.5,1)
    plt.grid()
    plt.show() 
    
    
    
                    
def main():
    # The main driver for the program. 
    
    # The side length of the hexagon. Make sure its a float. 
    t=11.0
    
    # LJ Parameters 
    #epsilon = 1.0
    #sigma = 1.0 
    #density = 1.0 
    
    epsilon = 43.48
    sigma = 2.494
    density = .05982
    
    # Discretize space for the heat map
    fDim = 300
    gDim = 300
    tempF = np.linspace(-t, t, fDim)
    tempG = np.linspace(-(np.sqrt(3)/2)*t, (np.sqrt(3)/2)*t, gDim)
      
   # Fill matrix with values of potential for the heat map.
    
    #PotentialMatrix = np.zeros([fDim, gDim])
    #
    #for nf, f in enumerate(tempF): 
    #    for ng, g in enumerate(tempG):
    #        
    #        if -t/2 <= f <= t/2:
    #            if -(np.sqrt(3)/2)*t < g < (np.sqrt(3)/2)*t:
    #                PotentialMatrix[ng, nf] = PotentialFunction(f,g,t,epsilon,sigma,density)
    #            else:
    #                PotentialMatrix[ng,nf] = None       
    #        elif -t < f < -t/2:
    #            if -np.sqrt(3)*(f+t) < g < np.sqrt(3)*(f+t):
    #                PotentialMatrix[ng, nf] = PotentialFunction(f,g,t,epsilon,sigma,density)  
    #            else:
    #                PotentialMatrix[ng,nf] = None  
    #        elif t/2 < f < t:
    #            if np.sqrt(3)*(f-t) < g < -np.sqrt(3)*(f-t):
    #                PotentialMatrix[ng, nf] = PotentialFunction(f,g,t,epsilon,sigma,density)
    #            else:
    #                PotentialMatrix[ng,nf] = None
    #        else:
    #            PotentialMatrix[ng,nf] = None 
    
    # Plot potential along specific lines at a fixed angle
    piOverThreePlots(t, epsilon, sigma, density)
    piOverSixPlots(t, epsilon, sigma, density)
    
    # Create heat map of Potential Matrix
    #plt.figure(1)
    #plt.imshow(PotentialMatrix, vmin=-1,vmax=1)
    #cbar = plt.colorbar()
    #cbar.set_label("Normalized Magnitude of Potential",fontsize=16,labelpad=20,rotation=270)
    #plt.suptitle('Unitless Potential: ' + 'Side Length = %s'%(t), fontsize=20)
    #plt.xlabel("X",fontsize=18)
    #plt.ylabel("Y",fontsize=18)
    ##plt.xticks(np.arange(0,fDim+(fDim/(2*t)),fDim/(2*t)),range(-t,t+1))
    ##plt.yticks(np.arange(0,fDim+(fDim/(2*t)),fDim/(2*t)),range(-t,t+1))
    #plt.show()  
    
if __name__=='__main__':
    main()