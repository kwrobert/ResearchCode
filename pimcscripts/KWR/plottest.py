import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import mplrcparams

def main():
    x = np.linspace(-5.0,5.0,100)
    y = x*x
    plt.figure(1)
    plt.plot(x,y,label='x=y^2')
    plt.plot(x,y*y,label='x=y^4')
    plt.title("The Title")
    plt.xlabel("Stuff w/ tex $\epsilon$")
    plt.ylabel("More stuff")
    plt.legend(loc='best')
    plt.show()
main()