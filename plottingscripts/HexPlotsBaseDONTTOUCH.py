import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def getBounds(f,g,t):
    #Calculates all six bounds on theta and stores them in a list. The list
    #has toprightlbound as first entry and goes counterclockwise from there. 
    #Function returns that list of the bounds
    
    toprightlbound = np.arctan2(-g,(t-f))
    #if g<=0:
    #    toprightlbound = np.arctan2(-g,(t-f))
    #else:
    #    toprightlbound = 2*np.pi + np.arctan2(-g,(t-f))
        
    toprightubound = np.arctan2(((np.sqrt(3)/2)*t-g),((t/2)-f))
    topmiddleubound = np.arctan2(((np.sqrt(3)/2)*t-g),((-t/2)-f))
    
    topleftubound = np.arctan2(-g,(-(t+f)))
    #if g<=0:
    #    topleftubound = np.arctan2(-g,(-(t+f)))
    #else:
    #    topleftubound = 2*np.pi + np.arctan2(-g,(-(t+f)))
        
    bottomleftubound = 2*np.pi + np.arctan2(((-np.sqrt(3)/2)*t-g),((-t/2)-f))
    bottommiddleubound = 2*np.pi + np.arctan2(((-np.sqrt(3)/2)*t-g),((t/2)-f))
    
    #if f > t/2:
    #    toprightubound =  np.pi + np.arctan(((np.sqrt(3)/2)*t-g)/((t/2)-f))
    #elif f == t/2:
    #    toprightubound = np.pi/2
    #else:
    #    toprightubound = np.arctan(((np.sqrt(3)/2)*t-g)/((t/2)-f))
    #    
    #if f < -t/2:
    #     topmiddleubound = np.arctan(((np.sqrt(3)/2)*t-g)/((-t/2)-f))
    #elif f == -t/2:
    #    topmiddleubound = np.pi/2
    #else: 
    #    topmiddleubound = np.pi + np.arctan(((np.sqrt(3)/2)*t-g)/((-t/2)-f))
    #
    #topleftubound = 2*np.pi + np.arctan2(-g,(-(t+f)))
    #
    #if f < -t/2:
    #    bottomleftubound = (2*np.pi) + np.arctan(((-np.sqrt(3)/2)*t-g)/((-t/2)-f))
    #elif f == -t/2:
    #    bottomleftubound = (3/2)*np.pi
    #else:
    #    bottomleftubound = np.pi + np.arctan(((-np.sqrt(3)/2)*t-g)/((-t/2)-f))
    #
    #if f > t/2:
    #    bottommiddleubound = np.pi + np.arctan(((-np.sqrt(3)/2)*t-g)/((t/2)-f))
    #elif f == t/2:
    #    bottommiddleubound = (3/2)*np.pi
    #else:
    #    bottommiddleubound = (2*np.pi) + np.arctan(((-np.sqrt(3)/2)*t-g)/((t/2)-f))
    
    
    boundList = [toprightlbound,toprightubound,topmiddleubound,topleftubound,bottomleftubound,bottommiddleubound]
    
    #print 'The bounds are:'
    #print boundList
    
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
          
def PotentialFunction(f,g,t):
    
    bounds = getBounds(f,g,t)
    
    a,b,c,d,e,h = bounds
    
    V1 = SectionOnePot(f,g,t,a,b)
    V2 = SectionTwoPot(f,g,t,b,c)
    V3 = SectionThreePot(f,g,t,c,d)
    V4 = SectionFourPot(f,g,t,d,e)
    V5 = SectionFivePot(f,g,t,e,h)
    V6 = SectionSixPot(f,g,t,h,a) 
    
    potList = [V1,V2,V3,V4,V5,V6]
    
    TotalPotential = sum(potList)
    
    #print 'Values of the potential are:'
    #print potList
    #print 'The total potential is:'
    #print TotalPotential
    
    return TotalPotential

def piOverThreePlots(t):    
    f1Line = np.linspace(0,t,275)
    f2Line = np.linspace(-t,0,275)
    distanceList1 = []
    distanceList2 = []
    PotValues1 = []
    PotValues2 = []
    PotValues3 = []
    PotValues4 = []
    PotValues5 = []
    PotValues6 = []
    for f in f1Line:
        g1 = np.sqrt(3)*f
        g5 = -np.sqrt(3)*f
        distance1 = np.sqrt(g1**2 + f**2)
        if distance1 <= t:
            distanceList1.append(distance1)
            PotValue1 = PotentialFunction(f,g1,t)
            PotValues1.append(PotValue1)
            PotValue5 = PotentialFunction(f,g5,t)
            PotValues5.append(PotValue5)
        else:
            None
        PotValue6 = PotentialFunction(f,0,t)
        PotValues6.append(PotValue6)
        
    for f in f2Line:
        g2 = -np.sqrt(3)*f
        g4 = np.sqrt(3)*f
        distance2 = np.sqrt(g2**2+f**2)
        if distance2 <= t:
            distanceList2.append(distance2)
            PotValue2 = PotentialFunction(f,g2,t)
            PotValues2.append(PotValue2)
            PotValue4 = PotentialFunction(f,g4,t)
            PotValues4.append(PotValue4)
        else:
            None
        PotValue3 = PotentialFunction(f,0,t)
        PotValues3.append(PotValue3)
 
    PotValues3.reverse() 
    plt.figure(4)
    plt.plot(distanceList1,PotValues1,label='Theta=$\pi/3$')
    plt.plot(distanceList2,PotValues2,label='Theta=$2\pi/3$')
    plt.plot(f1Line,PotValues3,label='Theta=$\pi$')
    plt.plot(distanceList2,PotValues4,label='Theta=$4\pi/3$')
    plt.plot(distanceList1,PotValues5,label='Theta=$5\pi/3$')
    plt.plot(f1Line,PotValues6,label='Theta=$2\pi$')
    plt.legend(loc=2)
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.ylim(-1,1)
    plt.grid()
    plt.show()

