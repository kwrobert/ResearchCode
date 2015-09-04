from scipy.integrate import dblquad
from scipy.optimize import curve_fit 
import mplrcparamslineplot
import matplotlib.pyplot as plt
import numpy as np

def integrand(x,y):
    # The integrand of the numerical integrals for the hexagonal chunks 
    return (63*np.pi/(256*(x**2+y**2)**(11.0/2)) - (3*np.pi/(8*(x**2+y**2)**(5.0/2))))
        
def CavityIntegral(a,b,t):
    
    # Integrate over the top and bottom half of the hexagonal chunk we are
    # trying to remove. 
    
    TopIntegral = dblquad(integrand, b, b + (np.sqrt(3.0)/2.0)*t, lambda y: y/np.sqrt(3.0) - b/np.sqrt(3.0) + a - t, lambda y: -y/np.sqrt(3.0) + b/np.sqrt(3.0) + a +t)
    BottomIntegral = dblquad(integrand,  b - (np.sqrt(3.0)/2.0)*t, b, lambda y: -y/np.sqrt(3.0) + b/np.sqrt(3.0) + a - t, lambda y: y/np.sqrt(3.0) - b/np.sqrt(3.0) + a +t)
    
    return TopIntegral[0] + BottomIntegral[0]
    
def CavitiesCalculation(f, g, t, T, radius, epsilon, sigma, density):
    # Iterate over an array of cavities with two different shapes using
    # two lattice vectors u and v. The correct linear combo of these 
    # lattice vectors will get you to the center of any hexagon in the lattice.
 
    # Define the lattice vectors
    u = np.array([(3.0/2.0)*T, (np.sqrt(3.0)/2.0)*T])
    v = np.array([0,np.sqrt(3.0)*T])
    
    # Define the accumulator that is going to hold the sum of the contributions
    # to the potential from each cavity/prism
    
    total = 0.0
    
    # A rectangular array of hexagonal pores. Width controls how many hexagons
    # are to the left and right of the central hexagon. So the total number of 
    # hexagons from left to right is 2*width+1 (to account for the central 
    # column). The height in hexagons is always width+2. 
    
    #counter1 = 0
    #counter2 = 1
    #width = 4
    #for i in range(-width, width+1):
    #    if (i%2) == 0:
    #        for j in range(-counter1, width+1-counter1): 
    #            if (i==0) and (j==0):
    #                pass
    #            else:
    #                R = i*u + j*v
    #                total += CavityIntegral(R[0]-f,R[1]-g,t)
    #        counter1 +=1
    #    else: 
    #        for j in range(-counter1, width+2-counter1): 
    #            if (i==0) and (j==0):
    #                pass
    #            else:
    #                R = i*u + j*v
    #                total += CavityIntegral(R[0]-f,R[1]-g,t)
    #        counter2 +=1
    
    # An array of hexagonal pores arranged in concentric rings. Function arg 
    # Radius controls the number of rings. 
    counter = 0
    counter2 = radius
    for i in range(-radius, radius+1):
        if i < 0:
            for j in range(-counter, -i+counter+1):
                R = i*u + j*v
                total += CavityIntegral(R[0]-f,R[1]-g,t)
        elif i == 0:
            for j in range(-radius, 0):
                R = i*u + j*v
                total += CavityIntegral(R[0]-f,R[1]-g,t)
            for j in range(1, radius+1):
                R = i*u + j*v
                total += CavityIntegral(R[0]-f,R[1]-g,t)
        elif i > 0:
            for j in range(-counter2-i+1, counter2):
                R = i*u + j*v
                total += CavityIntegral(R[0]-f,R[1]-g,t)
            counter2 -= 1
        counter += 1 
    return 4*epsilon*density*sigma**3*total

def getBounds(f,g,t):
    # Calculates all six bounds on theta and stores them in a list. The list
    # has toprightlbound as first entry and goes counterclockwise from there. 
    # Function returns that list of the bounds
    
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
          
