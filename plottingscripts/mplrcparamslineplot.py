# File for importing plot options
import matplotlib 

matplotlib.rcParams['text.usetex'] = True
matplotlib.rc('font',family='serif',serif='Helvetica',size=16.0,weight=900)
matplotlib.rc('axes',grid=True,linewidth=1.5,titlesize=24.0,labelsize=22.0,color_cycle=['forestgreen','crimson'])
matplotlib.rc('grid',linewidth=1.0,linestyle=':')
#matplotlib.rc('axes',linewidth=1.5,titlesize=20.0,labelsize=18.0,color_cycle=['forestgreen','blue','red','yellow'])
matplotlib.rc('lines',linestyle='-',marker=None,linewidth=1.2)
matplotlib.rc('patch',linewidth=2.0)
matplotlib.rc('xtick',labelsize=20.0)
matplotlib.rcParams['xtick.major.size'] = 7
matplotlib.rcParams['xtick.major.width'] = 1.2
matplotlib.rcParams['ytick.major.size'] = 7
matplotlib.rcParams['ytick.major.width'] = 1.2
matplotlib.rc('ytick',labelsize=16.0)
#matplotlib.rc('figure',figsize=8,dpi=100)