def piOverSixPlots(t):    
    f1Line = np.linspace(0,t,275)
    f2Line = np.linspace(-t,0,275)
    distanceList1 = []
    distanceList2 = []
    PotValues1 = []
    PotValues2 = []
    PotValues3 = []
    PotValues4 = []
    PotValues5 = []
    PotValues6 = []
    for f in f1Line:
        g1 = (np.sqrt(3)/3)*f
        g5 = (-np.sqrt(3)/3)*f
        distance1 = np.sqrt(g1**2 + f**2)
        if distance1 <= ((np.sqrt(3)*t)/2):
            distanceList1.append(distance1)
            PotValue1 = PotentialFunction(f,g1,t)
            PotValues1.append(PotValue1)
            PotValue5 = PotentialFunction(f,g5,t)
            PotValues5.append(PotValue5)
        else:
            None
        
        
    for f in f2Line:
        g2 = (-np.sqrt(3)/3)*f
        g4 = (np.sqrt(3)/3)*f
        distance2 = np.sqrt(g2**2+f**2)
        if distance2 <= ((np.sqrt(3)*t)/2):
            distanceList2.append(distance2)
            PotValue2 = PotentialFunction(f,g2,t)
            PotValues2.append(PotValue2)
            PotValue4 = PotentialFunction(f,g4,t)
            PotValues4.append(PotValue4)
        else:
            None
    
    fZero1 = np.linspace(0,((np.sqrt(3)*t)/2),250)
    for g in fZero1:
        PotValue3 = PotentialFunction(0,g,t)
        PotValues3.append(PotValue3)
        PotValue6 = PotentialFunction(0,-g,t)
        PotValues6.append(PotValue6)   
        
    plt.figure(5)
    plt.plot(distanceList1,PotValues1,label='Theta=$\pi/6$')
    plt.plot(distanceList2,PotValues2,label='Theta=$5\pi/6$')
    plt.plot(fZero1,PotValues3,label='Theta=$\pi/2$')
    plt.plot(distanceList2,PotValues4,label='Theta=$7\pi/6$')
    plt.plot(distanceList1,PotValues5,label='Theta=$11\pi/6$')
    plt.plot(fZero1,PotValues6,label='Theta=$3\pi/2$')
    plt.legend(loc=2)
    plt.xlabel('Radial Distance from Center', fontsize=16)
    plt.ylabel(r'Effective Potential', fontsize=16)
    plt.tick_params(axis='x',labelsize=14)
    plt.tick_params(axis='y',labelsize=14)
    plt.ylim(-1,1)
    plt.grid()
    plt.show() 
                    
def main():
    
    t=6
    fDim = 250
    gDim = 250
    tempF = np.linspace(-t, t, fDim)
    tempG = np.linspace(-(np.sqrt(3)/2)*t, (np.sqrt(3)/2)*t, gDim)
      
   # Creating plot  
    
    PotentialMatrix = np.zeros([fDim, gDim])
    
    #PotentialFunction((t/2),((-np.sqrt(3)*8*t)/20),t)
    
    for nf, f in enumerate(tempF): 
        for ng, g in enumerate(tempG):
            
            if -t/2 <= f <= t/2:
                if -(np.sqrt(3)/2)*t < g < (np.sqrt(3)/2)*t:
                    PotentialMatrix[ng, nf] = PotentialFunction(f,g,t)
                else:
                    PotentialMatrix[ng,nf] = None       
            elif -t < f < -t/2:
                if -np.sqrt(3)*(f+t) < g < np.sqrt(3)*(f+t):
                    PotentialMatrix[ng, nf] = PotentialFunction(f,g,t)  
                else:
                    PotentialMatrix[ng,nf] = None  
            elif t/2 < f < t:
                if np.sqrt(3)*(f-t) < g < -np.sqrt(3)*(f-t):
                    PotentialMatrix[ng, nf] = PotentialFunction(f,g,t)
                else:
                    PotentialMatrix[ng,nf] = None
            else:
                PotentialMatrix[ng,nf] = None 
    
    piOverThreePlots(t)
    piOverSixPlots(t)
    
    plt.figure(1)
    plt.imshow(PotentialMatrix, vmin=-1,vmax=1)
    plt.colorbar()
    plt.suptitle('Side Length = %s'%(t))
    plt.show()  
    
if __name__=='__main__':
    main()