def AllSpaceCalculation(f,g,t,epsilon,sigma,density):
    
    # Takes care of calculating the LJ potential for a hexagonal pore 
    # completely surrounded on all sides by uniformly polarizable material
    
    # Make f and g dimensionLESS
    
    #f = f/sigma
    #g = g/sigma
    
    bounds = getBounds(f,g,t)
    
    a,b,c,d,e,h = bounds
    
    V1 = SectionOnePot(f,g,t,a,b)
    V2 = SectionTwoPot(f,g,t,b,c)
    V3 = SectionThreePot(f,g,t,c,d)
    V4 = SectionFourPot(f,g,t,d,e)
    V5 = SectionFivePot(f,g,t,e,h)
    V6 = SectionSixPot(f,g,t,h,a) 
        
    return 4*epsilon*density*sigma**3*(V1 + V2 + V3 + V4 + V5 + V6)    

def FittingAllSpaceCalculation(f,fitfactor):
    
    # Literally identical to AllSpaceCalculation with the arguments altered 
    # so it can be used with scipy.optimize.curve_fit in the EpsilonFit 
    # function. It only check along the line from the center to a corner, and
    # the value for t is hard coded in. 
    
    # LJ params. !!!!!!!!!!Make sure these match the ones in main()!!!!!!!!!!!!
    #epsilon = 43.48 # kelvin
    #sigma = 2.494 # angstroms
    #density = .05982 # atoms/angstrom^3
    
    epsilon = 1.0 # kelvin
    sigma = 1.0 # angstroms
    density = 1.0 # atoms/angstrom^3
    
    g = 0.0
    t = 9.0
    
    # Make f and g dimensionful
    #f = f/sigma
    #g = g/sigma
    bounds = getBounds(f,g,t)
    
    a,b,c,d,e,h = bounds
    
    V1 = SectionOnePot(f,g,t,a,b)
    V2 = SectionTwoPot(f,g,t,b,c)
    V3 = SectionThreePot(f,g,t,c,d)
    V4 = SectionFourPot(f,g,t,d,e)
    V5 = SectionFivePot(f,g,t,e,h)
    V6 = SectionSixPot(f,g,t,h,a) 
        
    return 4.0*fitfactor*epsilon*density*sigma**3*(V1 + V2 + V3 + V4 + V5 + V6)  
         
def piOverThreePlots(t,T,radius, epsilon, sigma, density):
    # Method for creating plots from center to a corner. The for loop is 
    # necessary because dblquad can't take a vector of bounds so the input to 
    # the CavitiesCalculation function cannot be vectorized. This only checks
    # one of the lines but this can be easily expanded to check all six if the 
    # symmetry of the potential needs to be verified (which it already has).
    
    numsteps = 500
    fVec = np.linspace(0, t, numsteps)
    AllSpaceCalc = np.zeros(numsteps)
    CavitiesCalc = np.zeros(numsteps)
    for i in range(len(fVec)-1):
        allspaceval = AllSpaceCalculation(fVec[i],0.0,t,epsilon,sigma,density)
        cavitiesval = allspaceval - CavitiesCalculation(fVec[i],0.0,t,T,radius,epsilon,sigma,density)
        AllSpaceCalc[i] = allspaceval
        CavitiesCalc[i] = cavitiesval
    plt.figure(1)        
    plt.plot(fVec,CavitiesCalc, label = 'Cavities Calculation')
    plt.plot(fVec,AllSpaceCalc, label = 'All Space Calculation')
    plt.xlabel(r"Radial Distance from Center $[\AA]$")
    plt.ylabel("Potential [K]")
    plt.title(r"$\theta = \frac{\pi}{3}$, Side Length = %2.1f" % (t),y=1.01)
    plt.ylim(-150,1)
    plt.legend(loc='lower left')
    plt.show()
    
