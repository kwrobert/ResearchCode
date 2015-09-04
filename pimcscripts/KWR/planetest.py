import pylab as pl

xvec = pl.linspace(-10,10,100)
yvec = pl.linspace(-10,10,100)
density=pl.zeros([100,100])
for nx, x in enumerate(xvec):
    for ny, y in enumerate(yvec):
        density[nx,ny] = x**2 + y**2
        
pl.imshow(density,cmap='BuGn',extent=[0,18,0,18])
pl.xlabel("X " + r"$(\AA)$",fontsize=18)
pl.ylabel("Y " + r"$(\AA)$",fontsize=18)
#pl.xlim([0,18])
#pl.ylim([0,18]) 
#pl.xticks(range(0,19),range(0,19))
#pl.yticks(range(0,19),range(0,19))
#pl.axis([0, 18, 0, 18])
cbar = pl.colorbar()
cbar.set_label("Particle Density"+ r"$\left(\frac{Particles}{\AA^3}\right)$",labelpad=30,fontsize=18,rotation=270)
pl.title( r"$%s = %s K$"%('\mu', 35),fontsize=24)
pl.show()