# File for importing plot options
import matplotlib 

matplotlib.rcParams['text.usetex'] = True
matplotlib.rc('font',family='serif',serif='cm',size=16.0)
#matplotlib.rc('axes',grid=True,linewidth=1.5,titlesize=20.0,labelsize=18.0,color_cycle='forestgreen')
matplotlib.rc('grid',linewidth=1.0,linestyle=':')
matplotlib.rc('axes',linewidth=1.5,titlesize=20.0,labelsize=18.0,color_cycle=['forestgreen','blue','red','yellow'])
matplotlib.rc('lines',linestyle='-',marker='o',markersize=8,markeredgewidth=1.0)
matplotlib.rc('patch',linewidth=2.0)
matplotlib.rc('xtick',labelsize=16.0)
matplotlib.rcParams['xtick.major.size'] = 7
matplotlib.rcParams['xtick.major.width'] = 1.2
matplotlib.rcParams['ytick.major.size'] = 7
matplotlib.rcParams['ytick.major.width'] = 1.2
matplotlib.rc('ytick',labelsize=16.0)