def piOverSixPlots(t,T,radius, epsilon, sigma, density):
    # Method for creating plots from center to center of an edge. The for loop
    # is necessary because dblquad can't take a vector of bounds so the input to 
    # the CavitiesCalculation function cannot be vectorized. This only checks
    # one of the lines but this can be easily expanded to check all six if the 
    # symmetry of the potential needs to be verified (which it already has).
    
    numsteps = 500
    gVec = np.linspace(0, (np.sqrt(3.0)/2.0)*t, numsteps)
    AllSpaceCalc = np.zeros(numsteps)
    CavitiesCalc = np.zeros(numsteps)
    for i in range(len(gVec)-1):
        allspaceval = AllSpaceCalculation(0.0,gVec[i],t,epsilon,sigma,density)
        cavitiesval = allspaceval - CavitiesCalculation(0.0,gVec[i],t,T,radius,epsilon,sigma,density)
        AllSpaceCalc[i] = allspaceval
        CavitiesCalc[i] = cavitiesval
    plt.figure(2)        
    plt.plot(gVec,CavitiesCalc, label = 'Cavities Calculation')
    plt.plot(gVec,AllSpaceCalc, label = 'All Space Calculation')
    plt.xlabel(r'Radial Distance from Center $[\AA]$')
    plt.ylabel("Potential [K]")
    plt.title(r'$\theta = \frac{\pi}{6}$, Side Length = %2.1f' % (t), y=1.01)
    plt.ylim(-110,1)
    plt.xlim(0,(np.sqrt(3.0)/2.0)*t)
    plt.legend(loc='lower left')
    plt.show()
    
def MinimaSearch(T, t, radius, epsilon, sigma, density):
    # This function examines how the difference between the isolated pore 
    # calculation and the cavities calculation scales with the size of the 
    # cavity array for a given pore size. It does this by simply looking at 
    # the minima of the two calculations and comparing the difference between
    # those. 
    
    # Create a vector of f values that zooms in on the potential minima. Note
    # we are only checking along a line from the center to a corner. 
    fvec = np.linspace(t-2, t, 300)
    
    # Create the empty arrays that will store the values of the radii and the 
    # difference in the minima at those radius values. 
    diffvec = np.array([])
    radiusvec = np.array([])
    
    # Loop through each radius value and calculate the difference
    for radius in range(1, radius+1):
        allspace = AllSpaceCalculation(fvec,0.0,t, epsilon, sigma, density)
        cavities = np.array([])
        for j in range(len(fvec)):
            val = allspace[j] - CavitiesCalculation(fvec[j],0.0,t,T, radius, epsilon, sigma, density)
            cavities = np.append(cavities, val)
        allspaceminima = np.nanmin(allspace)
        cavitiesminima = np.nanmin(cavities)
        diff = cavitiesminima - allspaceminima
        diffvec = np.append(diffvec, diff)
        radiusvec = np.append(radiusvec,radius)
        
    plt.figure(3)
    plt.plot(radiusvec,diffvec)
    plt.xlabel('Number of Rings')
    plt.ylabel('Difference in Potential')
    plt.title('Side Length = %d' % (t))
    plt.show()

def EpsilonFit(t, T, radius, epsilon, sigma, density):
    
    # This function attempts to fit the All Space calculation to the Cavities 
    # calculation by using epsilon as a tunable fitting parameter, since the 
    # cavities only serve to reduce epsilon and thus decrease the depth of the 
    # potential well. 
    
    # !!!!!Make sure the LJ params in FittingAllSpaceCalculation match the ones
    # in main()!!!!!!!
    
    # Gather our data for the silicate calculation by zooming in on the 
    # the potential minima. Otherwise, the error in the hard wall and the flat
    # portion in the center will prevent the fit from changing epsilon at all. 
    fvec = np.linspace(t-1.25, t-.9, 900)
    silicate = np.array([])
    for j in range(len(fvec)):
        val = FittingAllSpaceCalculation(fvec[j],1.0) - CavitiesCalculation(fvec[j],0.0,t,T,radius,epsilon,sigma,density)
        silicate = np.append(silicate, val)
    
    #Plot truncated curves 
    allspace = FittingAllSpaceCalculation(fvec,1.0)
    plt.figure(4)
    plt.plot(fvec, allspace, label = 'All Space')
    plt.plot(fvec,silicate,label = 'Silicate')
    plt.xlabel('Radial Distance')
    plt.ylabel('Potential')
    plt.legend(loc='upper center')
    plt.title('Potential Minima, t = %i'%int(t))
    plt.show()
    
    #Get the fit
    popt, pcov = curve_fit(FittingAllSpaceCalculation, fvec, silicate, .9) 
    
    # Recalculate original silicate curve without zooming in on minima. 
    fvec = np.linspace(0, t, 900)
    silicate = np.array([])
    for j in range(len(fvec)):
        val = FittingAllSpaceCalculation(fvec[j],1.0) - CavitiesCalculation(fvec[j],0.0,t,T, radius,epsilon,sigma,density)
        silicate = np.append(silicate, val)
    # Recalculate AllSpace using new fit parameter
    fittedVals = FittingAllSpaceCalculation(fvec,popt[0])
    
    # Plot everything
    plt.figure(5)
    plt.plot(fvec, silicate, label='Silicate Calculation')
    plt.plot(fvec,fittedVals, label='Isolated Pore Fit, \epsilon^* = %f\epsilon' %(popt[0]))
    plt.legend(loc='upper center')
    plt.ylim(-4,1)
    plt.title('Results of Fit, t= %i'%int(t))
    plt.xlabel('Radial Distance')
    plt.ylabel('Potential')
    plt.show()

def main():
    
    # The main driver that brings together the AllSpace calculation and the 
    # Cavities calculation 
    
    # Define length scales
    t = 6.0
    T = t + 2.0
    
    
    # LJ params
    epsilon = 43.48 # kelvin
    sigma = 2.494 # angstroms
    density = .05982 # atoms/angstrom^3
    
    #epsilon = 1.0 # kelvin
    #sigma = 1.0 # angstroms
    #density = 1.0 # atoms/angstrom^3
    
    #Define size of array
    radius = 8
    
    ## Vectorize space for heat map
    #fDim = 100
    #gDim = 100
    #tempF = np.linspace(-t, t, fDim)
    #tempG = np.linspace(-(np.sqrt(3)/2)*t, (np.sqrt(3)/2)*t, gDim) 
    #
    ## Allocate space for matrix used in heat map
    #PotentialMatrix = np.zeros([fDim, gDim])
    #
    ## Fill matrix for heat map
    #for nf, f in enumerate(tempF): 
    #    for ng, g in enumerate(tempG):
    #        
    #        if -t/2 <= f <= t/2:
    #            if -(np.sqrt(3)/2)*t < g < (np.sqrt(3)/2)*t:
    #                PotentialMatrix[ng, nf] = AllSpaceCalculation(f,g,t,epsilon,sigma,density) - CavitiesCalculation(f,g,t,T, radius)
    #            else:
    #                PotentialMatrix[ng,nf] = None       
    #        elif -t < f < -t/2:
    #            if -np.sqrt(3)*(f+t) < g < np.sqrt(3)*(f+t):
    #                PotentialMatrix[ng, nf] = AllSpaceCalculation(f,g,t,epsilon,sigma,density) - CavitiesCalculation(f,g,t,T, radius)  
    #            else:
    #                PotentialMatrix[ng,nf] = None  
    #        elif t/2 < f < t:
    #            if np.sqrt(3)*(f-t) < g < -np.sqrt(3)*(f-t):
    #                PotentialMatrix[ng, nf] = AllSpaceCalculation(f,g,t,epsilon,sigma,density) - CavitiesCalculation(f,g,t,T, radius)
    #            else:
    #                PotentialMatrix[ng,nf] = None
    #        else:
    #            PotentialMatrix[ng,nf] = None 
    
    #MinimaSearch(T,t, radius, epsilon, sigma, density)
    #EpsilonFit(t,T,radius,epsilon,sigma,density)
    piOverThreePlots(t,T,radius,epsilon,sigma,density)
    #piOverSixPlots(t,T,radius,epsilon,sigma,density)
    # Creating density plot 
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